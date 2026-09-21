# -*- coding: utf-8 -*-
"""Audita el USO de Aurora 7 en páginas consumidoras (el lint del agente).

El validador del sistema (`validar-css.py`) comprueba los packs desde dentro.
Este comprueba las páginas que CONSUMEN Aurora 7 desde fuera: el HTML que un
agente (o una persona) genera enlazando el CDN. Es el paso que falta en el
bucle: la IA verifica su propio output antes de entregarlo.

Qué detecta:
  · clases nz-* inventadas (no existen en components.json)  → FALLO
  · clases del shell del catálogo (cat-*, demo-*)           → FALLO
  · packs del sistema que faltan por enlazar                → FALLO
  · CDN sin pinear (@master)                                → AVISO
  · gradientes, backdrop-filter, !important                 → FALLO (manifiesto)
  · colores a mano (#hex, rgb, hsl)                         → AVISO
  · desktop-first (@media max-width)                        → AVISO
  · falta body.nz / data-nz-theme / lang=es / atribución    → AVISO

Uso:
  python scripts/auditar-uso.py pagina.html [otra.html …]
  curl -s https://mi-sitio.es | python scripts/auditar-uso.py -
  python scripts/auditar-uso.py --selftest      # test de la propia herramienta

Salida: informe por página y código de salida 1 si hay fallos.
"""
import glob
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CDN_RE = re.compile(
    r'href="(https://cdn\.jsdelivr\.net/gh/Ntizar/Aurora7@([^/"]+)/([^"]+))"')
CLASE_RE = re.compile(r'class="([^"]*)"')
STYLE_RE = re.compile(r'style="([^"]*)"')
STYLE_BLOCK_RE = re.compile(r"<style[^>]*>(.*?)</style>", re.S)
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")
RGB_RE = re.compile(r"\b(?:rgb|rgba|hsl|hsla)\(")

# Clases legítimas que no viven en el censo de componentes
EXENTAS = {"nz", "nz-visually-hidden", "nz-vh", "nz-print-hide"}


def cargar_censo():
    ruta = ROOT / "components.json"
    if not ruta.exists():
        sys.exit("No existe components.json. Ejecuta antes: python scripts/generar-llm-docs.py")
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    clase_a_familia = {}
    for familia, objeto in datos["objetos"].items():
        for clase in objeto["clases"]:
            clase_a_familia[clase] = familia
    packs = set(datos["packs"].keys())
    return clase_a_familia, packs, datos["version"]


def auditar(html, clase_a_familia, packs_conocidos):
    """Devuelve (fallos, avisos, info) de una página."""
    fallos, avisos = [], []

    # --- 1. CDN enlazado -----------------------------------------------------
    enlaces = CDN_RE.findall(html)
    ficheros = {e[2] for e in enlaces}
    versiones = {e[1] for e in enlaces}
    if not enlaces:
        avisos.append("No enlaza el CDN de Aurora 7 (¿es una página Aurora?)")
    if "master" in versiones:
        avisos.append("CDN sin pinear (@master): jsDelivr puede servir CSS viejo desde su caché. Pineas con @vX.Y.Z")
    if enlaces and "tokens.css" not in ficheros and "all.css" in " ".join(ficheros):
        avisos.append("tokens.css no está enlazado: los packs lo necesitan para resolver los tokens")
    for _, _, fichero in enlaces:
        if fichero.startswith("packs/") and fichero != "packs/all.css":
            if fichero[len("packs/"):] not in packs_conocidos:
                fallos.append(f"Pack enlazado que no existe en el sistema: {fichero}")

    # --- 2. Clases -----------------------------------------------------------
    vistas = []
    for valor in CLASE_RE.findall(html):
        vistas.extend(valor.split())
    nz = {c for c in vistas if c.startswith("nz-")}
    invented = sorted(c for c in nz if c not in clase_a_familia and c not in EXENTAS)
    for c in invented:
        fallos.append(f"Clase inventada (no está en components.json): .{c}")
    for c in sorted({c for c in vistas if c.startswith(("cat-", "demo-"))}):
        fallos.append(f"Clase del shell del catálogo (no es del sistema): .{c}")

    # --- 3. Packs necesarios vs enlazados ------------------------------------
    if enlaces:
        # pack de cada familia usada
        familias = {clase_a_familia[c] for c in nz if c in clase_a_familia}
        necesarios = {FAMILIA_PACK.get(f, "") for f in familias}
        necesarios.discard("")
        enlazados = {f[len("packs/"):] for f in ficheros if f.startswith("packs/")}
        if "all.css" in enlazados:
            necesarios = set()  # all.css lo cubre todo
        for p in sorted(necesarios - enlazados):
            fallos.append(f"Falta por enlazar el pack {p} (lo usan clases de la página)")
        for p in sorted(enlazados - necesarios - {"all.css"}):
            avisos.append(f"Pack enlazado sin uso aparente: {p} (peso muerto, valora quitarlo)")

    # --- 4. Manifiesto en <style> y style="" ---------------------------------
    bloques = " ".join(STYLE_BLOCK_RE.findall(html))
    inline = " ".join(STYLE_RE.findall(html))
    for nombre, texto in (("<style>", bloques), ('style=""', inline)):
        if "gradient" in texto.lower():
            fallos.append(f"Gradiente en {nombre}: prohibido por el manifiesto")
        if "backdrop-filter" in texto.lower():
            fallos.append(f"backdrop-filter en {nombre}: prohibido por el manifiesto")
        if "!important" in texto:
            fallos.append(f"!important en {nombre}: prohibido por el manifiesto")
        for rx, etiqueta in ((HEX_RE, "hex"), (RGB_RE, "rgb/hsl")):
            toques = rx.findall(texto)
            if toques:
                avisos.append(
                    f"{len(toques)} color(es) {etiqueta} a mano en {nombre}: usa var(--nz-*) ({', '.join(toques[:3])}…)")
    if "@media" in bloques and re.search(r"@media[^{]*max-width", bloques):
        avisos.append("@media (max-width) detectado: Aurora 7 es mobile-first (base 1 columna + min-width)")

    # --- 5. Estructura mínima -------------------------------------------------
    if not re.search(r'<html[^>]*lang="es"', html):
        avisos.append('<html> sin lang="es"')
    if not re.search(r'<html[^>]*data-nz-theme="(light|dark)"', html):
        avisos.append('<html> sin data-nz-theme="light|dark"')
    if not re.search(r"<body[^>]*class=\"[^\"]*\bnz\b", html):
        avisos.append('<body> sin class="nz"')
    if "Hecho con ❤️ por David Antizar" not in html:
        avisos.append('Falta la atribución exacta: "Hecho con ❤️ por David Antizar"')

    return fallos, avisos


# mapa familia → pack, relleno al cargar el censo
FAMILIA_PACK = {}


def main():
    global FAMILIA_PACK
    args = sys.argv[1:]

    if args and args[0] == "--selftest":
        return selftest()

    clase_a_familia, packs_conocidos, version = cargar_censo()
    FAMILIA_PACK = {}
    censo = json.loads((ROOT / "components.json").read_text(encoding="utf-8"))
    for familia, objeto in censo["objetos"].items():
        FAMILIA_PACK[familia] = objeto["pack"]

    rutas = []
    for a in args:
        if a == "-":
            rutas.append(("-: stdin", sys.stdin.read()))
        elif "/" in a and a.startswith("http"):
            import urllib.request
            rutas.append((a, urllib.request.urlopen(a, timeout=30).read().decode("utf-8")))
        else:
            rutas.extend((str(p), p.read_text(encoding="utf-8"))
                         for p in [pathlib.Path(a)] if p.exists())
    if not rutas:
        rutas = [(str(p), p.read_text(encoding="utf-8"))
                 for p in map(pathlib.Path, sorted(glob.glob(str(ROOT / "examples" / "*.html"))))]
        print(f"(sin argumentos: auditando examples/ de fábrica)")

    total_fallos = 0
    for nombre, html in rutas:
        fallos, avisos = auditar(html, clase_a_familia, packs_conocidos)
        total_fallos += len(fallos)
        print(f"\n== {nombre}")
        for f in fallos:
            print(f"  ✗ FALLO  {f}")
        for a in avisos:
            print(f"  ! aviso  {a}")
        if not fallos and not avisos:
            print("  ✓ limpia: clases, packs, manifiesto y estructura OK")
        print(f"  → {len(fallos)} fallos · {len(avisos)} avisos")

    print(f"\nTOTAL: {total_fallos} fallos")
    return 1 if total_fallos else 0


def selftest():
    """El lint se prueba a sí mismo: una página mala debe salir con fallos."""
    clase_a_familia, packs_conocidos, version = cargar_censo()
    global FAMILIA_PACK
    FAMILIA_PACK = {f: o["pack"] for f, o in
                    json.loads((ROOT / "components.json").read_text(encoding="utf-8"))["objetos"].items()}

    # Ojo: esta página mala enlaza tokens.css pero NO p1-layout.css, para que
    # el lint cace también el pack que falta por enlazar.
    mala = f"""<!DOCTYPE html><html lang="es"><head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@master/tokens.css">
<style>.x {{ background: linear-gradient(90deg, red, blue); color: #ff0000 }}</style>
</head><body><main class="nz-container nz-card nz-boton">Hola</main></body></html>"""

    fallos, avisos = auditar(mala, clase_a_familia, packs_conocidos)
    texto = " | ".join(fallos + avisos)
    esperados = [
        ("clase inventada .nz-card", "nz-card" in texto),
        ("clase inventada .nz-boton", "nz-boton" in texto),
        ("gradiente detectado", "Gradiente" in texto),
        ("color hex a mano", "hex" in texto),
        ("CDN @master avisado", "@master" in texto),
        ("falta pack de nz-container", "Falta por enlazar el pack p1-layout.css" in texto),
        ("body sin nz", 'class="nz"' in texto),
        ("falta atribución", "atribución" in texto),
    ]
    ok = True
    for nombre, cond in esperados:
        print(f"  {'✓' if cond else '✗ FALLO DEL TEST'} {nombre}")
        ok = ok and cond
    print(f"\nSELFTEST: {'OK — el lint caza los 8 defectos' if ok else 'FALLIDO'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
