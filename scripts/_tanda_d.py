# -*- coding: utf-8 -*-
"""Tanda D de ampliacion: p1-layout, p7-overlays, p9-media, p10-commerce (+ demo msg spec14)."""
import json, pathlib, re, sys

MARCA = "ampliado con léxico cerrado (tanda D)"


def css_add(ruta, bloque):
    css = pathlib.Path(ruta).read_text(encoding='utf-8')
    if MARCA in css:
        print(f'{ruta}: ya aplicado')
        return
    pathlib.Path(ruta).write_text(css + bloque, encoding='utf-8')
    print(f'{ruta}: +{bloque.count(chr(10)) - 1} lineas')


def agregar(nfich, demos):
    p = pathlib.Path(f'specs/{int(nfich):02d}.json')
    d = json.loads(p.read_text(encoding='utf-8'))
    vistos = {x['titulo'] for x in d['demos']}
    nuevas = [x for x in demos if x['titulo'] not in vistos]
    d['demos'].extend(nuevas)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'specs/{int(nfich):02d}.json -> +{len(nuevas)} demos (total {len(d["demos"])})')


BLOQUE_P1 = '''

/* ============================================================
   Densidades y estados de layout (ampliado con léxico cerrado (tanda D)) */
.nz-appshell--compact { min-height: auto; }
.nz-appshell--spacious { gap: var(--nz-space-6); }
.nz-bento--compact { gap: var(--nz-space-2); }
.nz-bento--spacious { gap: var(--nz-space-6); }
.nz-grid-12--compact { gap: var(--nz-space-2); }
.nz-grid-12--spacious { gap: var(--nz-space-6); }
.nz-grid-auto--compact { gap: var(--nz-space-2); }
.nz-grid-auto--spacious { gap: var(--nz-space-6); }
.nz-hero-bleed--compact { padding: var(--nz-space-6) var(--nz-gutter); }
.nz-hero-bleed--spacious { padding: var(--nz-space-16) var(--nz-gutter); }
.nz-hero-bleed--brand { background: var(--nz-brand); color: var(--nz-text-invert); }
.nz-collapsible.is-open { border-left: var(--nz-border-w-strong) solid var(--nz-brand); }
.nz-route.is-active { border-left: var(--nz-border-w-strong) solid var(--nz-brand); padding-left: var(--nz-space-4); }
'''

BLOQUE_P7 = '''

/* ============================================================
   Lightbox compacto (ampliado con léxico cerrado (tanda D))   */
.nz-lightbox--compact { width: min(100%, 28rem); aspect-ratio: 4 / 3; }
'''

BLOQUE_P9 = '''

/* ============================================================
   Tonos de fondo, densidad de logos y mapa (ampliado con léxico cerrado (tanda D)) */
.nz-bgimg--brand::before { background: var(--nz-brand); }
.nz-bgimg--accent::before { background: var(--nz-accent); }
.nz-bgimg--brand, .nz-bgimg--accent { color: var(--nz-text-invert); }
.nz-logos--compact { gap: var(--nz-space-3); }
.nz-logos--spacious { gap: var(--nz-space-8); }
.nz-logo-nube--sm .nz-logo-nube__item { min-height: 44px; font-size: var(--nz-text-sm); }
.nz-logo-nube--lg .nz-logo-nube__item { min-height: 72px; padding: var(--nz-space-4); font-size: var(--nz-text-lg); }
.nz-mapa-placeholder--brand { background: var(--nz-brand-soft); }
.nz-mapa-placeholder--brand .nz-mapa-placeholder__pin { background: var(--nz-brand); }
.nz-mapa-placeholder--neutral { background: var(--nz-surface-2); }
'''

BLOQUE_P10 = '''

/* ============================================================
   Estado y densidad de comercio (ampliado con léxico cerrado (tanda D)) */
.nz-cart-item.is-error { opacity: .7; }
.nz-cart-item.is-error .nz-cart-item__name { color: var(--nz-danger); text-decoration: line-through; }
.nz-cart-item--compact { padding: var(--nz-space-2) 0; }
.nz-compare-bar--compact { padding: var(--nz-space-2) var(--nz-space-3); gap: var(--nz-space-2); }
.nz-order--compact { padding: var(--nz-space-3); gap: var(--nz-space-2); }
.nz-pay.is-error { border-color: var(--nz-danger); }
.nz-pay.is-error .nz-pay__icon { background: var(--nz-danger-soft); color: var(--nz-danger); }
.nz-gift-note--sm { padding: var(--nz-space-2) var(--nz-space-3); font-size: var(--nz-text-sm); }
'''

# --- 0) verificacion de tokens ANTES de escribir (inmunidad a tokens fantasma) ---
tokens = pathlib.Path('tokens.css').read_text(encoding='utf-8')
usados = set()
for bloque in (BLOQUE_P1, BLOQUE_P7, BLOQUE_P9, BLOQUE_P10):
    usados.update(re.findall(r'var\((--nz-[a-z0-9-]+)\)', bloque))
faltan = sorted(t for t in usados if t not in tokens)
if faltan:
    print('TOKENS INEXISTENTES:', ', '.join(faltan))
    sys.exit(1)
print(f'tokens verificados: {len(usados)} OK')

# --- 1) CSS ---
css_add('packs/p1-layout.css', BLOQUE_P1)
css_add('packs/p7-overlays.css', BLOQUE_P7)
css_add('packs/p9-media.css', BLOQUE_P9)
css_add('packs/p10-commerce.css', BLOQUE_P10)

# --- 2) markup base clonado de las demos existentes (fiel al sistema) ---
d07 = json.loads(pathlib.Path('specs/07.json').read_text(encoding='utf-8'))
base_lightbox = next(x['markup'] for x in d07['demos'] if 'nz-lightbox' in x['markup'])
markup_lightbox_compacto = base_lightbox.replace('class="nz-lightbox"', 'class="nz-lightbox nz-lightbox--compact"', 1)

d10 = json.loads(pathlib.Path('specs/10.json').read_text(encoding='utf-8'))
base_cart = next(x['markup'] for x in d10['demos'] if 'class="nz-cart-item"' in x['markup'])
cart_error = base_cart.replace('class="nz-cart-item"', 'class="nz-cart-item is-error"', 1)
cart_error = cart_error.replace('× 2 · envío en 24 h', 'sin stock')
cart_compacto = base_cart.replace('class="nz-cart-item"', 'class="nz-cart-item nz-cart-item--compact"', 1)

base_pay = next(x['markup'] for x in d10['demos'] if 'class="nz-pay"' in x['markup'])
pay_error = base_pay.replace('class="nz-pay"', 'class="nz-pay is-error"', 1).replace('Caduca 04/28', 'Pago rechazado')

base_cbar = next((x['markup'] for x in d10['demos'] if 'nz-compare-bar' in x['markup']), None)
markup_cbar = base_cbar.replace('class="nz-compare-bar"', 'class="nz-compare-bar nz-compare-bar--compact"', 1) if base_cbar else None

# --- 3) demos ---
D01 = [
    {
        'titulo': 'Densidades de shell y rejilla',
        'tag': '.nz-appshell--compact/--spacious · .nz-bento--compact/--spacious · .nz-grid-12--compact/--spacious · .nz-grid-auto--compact/--spacious',
        'markup': '<div class="nz-stack nz-stack--sm"><div class="nz-appshell nz-appshell--compact"><div class="demo-box">shell compacto</div><div class="demo-box">contenido</div><div class="demo-box">pie</div></div><div class="nz-appshell nz-appshell--spacious"><div class="demo-box">shell espacioso</div><div class="demo-box">contenido</div><div class="demo-box">pie</div></div><div class="nz-bento nz-bento--compact"><div class="demo-box">bento</div><div class="demo-box">compacto</div></div><div class="nz-bento nz-bento--spacious"><div class="demo-box">bento</div><div class="demo-box">espacioso</div></div><div class="nz-grid-12 nz-grid-12--compact"><div class="demo-box">1</div><div class="demo-box">2</div><div class="demo-box">3</div><div class="demo-box">4</div></div><div class="nz-grid-12 nz-grid-12--spacious"><div class="demo-box">1</div><div class="demo-box">2</div><div class="demo-box">3</div><div class="demo-box">4</div></div><div class="nz-grid-auto nz-grid-auto--compact"><div class="demo-box">auto</div><div class="demo-box">compacto</div></div><div class="nz-grid-auto nz-grid-auto--spacious"><div class="demo-box">auto</div><div class="demo-box">espacioso</div></div></div>',
    },
    {
        'titulo': 'Hero: densidad y tono',
        'tag': '.nz-hero-bleed--compact · --spacious · --brand',
        'markup': '<div class="nz-stack nz-stack--sm"><div class="nz-hero-bleed nz-hero-bleed--compact" style="border-radius:var(--nz-radius-md)"><h3 style="font-size:var(--nz-text-md);margin:0">Hero compacto</h3></div><div class="nz-hero-bleed nz-hero-bleed--spacious" style="border-radius:var(--nz-radius-md)"><h3 style="font-size:var(--nz-text-md);margin:0">Hero espacioso</h3></div><div class="nz-hero-bleed nz-hero-bleed--brand" style="border-radius:var(--nz-radius-md)"><h3 style="font-size:var(--nz-text-lg);margin:0">Hero de marca</h3><p style="margin:var(--nz-space-1) 0 0">Fondo azul sólido, texto invertido.</p></div></div>',
    },
    {
        'titulo': 'Panel abierto y ruta activa',
        'tag': '.nz-collapsible.is-open · .nz-route.is-active',
        'markup': '<div class="nz-stack nz-stack--sm"><div class="nz-collapsible is-open"><details open><summary style="cursor:pointer">Panel abierto (is-open)</summary><p style="font-size:var(--nz-text-sm);color:var(--nz-text-soft);margin-top:var(--nz-space-2)">El borde azul marca el estado abierto; el atributo hidden lo pliega.</p></details></div><div class="nz-route is-active"><div class="demo-box">ruta activa</div><div class="nz-route__outlet">outlet</div></div></div>',
    },
]

D07 = [
    {
        'titulo': 'Lightbox compacto',
        'tag': '.nz-lightbox--compact',
        'markup': markup_lightbox_compacto,
    },
]

D09 = [
    {
        'titulo': 'Fondo con tinte de marca',
        'tag': '.nz-bgimg--brand · --accent',
        'markup': '<div class="nz-cluster"><div class="nz-bgimg nz-bgimg--brand" style="max-width:16rem;min-height:6rem;border-radius:var(--nz-radius-md);background-color:var(--nz-gray-700);display:grid;place-items:center"><span class="nz-media__title">Tinte azul</span></div><div class="nz-bgimg nz-bgimg--accent" style="max-width:16rem;min-height:6rem;border-radius:var(--nz-radius-md);background-color:var(--nz-gray-700);display:grid;place-items:center"><span class="nz-media__title">Tinte naranja</span></div></div>',
    },
    {
        'titulo': 'Logos: densidad y tamaño',
        'tag': '.nz-logos--compact/--spacious · .nz-logo-nube--sm/--lg',
        'markup': '<div class="nz-stack nz-stack--sm"><div class="nz-logos nz-logos--compact"><span class="nz-brand">◆ Marca</span><span class="nz-brand">● Otra</span><span class="nz-brand">▲ Tercera</span></div><div class="nz-logos nz-logos--spacious"><span class="nz-brand">◆ Marca</span><span class="nz-brand">● Otra</span><span class="nz-brand">▲ Tercera</span></div><div class="nz-logo-nube nz-logo-nube--sm"><span class="nz-logo-nube__item nz-brand">◆ Pequeño</span><span class="nz-logo-nube__item nz-logo-nube__item--muted">■ Muted</span></div><div class="nz-logo-nube nz-logo-nube--lg"><span class="nz-logo-nube__item nz-brand">◆ Grande</span><span class="nz-logo-nube__item nz-logo-nube__item--muted">■ Muted</span></div></div>',
    },
    {
        'titulo': 'Mapa con tono',
        'tag': '.nz-mapa-placeholder--brand · --neutral',
        'markup': '<div class="nz-cluster"><div class="nz-mapa-placeholder nz-mapa-placeholder--brand" style="max-width:16rem"><span class="nz-mapa-placeholder__pin"></span><span class="nz-mapa-placeholder__label">Tono marca</span></div><div class="nz-mapa-placeholder nz-mapa-placeholder--neutral" style="max-width:16rem"><span class="nz-mapa-placeholder__pin"></span><span class="nz-mapa-placeholder__label">Tono neutro</span></div></div>',
    },
]

D10 = [
    {
        'titulo': 'Carrito: sin stock y compacto',
        'tag': '.nz-cart-item.is-error · .nz-cart-item--compact',
        'markup': f'<div class="nz-stack nz-stack--sm">{cart_error}{cart_compacto}</div>',
    },
    {
        'titulo': 'Pago rechazado',
        'tag': '.nz-pay.is-error',
        'markup': f'<div class="nz-stack nz-stack--sm">{base_pay}{pay_error}</div>',
    },
    {
        'titulo': 'Pedido compacto y nota corta',
        'tag': '.nz-order--compact · .nz-gift-note--sm',
        'markup': '<div class="nz-stack nz-stack--sm"><article class="nz-order nz-order--compact"><div class="nz-order__head"><span class="nz-order__id">#A7-10431</span><span class="nz-order__status">Enviado</span></div><div class="nz-order__foot"><span>Total</span><span class="nz-order__total">48 €</span></div></article><div class="nz-gift-note nz-gift-note--sm"><span class="nz-gift-note__label">Es un regalo</span><span class="nz-gift-note__body">Nota breve para la caja.</span></div></div>',
    },
]
if markup_cbar:
    D10.append({'titulo': 'Barra de comparación compacta', 'tag': '.nz-compare-bar--compact', 'markup': markup_cbar})

D14 = [
    {
        'titulo': 'Mensaje neutro y de éxito',
        'tag': '.nz-msg--neutral · --success',
        'markup': '<div class="nz-stack nz-stack--sm"><div class="nz-msg nz-msg--neutral"><div class="nz-msg__body"><div class="nz-msg__bubble"><span class="nz-msg__text">Mensaje neutro del sistema.</span></div></div></div><div class="nz-msg nz-msg--success"><div class="nz-msg__body"><div class="nz-msg__bubble"><span class="nz-msg__text">Pago aceptado: tu pedido sale hoy.</span></div></div></div></div>',
    },
]

agregar(1, D01)
agregar(7, D07)
agregar(9, D09)
agregar(10, D10)
agregar(14, D14)

# --- 4) verificacion JSON ---
for n in (1, 7, 9, 10, 14):
    json.load(open(f'specs/{n:02d}.json', encoding='utf-8'))
print('TANDA D COMPLETA — JSON válidos')
