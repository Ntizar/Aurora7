# -*- coding: utf-8 -*-
"""Extrae specs/NN.json desde las páginas de catálogo ya existentes.

A partir de aquí la fuente de verdad de las demos son los JSON de specs/,
no el código Python del generador. Así el generador es tonto y los datos
viven en un formato declarativo que cualquiera puede editar.

Uso: python scripts/extraer-specs.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAG = ROOT / "paginas"
SPECS = ROOT / "specs"

META = {
    1: ("Layout y estructura", "p1-layout.css", "01-layout.html"),
    2: ("Navegación", "p2-navigation.css", "02-navigation.html"),
    3: ("Tipografía", "p3-typography.css", "03-typography.html"),
    4: ("Acciones y botones", "p4-actions.css", "04-actions.html"),
    5: ("Formularios e inputs", "p5-forms.css", "05-forms.html"),
    6: ("Feedback y estados", "p6-feedback.css", "06-feedback.html"),
    7: ("Overlays y diálogo", "p7-overlays.css", "07-overlays.html"),
    8: ("Datos, tablas y listas", "p8-data.css", "08-data.html"),
    9: ("Media e iconografía", "p9-media.css", "09-media.html"),
    10: ("Comercio y producto", "p10-commerce.css", "10-commerce.html"),
    11: ("Social y marketing", "p11-social.css", "11-social.html"),
    12: ("Accesibilidad y sistema", "p12-system.css", "12-system.html"),
}


def bloque_stage(html_txt, pos):
    """Devuelve el markup interno del .cat-stage que empieza en pos (tras su >)."""
    prof = 1
    j = pos
    while prof > 0 and j < len(html_txt):
        na = html_txt.find("<div", j)
        nc = html_txt.find("</div>", j)
        if nc == -1:
            break
        if na != -1 and na < nc:
            prof += 1
            j = na + 4
        else:
            prof -= 1
            j = nc + 6
    return html_txt[pos:j - 6]


def extrae(html_txt):
    demos = []
    for m in re.finditer(r'<section class="cat-demo[^"]*">(.*?)</section>', html_txt, re.S):
        sec = m.group(1)
        t = re.search(r'cat-demo__name">(.*?)</span>', sec, re.S)
        g = re.search(r'cat-demo__tag">(.*?)</span>', sec, re.S)
        st = re.search(r'<div class="cat-stage[^"]*">', sec)
        if not (t and g and st):
            continue
        markup = bloque_stage(sec, st.end()).strip()
        demos.append({
            "titulo": t.group(1).strip(),
            "tag": g.group(1).strip(),
            "markup": markup,
        })
    return demos


def main():
    SPECS.mkdir(exist_ok=True)
    total = 0
    for num, (nombre, pack, fichero) in META.items():
        f = PAG / fichero
        if not f.exists():
            print("AVISO: falta", fichero)
            continue
        h = f.read_text(encoding="utf-8")
        desc = ""
        d = re.search(r'<p class="cat-pagehead__over">.*?</p>\s*<h1>.*?</h1>\s*<p>(.*?)</p>', h, re.S)
        if d:
            desc = d.group(1).strip()
        demos = extrae(h)
        datos = {
            "cat": num,
            "nombre": nombre,
            "desc": desc,
            "pack": pack,
            "fichero": fichero,
            "demos": demos,
        }
        (SPECS / f"{num:02d}.json").write_text(
            json.dumps(datos, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(demos)
        print(f"specs/{num:02d}.json  {len(demos):>3} demos  {nombre}")
    print("TOTAL demos extraídas:", total)


if __name__ == "__main__":
    main()
