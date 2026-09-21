# -*- coding: utf-8 -*-
"""Tanda C de ampliacion: p13-charts, p8-data (CSS + demos en specs)."""
import json, pathlib


def agregar(nfich, demos):
    p = pathlib.Path(f'specs/{int(nfich):02d}.json')
    d = json.loads(p.read_text(encoding='utf-8'))
    vistos = {x['titulo'] for x in d['demos']}
    nuevas = [x for x in demos if x['titulo'] not in vistos]
    if not nuevas:
        print(f'specs/{p.name}: nada nuevo')
        return
    d['demos'].extend(nuevas)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'specs/{p.name} -> +{len(nuevas)} demos (total {len(d["demos"])})')


def css_add(ruta, bloque, marca):
    css = pathlib.Path(ruta).read_text(encoding='utf-8')
    if marca in css:
        print(f'{ruta}: ya aplicado')
        return
    pathlib.Path(ruta).write_text(css + bloque, encoding='utf-8')
    print(f'{ruta}: +{bloque.count(chr(10))-1} lineas')


# ============ p8-data.css ============
css_add('packs/p8-data.css', '''

/* ============================================================
   Estados de arbol, densidad y tono de registros (lexico)      */
.nz-arbol__node.is-selected > .nz-arbol__toggle,
.nz-arbol__leaf.is-selected { background: var(--nz-brand-soft); color: var(--nz-brand); }
.nz-arbol__leaf.is-error { color: var(--nz-danger); }
.nz-arbol__leaf.is-done { color: var(--nz-success); }
.nz-records--dense { gap: var(--nz-space-1); }
.nz-records--spacious { gap: var(--nz-space-4); }
.nz-record--success { box-shadow: inset 3px 0 0 var(--nz-success), var(--nz-shadow-sm); }
.nz-record--warning { box-shadow: inset 3px 0 0 var(--nz-warning), var(--nz-shadow-sm); }
.nz-record.is-selected { box-shadow: 0 0 0 2px var(--nz-brand), var(--nz-shadow-sm); }
''', 'nz-arbol__node.is-selected')

# ============ p13-charts.css ============
css_add('packs/p13-charts.css', '''

/* ============================================================
   Tono semantico de series (lexico cerrado)                    */
.nz-chart-line--brand { border-color: var(--nz-brand); }
.nz-chart-line--accent { border-color: var(--nz-accent); }
.nz-chart-line--success { border-color: var(--nz-success); }
.nz-chart-line--danger { border-color: var(--nz-danger); }
.nz-chart-mini__bar { flex: 1 1 auto; min-width: 3px; background: var(--nz-accent); border-radius: 1px 1px 0 0; }
.nz-chart-mini__bar--brand { background: var(--nz-brand); }
.nz-chart-mini__bar--success { background: var(--nz-success); }
.nz-chart-mini__bar--danger { background: var(--nz-danger); }
.nz-chart-mini__bar--warning { background: var(--nz-warning); }
''', 'nz-chart-line--brand')

# ============ Demos ============
barra = lambda h, v, cls='': (f'<div class="nz-chart-bar__col{cls}"><span class="nz-chart-bar__value">{v}</span>'
                              f'<span class="nz-chart-bar__bar" style="height:{h}"></span>'
                              f'<span class="nz-chart-bar__label">L</span></div>')
mini = lambda cls='': f'<span class="nz-chart-mini__bar{cls}" style="height:40%"></span>'

agregar(8, [
    {"titulo": "Arbol · estados de nodo y hoja", "tag": ".nz-arbol__node.is-selected / __leaf.is-error",
     "markup": ('<ul class="nz-arbol"><li class="nz-arbol__node is-selected"><span class="nz-arbol__toggle">Proyecto</span>'
                '<ul class="nz-arbol__group"><li><a class="nz-arbol__leaf" href="#">docs</a></li>'
                '<li><a class="nz-arbol__leaf is-done" href="#">CHANGELOG.md</a></li>'
                '<li><a class="nz-arbol__leaf is-error" href="#">secreto.env</a></li></ul></li></ul>')},
    {"titulo": "Registros · densidad", "tag": ".nz-records--dense / --spacious",
     "markup": ('<div class="nz-records nz-records--dense"><div class="nz-record">Densa · fila 1</div>'
                '<div class="nz-record">Densa · fila 2</div></div>'
                '<div class="nz-records nz-records--spacious" style="margin-top:1rem"><div class="nz-record">Amplia · fila 1</div>'
                '<div class="nz-record">Amplia · fila 2</div></div>')},
    {"titulo": "Registro · tono y seleccion", "tag": ".nz-record--success / --warning / .is-selected",
     "markup": ('<div class="nz-records"><div class="nz-record nz-record--success">Pago confirmado</div>'
                '<div class="nz-record nz-record--warning">Stock bajo: 3 unidades</div>'
                '<div class="nz-record is-selected">Factura 2026-114 seleccionada</div></div>')},
])

agregar(13, [
    {"titulo": "Linea · tono de serie", "tag": ".nz-chart-line--brand / --success / --danger",
     "markup": ('<div class="nz-chart nz-chart-line nz-chart-line--brand"><i style="left:10%;top:60%"></i><i style="left:50%;top:30%"></i><i style="left:90%;top:45%"></i></div>'
                '<div class="nz-chart nz-chart-line nz-chart-line--success"><i style="left:10%;top:70%"></i><i style="left:50%;top:50%"></i><i style="left:90%;top:20%"></i></div>'
                '<div class="nz-chart nz-chart-line nz-chart-line--danger"><i style="left:10%;top:20%"></i><i style="left:50%;top:40%"></i><i style="left:90%;top:80%"></i></div>')},
    {"titulo": "Minigráfico · tono", "tag": ".nz-chart-mini__bar--brand / --success / --warning / --danger",
     "markup": ('<div class="nz-chart-mini">' + mini() + mini() + mini(" nz-chart-mini__bar--brand") + mini(" nz-chart-mini__bar--brand") + '</div>'
                '<div class="nz-chart-mini">' + mini() + mini(" nz-chart-mini__bar--success") + mini(" nz-chart-mini__bar--success") + '</div>'
                '<div class="nz-chart-mini">' + mini() + mini(" nz-chart-mini__bar--warning") + mini(" nz-chart-mini__bar--warning") + '</div>'
                '<div class="nz-chart-mini">' + mini() + mini(" nz-chart-mini__bar--danger") + mini(" nz-chart-mini__bar--danger") + '</div>')},
])

print('TANDA C COMPLETA')
