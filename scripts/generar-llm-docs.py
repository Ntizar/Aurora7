# -*- coding: utf-8 -*-
"""Genera components.json y LLM.md a partir de los packs y los specs.

La idea (patrón «design system infalible para LLMs»): un agente NO debe leer
250 KB de CSS para usar Aurora 7. Con estos dos archivos sabe qué packs cargar,
qué clases existen de verdad y cuáles son sus modificadores y partes, sin
inventarse nada.

  · components.json → spec machine-readable completo (todas las clases reales)
  · LLM.md          → guía de decisión en prosa, ~2 KB, para meter en contexto

Uso: python scripts/generar-llm-docs.py
"""
import json
import pathlib
import sys
from importlib import import_module

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
bc = import_module("build-catalog")

ROOT = bc.ROOT
VERSION = "7.1.0"


def main():
    packs, censo_cat, total_clases, total_bases = bc.censo()
    specs = {s["cat"]: s for s in bc.carga_specs()}
    total_demos = sum(len(s["demos"]) for s in specs.values())

    objetos = {}
    for cat, datos in sorted(censo_cat.items()):
        spec = specs.get(cat, {})
        for clase in sorted(datos["clases"]):
            base = bc.base_de(clase)
            o = objetos.setdefault(base, {
                "pack": datos["pack"], "categoria": cat,
                "demo": f"paginas/{spec.get('fichero', '')}",
                "clases": [], "modificadores": [], "partes": [],
            })
            o["clases"].append(clase)
            resto = clase[len(base):]
            if "--" in resto:
                o["modificadores"].append(resto.split("--", 1)[1])
            if "__" in clase:
                o["partes"].append(clase.split("__", 1)[1])

    datos = {
        "name": "Aurora 7",
        "version": VERSION,
        "type": "css-only design system",
        "namespace": ".nz-",
        "tokens": "tokens.css",
        "cdn": "https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@master/",
        "manifiesto": {
            "gradientes": 0,
            "glass": 0,
            "coloresAMano": 0,
            "importantPermitidoEn": [".nz-visually-hidden", ".nz-print-hide"],
            "tema": "data-nz-theme=\"light\" | \"dark\" en el elemento <html>",
            "cuerpo": "class=\"nz\"",
            "mobileFirst": True,
            "objetivoTactil": "44px",
        },
        "resumen": {
            "objetos": total_clases,
            "familias": total_bases,
            "categorias": len(censo_cat),
            "demos": total_demos,
        },
        "packs": {
            datos_pack["pack"]: {
                "categoria": cat,
                "nombre": specs[cat]["nombre"] if cat in specs else "",
                "descripcion": specs[cat]["desc"] if cat in specs else "",
                "objetos": len(datos_pack["clases"]),
                "familias": len(datos_pack["bases"]),
                "demos": len(specs[cat]["demos"]) if cat in specs else 0,
                "pagina": f"paginas/{specs[cat]['fichero']}" if cat in specs else "",
            }
            for cat, datos_pack in sorted(censo_cat.items())
        },
        "lexico": {
            "tamano": ["--2xs", "--xs", "--sm", "--lg", "--xl"],
            "tono": ["--brand", "--accent", "--success", "--warning", "--danger", "--info", "--neutral"],
            "enfasis": ["--solid", "--soft", "--outline", "--ghost"],
            "disposicion": ["--vertical", "--horizontal", "--inline", "--compact",
                            "--spacious", "--center", "--between", "--end"],
            "forma": ["--square", "--rounded", "--pill"],
            "elevacion": ["--flat", "--raised"],
            "estado": [".is-active", ".is-disabled", ".is-loading", ".is-done",
                       ".is-error", ".is-empty", ".is-selected",
                       "[aria-current]", "[aria-selected]", "[aria-expanded]"],
        },
        "objetos": objetos,
    }
    (ROOT / "components.json").write_text(
        json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---------- LLM.md ----------
    filas = "\n".join(
        f"| {v['categoria']:02d} · {v['nombre']} | `{k}` | "
        f"{', '.join(f'`{b}`' for b in sorted(censo_cat[v['categoria']]['bases'])[:4])}"
        f"{'…' if len(censo_cat[v['categoria']]['bases']) > 4 else ''} |"
        for k, v in sorted(datos["packs"].items(), key=lambda kv: kv[1]["categoria"]))

    llm = f"""# Aurora 7 — guía de decisión para agentes

Design system CSS puro, sin dependencias ni build. {total_clases} objetos en {len(censo_cat)} categorías.
**No pegues el CSS en el prompt**: enlaza por CDN y usa las clases de esta guía.

## 1. Mínimo obligatorio

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@master/tokens.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@master/packs/all.css">
<html lang="es" data-nz-theme="light">
<body class="nz">
```

## 2. ¿Qué pack necesito?

| Categoría | Pack | Objetos clave (API completa en `components.json`) |
|---|---|---|
{filas}

Carga solo los packs que uses (producción) o `packs/all.css` (prototipo).

## 3. Necesito X → uso Y

| Necesito | Clases |
|---|---|
| Botón | `.nz-btn` + `.nz-btn--primary/--accent/--ghost/--soft/--outline/--danger` + `--sm/--lg/--icon` |
| Tarjeta | `.nz-card`, `.nz-article`, `.nz-chart` |
| Formulario | `.nz-field` > `.nz-field__label` + `.nz-input` + `.nz-field__help` |
| Elegir una opción | `.nz-checkbox`, `.nz-radio`, `.nz-switch`, `.nz-segmented` |
| Aviso | `.nz-alert--info/--success/--warning/--danger`, `.nz-callout` |
| Etiqueta de estado | `.nz-badge--brand/--success/--danger/--warning`, `.nz-lbl` |
| Tabla | `.nz-table-wrap` > `.nz-table` (+ `--striped`, `__num`, `__status`) |
| Cifra destacada | `.nz-kpi` (`__label/__value/__delta`), `.nz-chart-stat` |
| Gráfico | `.nz-chart-bar`, `.nz-chart-line`, `.nz-chart-donut`, `.nz-chart-gauge`, `.nz-heatmap` |
| Diálogo | `.nz-modal` (checkbox + label, sin JS), `.nz-drawer`, `.nz-sheet` |
| Pantalla completa | `.nz-appshell`, `.nz-with-sidebar`, `.nz-split`, `.nz-dash-grid` |
| Chat / IA | `.nz-chat`, `.nz-msg`, `.nz-prompt`, `.nz-toolcall`, `.nz-taskplan` |
| Escritorio / app | `.nz-window`, `.nz-appnav`, `.nz-kanban`, `.nz-editor`, `.nz-terminal` |

## 4. Léxico de modificadores (igual en los 15 packs)

- **Tamaño**: `--2xs --xs --sm --lg --xl`
- **Tono**: `--brand --accent --success --warning --danger --info --neutral`
- **Énfasis**: `--solid --soft --outline --ghost`
- **Disposición**: `--vertical --horizontal --inline --compact --spacious --center --between --end`
- **Forma**: `--square --rounded --pill` · **Elevación**: `--flat --raised`
- **Estado**: `.is-active .is-disabled .is-loading .is-done .is-error .is-selected` o `[aria-current] [aria-selected]`

## 5. Personalizar la marca

```css
:root {{
  --nz-brand: #2563eb;          /* color primario */
  --nz-accent: #f97316;         /* acento, nunca fundido con el primario */
  --nz-font: "Inter", system-ui, sans-serif;
  --nz-radius-md: 10px;
  --nz-container-max: 72rem;
}}
```

## 6. Anti-patrones (NO lo hagas)

- ❌ Pegar el CSS de los packs en el prompt (250 KB ≈ 60.000 tokens). Enlaza por CDN.
- ❌ Inventar clases (`nz-gradient-text`, `nz-btn--glass-liquid-brand`): no existen aquí.
- ❌ Escribir colores a mano (`#2563eb`, `rgb(...)`): usa tokens `var(--nz-*)`.
- ❌ Gradientes, `backdrop-filter` o `!important`: prohibidos por el manifiesto y la CI los detecta.
- ❌ Clases globales sin `.nz-`: romperías la convivencia con otros frameworks.
- ❌ Desktop-first: el sistema es mobile-first (base 1 columna, `min-width` para crecer).

## 7. Verificar antes de entregar

```bash
python scripts/validar-css.py     # manifiesto + cobertura
```

Docs hermanas: `AGENTS.md` (reglas duras del repo), `components.json` (API completa
machine-readable), `paginas/` (catálogo con una demo viva por objeto), `README.md`.

Hecho con ❤️ por David Antizar
"""
    (ROOT / "LLM.md").write_text(llm, encoding="utf-8")
    print(f"components.json → {len(objetos)} familias, {total_clases} clases")
    print(f"LLM.md → {len(llm)} bytes")


if __name__ == "__main__":
    main()
