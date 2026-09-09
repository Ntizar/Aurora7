# -*- coding: utf-8 -*-
"""Generador del catálogo Aurora 7 · páginas 02-12.
Sigue el patrón de 01-layout.html. Solo usa clases .nz-* reales
definidas en cada pack. Sin slop: cada demo es markup real del objeto."""
import pathlib, html

ROOT = pathlib.Path(r"C:\Users\d_ant\Projects\Aurora-7")
PAG = ROOT / "paginas"

# ---------------------------------------------------------------
# DATOS: categorias -> lista de demos.
# Cada demo: (titulo, tag, markup_html). markup usa clases reales.
# Num se asigna automáticamente en grupos 1..N.
# ---------------------------------------------------------------
NAV = [
    (1,  "01 Layout", "01-layout.html", "p1-layout.css"),
    (2,  "02 Navegación", "02-navigation.html", "p2-navigation.css"),
    (3,  "03 Tipografía", "03-typography.html", "p3-typography.css"),
    (4,  "04 Acciones", "04-actions.html", "p4-actions.css"),
    (5,  "05 Formularios", "05-forms.html", "p5-forms.css"),
    (6,  "06 Feedback", "06-feedback.html", "p6-feedback.css"),
    (7,  "07 Overlays", "07-overlays.html", "p7-overlays.css"),
    (8,  "08 Datos", "08-data.html", "p8-data.css"),
    (9,  "09 Media", "09-media.html", "p9-media.css"),
    (10, "10 Comercio", "10-commerce.html", "p10-commerce.css"),
    (11, "11 Social", "11-social.html", "p11-social.css"),
    (12, "12 Sistema", "12-system.html", "p12-system.css"),
]

DEMOS = {
 2: [
  ("Navbar superior", ".nz-navbar · __brand/__link",
   '<div class="nz-navbar"><span class="nz-navbar__brand"><i></i>Marca</span><span class="nz-navbar__links"><a class="nz-navbar__link" aria-current="page">Inicio</a><a class="nz-navbar__link">Docs</a><a class="nz-navbar__link">Blog</a></span></div>'),
  ("Menú con hamburguesa (sin JS)", ".nz-menu > input:checked ~ .nz-menu__drop",
   '<div class="nz-menu"><input type="checkbox" id="m1" hidden><label class="nz-menu__btn" for="m1">☰</label><div class="nz-menu__drop"><a class="nz-menu__item" aria-current="page">Inicio</a><a class="nz-menu__item">Perfil</a><a class="nz-menu__item">Ajustes</a></div></div>'),
  ("Sidebar de navegación", ".nz-sidebar · __link[aria-current]",
   '<div class="nz-sidebar"><span class="nz-sidebar__heading">Menú</span><a class="nz-sidebar__link" aria-current="page">Panel</a><a class="nz-sidebar__link">Informes</a><a class="nz-sidebar__link">Datos</a></div>'),
  ("Tabs", ".nz-tabs__tab[aria-selected]",
   '<div class="nz-tabs"><button class="nz-tabs__tab" aria-selected="true">Resumen</button><button class="nz-tabs__tab">Detalle</button><button class="nz-tabs__tab">Historial</button></div>'),
  ("Breadcrumbs", ".nz-breadcrumb__sep",
   '<nav class="nz-breadcrumb" aria-label="miga"><a>Inicio</a><span class="nz-breadcrumb__sep">/</span><a>Docs</a><span class="nz-breadcrumb__sep">/</span><span aria-current="page">Instalación</span></nav>'),
  ("Paginación", ".nz-pagination [aria-current]",
   '<nav class="nz-pagination" aria-label="páginas"><a>‹</a><a aria-current="page">1</a><a>2</a><a>3</a><span class="nz-pagination__ellipsis">…</span><a>›</a></nav>'),
  ("Índice de contenidos (TOC)", ".nz-toc a[aria-current=location]",
   '<nav class="nz-toc"><span class="nz-toc__title">En esta página</span><a href="#" aria-current="location">Introducción</a><a href="#" class="nz-toc--level2">- Inicio rápido</a><a href="#">Componentes</a></nav>'),
  ("Dropdown select", ".nz-dropdown > input:checked ~ .nz-dropdown__list",
   '<div class="nz-dropdown"><input type="checkbox" id="d1" hidden><label class="nz-dropdown__btn" for="d1">País</label><div class="nz-dropdown__list"><a class="nz-menu__item">España</a><a class="nz-menu__item">Francia</a><a class="nz-menu__item">Italia</a></div></div>'),
  ("Nav footer", ".nz-navfooter__col",
   '<div class="nz-navfooter"><div class="nz-navfooter__col"><span class="nz-navfooter__title">Producto</span><a>Docs</a><a>Guías</a></div><div class="nz-navfooter__col"><span class="nz-navfooter__title">Compañía</span><a>Blog</a><a>Contacto</a></div></div>'),
  ("Stepper de proceso", ".nz-stepper__step.is-active/.is-done",
   '<div class="nz-stepper"><div class="nz-stepper__step is-done"><span class="nz-stepper__num">1</span>Cuenta</div><div class="nz-stepper__step is-active"><span class="nz-stepper__num">2</span>Pago</div><div class="nz-stepper__step"><span class="nz-stepper__num">3</span>Listo</div></div>'),
  ("Pill tabs (móvil)", ".nz-tabs--pill .nz-tabs__tab",
   '<div class="nz-tabs nz-tabs--pill"><button class="nz-tabs__tab" aria-selected="true">Hoy</button><button class="nz-tabs__tab">Semana</button><button class="nz-tabs__tab">Mes</button></div>'),
 ],
 3: [
  ("Escala de títulos", ".nz-h1 … .nz-h6",
   '<div><p class="nz-display">Display 4XL</p><p class="nz-h1">H1 3XL</p><p class="nz-h2">H2 2XL</p><p class="nz-h3">H3 XL</p><p class="nz-h4">H4 LG</p><p class="nz-h5">H5 base</p><p class="nz-h6">H6 · caps</p></div>'),
  ("Eyebrow", ".nz-eyebrow",
   '<p class="nz-eyebrow">Design System</p>'),
  ("Lead y cuerpo", ".nz-lead · .nz-text--muted",
   '<p class="nz-lead">Párrafo introductorio, algo mayor y más blando.</p><p class="nz-text--muted">Texto secundario en gris.</p><p class="nz-text--faint">Texto tenue para metadatos.</p>'),
  ("Prose", ".nz-prose",
   '<div class="nz-prose"><p>Párrafo de prosa con cuerpo normal y <strong>énfasis fuerte</strong> y enlaces <a class="nz-prose a">destacados</a>.</p></div>'),
  ("Listas", ".nz-list · _check · _numeric",
   '<div><ul class="nz-list"><li class="nz-list__item">Item con punto azul</li><li class="nz-list__item">Item 2</li></ul><ul class="nz-list nz-list--check"><li class="nz-list__item">Validado</li></ul><ol class="nz-list nz-list--numeric"><li class="nz-list__item">Paso 1</li><li class="nz-list__item">Paso 2</li></ol></div>'),
  ("Blockquote", ".nz-blockquote",
   '<blockquote class="nz-blockquote"><p>“El sistema se entiende por sus límites, no por su cantidad.”</p><footer>David Antizar</footer></blockquote>'),
  ("Código", ".nz-code · .nz-code--block · .nz-kbd",
   '<div><code class="nz-code">const nz = true</code><pre class="nz-code--block">// bloque\necho "hola";</pre><kbd class="nz-kbd">Ctrl+K</kbd></div>'),
  ("Etiquetas", ".nz-lbl--brand/accent/success/danger",
   '<div><span class="nz-lbl">Nuevo</span><span class="nz-lbl nz-lbl--brand"><i></i>Brand</span><span class="nz-lbl nz-lbl--accent"><i></i>Accent</span><span class="nz-lbl nz-lbl--success">OK</span><span class="nz-lbl nz-lbl--danger">Err</span></div>'),
  ("Cifras", ".nz-num--stat/--brand",
   '<p><span class="nz-num nz-num--stat">12 480</span> <span class="nz-num nz-num--brand">+8,2 %</span></p>'),
  ("Enlace con vida", ".nz-link::after",
   '<a class="nz-link" href="#">Ver documentación</a> <a class="nz-link nz-link--accent nz-link--arrow" href="#">Siguiente</a>'),
 ],
 4: [
  ("Botones primarios de variante", ".nz-btn--primary/_accent",
   '<div style="display:flex;gap:.5rem;flex-wrap:wrap"><button class="nz-btn nz-btn--primary">Primario</button><button class="nz-btn nz-btn--accent">Acento</button></div>'),
  ("Botones de estilo", ".nz-btn--ghost/_soft/_danger",
   '<div style="display:flex;gap:.5rem;flex-wrap:wrap"><button class="nz-btn nz-btn--ghost">Fantasma</button><button class="nz-btn nz-btn--soft">Suave</button><button class="nz-btn nz-btn--danger">Peligro</button></div>'),
  ("Tamaños", ".nz-btn--sm/_lg/_block/_icon",
   '<div style="display:flex;gap:.5rem;flex-wrap:wrap;align-items:center"><button class="nz-btn nz-btn--primary nz-btn--sm">Pequeño</button><button class="nz-btn nz-btn--primary">Base</button><button class="nz-btn nz-btn--primary nz-btn--lg">Grande</button><button class="nz-btn nz-btn--primary nz-btn--icon" aria-label="añadir">＋</button></div>'),
  ("Grupo de botones", ".nz-btn-group--joined",
   '<div class="nz-btn-group nz-btn-group--joined"><button class="nz-btn nz-btn--ghost">Izq</button><button class="nz-btn nz-btn--ghost">Med</button><button class="nz-btn nz-btn--ghost">Der</button></div>'),
  ("Selector segmentado", ".nz-segmented [aria-selected=true]",
   '<div class="nz-segmented"><button aria-selected="true">Lista</button><button aria-selected="false">Grid</button><button aria-selected="false">Mapa</button></div>'),
  ("FAB", ".nz-fab",
   '<button class="nz-fab" aria-label="nuevo">＋</button>'),
  ("Estado de carga", ".nz-btn.is-busy · .nz-spin",
   '<button class="nz-btn nz-btn--primary is-busy"><span class="nz-spin"></span> Guardando…</button>'),
  ("Link-acción", ".nz-cta__arrow",
   '<a class="nz-cta" href="#">Explorar <span class="nz-cta__arrow">→</span></a> <a class="nz-cta nz-cta--accent" href="#">Comprar</a>'),
  ("Toolbar", ".nz-toolbar__spacer",
   '<div class="nz-toolbar"><button class="nz-btn nz-btn--ghost">Abrir</button><button class="nz-btn nz-btn--ghost">Editar</button><span class="nz-toolbar__spacer"></span><button class="nz-btn nz-btn--primary">Exportar</button></div>'),
 ],
 5: [
  ("Campo con etiqueta y ayuda", ".nz-field",
   '<label class="nz-field"><span class="nz-field__label nz-field__label--req">Correo</span><input class="nz-input" type="email" placeholder="tu@correo.es"><span class="nz-field__help">Nunca lo compartimos.</span></label>'),
  ("Inputs", ".nz-input · :focus",
   '<input class="nz-input" placeholder="Texto" style="max-width:16rem"><input class="nz-input nz-input--error" placeholder="Con error" style="max-width:16rem">'),
  ("Textarea", ".nz-textarea",
   '<textarea class="nz-textarea" placeholder="Descripción…" style="max-width:20rem"></textarea>'),
  ("Select", ".nz-select",
   '<select class="nz-select" style="max-width:14rem"><option>Opción A</option><option>Opción B</option></select>'),
  ("Checkbox", ".nz-checkbox__box",
   '<label class="nz-checkbox"><input type="checkbox" checked><span class="nz-checkbox__box"></span>Acepto los términos</label>'),
  ("Radio", ".nz-radio__dot",
   '<label class="nz-radio"><input type="radio" name="r" checked><span class="nz-radio__dot"></span>Estándar</label>'),
  ("Switch", ".nz-switch__thumb",
   '<label class="nz-switch"><input type="checkbox" checked><span class="nz-switch__track"><span class="nz-switch__thumb"></span></span><span class="nz-switch__label">Notificaciones</span></label>'),
  ("Range", ".nz-range",
   '<input class="nz-range" type="range" min="0" max="100" value="60" style="max-width:16rem">'),
  ("Grupo con addon", ".nz-inputgroup__addon",
   '<div class="nz-inputgroup" style="max-width:16rem"><span class="nz-inputgroup__addon">€</span><input class="nz-input" placeholder="0,00"></div>'),
  ("Búsqueda", ".nz-search__icon",
   '<div class="nz-search" style="max-width:16rem"><span class="nz-search__icon">⌕</span><input class="nz-input" placeholder="Buscar…"></div>'),
  ("Cantidad", ".nz-qty",
   '<div class="nz-qty"><button aria-label="menos">−</button><input value="2" aria-label="cantidad"><button aria-label="más">+</button></div>'),
 ],
 6: [
  ("Alertas", ".nz-alert--info/success/warning/danger",
   '<div class="nz-alert nz-alert--info"><span class="nz-alert__icon">ℹ</span><div class="nz-alert__body"><span class="nz-alert__title">Información</span><span class="nz-alert__msg">Mensaje informativo.</span></div></div>'),
  ("Alerta de éxito", ".nz-alert--success",
   '<div class="nz-alert nz-alert--success"><span class="nz-alert__icon">✓</span><div class="nz-alert__body"><span class="nz-alert__title">Guardado</span><span class="nz-alert__msg">Los cambios se aplicaron.</span></div></div>'),
  ("Alerta de error", ".nz-alert--danger",
   '<div class="nz-alert nz-alert--danger"><span class="nz-alert__icon">✕</span><div class="nz-alert__body"><span class="nz-alert__title">Error</span><span class="nz-alert__msg">Algo falló.</span></div></div>'),
  ("Callout", ".nz-callout--accent",
   '<div class="nz-callout"><p>Nota: esta regla es importante.</p></div>'),
  ("Badges de estado", ".nz-badge--brand/success/danger/warning",
   '<div><span class="nz-badge nz-badge--brand"><i></i>Brand</span><span class="nz-badge nz-badge--success"><i></i>Activo</span><span class="nz-badge nz-badge--danger"><i></i>Crítico</span><span class="nz-badge nz-badge--warning"><i></i>Pendiente</span></div>'),
  ("Chips", ".nz-chip.is-active",
   '<div style="display:flex;gap:.5rem;flex-wrap:wrap"><button class="nz-chip is-active">Todos ×</button><button class="nz-chip">Agua</button></div>'),
  ("Skeleton", ".nz-skeleton",
   '<div class="nz-skeleton"><div class="nz-skeleton__card"><div class="nz-skeleton__line nz-skeleton__line--title"></div><div class="nz-skeleton__line nz-skeleton__line--wide"></div><div class="nz-skeleton__line"></div><div class="nz-skeleton__line" style="width:65%"></div></div></div>'),
  ("Empty state", ".nz-empty",
   '<div class="nz-empty"><span class="nz-empty__icon">📦</span><p class="nz-empty__title">Sin resultados</p><p class="nz-empty__body">Todavía no hay nada que mostrar.</p><button class="nz-btn nz-btn--primary nz-empty__action">Crear</button></div>'),
  ("Barra de progreso", ".nz-progress__bar",
   '<div class="nz-progress" style="max-width:16rem"><div class="nz-progress__bar" style="width:60%"></div></div>'),
  ("Anillo de progreso", ".nz-ring__fill",
   '<div class="nz-ring" style="width:56px;height:56px"><svg width="56" height="56" viewBox="0 0 56 56"><circle class="nz-ring__track" cx="28" cy="28" r="24" fill="none" stroke-width="6"/><circle class="nz-ring__fill" cx="28" cy="28" r="24" fill="none" stroke-width="6" stroke-dasharray="150.8" stroke-dashoffset="60"/></svg><span class="nz-ring__label">60%</span></div>'),
  ("Status bar", ".nz-statusbar--success",
   '<div class="nz-statusbar"><span>2 de 5 completados</span><span class="nz-statusbar__spacer"></span><span class="nz-statusbar--success">40%</span></div>'),
 ],
 7: [
  ("Modal", ".nz-modal > input:checked ~ .nz-modal__dialog",
   '<label class="nz-btn nz-btn--primary" for="mo1">Abrir modal</label><div class="nz-modal"><input type="checkbox" id="mo1" hidden><label class="nz-modal__scrim" for="mo1"></label><div class="nz-modal__dialog"><div class="nz-modal__head"><h3 class="nz-modal__title">Confirmar</h3><label class="nz-modal__close" for="mo1">✕</label></div><p class="nz-modal__body">¿Estás seguro?</p><div class="nz-modal__foot"><label class="nz-btn nz-btn--ghost" for="mo1">Cancelar</label><label class="nz-btn nz-btn--primary" for="mo1">Sí</label></div></div></div>'),
  ("Drawer lateral", ".nz-drawer__panel--right",
   '<label class="nz-btn nz-btn--primary" for="dr1">Abrir panel</label><div class="nz-drawer"><input type="checkbox" id="dr1" hidden><label class="nz-drawer__scrim" for="dr1"></label><div class="nz-drawer__panel nz-drawer__panel--left"><div class="nz-drawer__head"><span class="nz-drawer__title">Ajustes</span></div><div class="nz-drawer__body"><label class="nz-switch"><input type="checkbox"><span class="nz-switch__track"><span class="nz-switch__thumb"></span></span><span class="nz-switch__label">Modo oscuro</span></label></div></div></div>'),
  ("Bottom-sheet", ".nz-sheet__panel",
   '<label class="nz-btn nz-btn--primary" for="sh1">Abrir sheet</label><div class="nz-sheet"><input type="checkbox" id="sh1" hidden><label class="nz-sheet__scrim" for="sh1"></label><div class="nz-sheet__panel"><div class="nz-sheet__grab"></div><div class="nz-sheet__head"><span class="nz-sheet__title">Compartir</span></div><p class="nz-sheet__body">Elige una opción.</p></div></div>'),
  ("Popover", ".nz-popover > input:checked ~ .nz-popover__body",
   '<div class="nz-popover"><input type="checkbox" id="po1" hidden><label class="nz-btn nz-btn--ghost" for="po1">Más ▼</label><div class="nz-popover__body"><span class="nz-popover__arrow"></span><a class="nz-menu__item">Editar</a><a class="nz-menu__item">Duplicar</a></div></div>'),
  ("Tooltip", ".nz-tip__body",
   '<span class="nz-tip"><button class="nz-btn nz-btn--ghost" tabindex="0">Hover</button><span class="nz-tip__body">Soy un tooltip</span></span>'),
  ("Menú contextual", ".nz-menu-pop__list",
   '<div class="nz-menu-pop"><input type="checkbox" id="mc1" hidden><label class="nz-btn nz-btn--ghost" for="mc1">⋯</label><div class="nz-menu-pop__list"><button class="nz-menu-pop__item">Abrir</button><button class="nz-menu-pop__item">Copiar</button><div class="nz-menu-pop__sep"></div><button class="nz-menu-pop__item nz-menu-pop__item--danger">Eliminar</button></div></div>'),
  ("Command palette", ".nz-cmd__item--active",
   '<label class="nz-btn nz-btn--primary" for="cm1">⌘K</label><div class="nz-cmd"><input type="checkbox" id="cm1" hidden><label class="nz-cmd__scrim" for="cm1"></label><div class="nz-cmd__panel"><input class="nz-cmd__input" placeholder="Buscar…"><div class="nz-cmd__list"><div class="nz-cmd__item nz-cmd__item--active"><span class="nz-cmd__icon">◈</span>Abrir informe</div><div class="nz-cmd__item"><span class="nz-cmd__icon">▦</span>Ejecutar</div></div><div class="nz-cmd__foot"><span><kbd>↑</kbd><kbd>↓</kbd> navegar</span><span><kbd>↵</kbd> elegir</span></div></div></div>'),
 ],
 8: [
  ("Tabla", ".nz-table",
   '<div class="nz-table-wrap"><table class="nz-table"><thead><tr><th>Item</th><th class="nz-table__right">Cantidad</th><th>Estado</th></tr></thead><tbody><tr><td class="nz-table__strong">Agua</td><td class="nz-table__num nz-table__right">12</td><td><span class="nz-table__status nz-table__status--ok"><i></i>OK</span></td></tr><tr><td>Comida</td><td class="nz-table__num nz-table__right">8</td><td><span class="nz-table__status nz-table__status--warn"><i></i>Bajo</span></td></tr></tbody></table></div>'),
  ("KPI", ".nz-kpi",
   '<div class="nz-kpi"><span class="nz-kpi__label">Ingresos</span><span class="nz-kpi__value nz-kpi__value--brand">3 420 €</span><span class="nz-kpi__delta nz-kpi__delta--up">+12% vs ayer</span></div>'),
  ("KPI destacado", ".nz-kpi--accent",
   '<div class="nz-kpi nz-kpi--accent"><span class="nz-kpi__label">Cobertura</span><span class="nz-kpi__value">78%</span><span class="nz-kpi__delta">−3%</span></div>'),
  ("Sparkline", ".nz-spark",
   '<div class="nz-spark" style="max-width:16rem"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>'),
  ("Registro", ".nz-record",
   '<div class="nz-records"><div class="nz-record"><span class="nz-record__thumb"></span><div class="nz-record__body"><span class="nz-record__title">Kit familiar</span><span class="nz-record__meta">18 items · revisado</span></div><span class="nz-record__value nz-record__value--brand">▲</span></div></div>'),
  ("Timeline", ".nz-timeline",
   '<div class="nz-timeline"><div class="nz-timeline__item"><span class="nz-timeline__dot"></span><span class="nz-timeline__time">Hoy</span><span class="nz-timeline__title">Revisado</span><span class="nz-timeline__desc">Todo OK</span></div><div class="nz-timeline__item"><span class="nz-timeline__dot nz-timeline__dot--accent"></span><span class="nz-timeline__time">Ayer</span><span class="nz-timeline__title">Añadido</span></div></div>'),
  ("Definition list", ".nz-dl__row",
   '<div class="nz-dl"><div class="nz-dl__row"><dt class="nz-dl__dt">Categoría</dt><dd class="nz-dl__dd">Supervivencia</dd></div><div class="nz-dl__row"><dt class="nz-dl__dt">Precio</dt><dd class="nz-dl__dd nz-dl__dd--brand">34 €</dd></div></div>'),
  ("Status inline", ".nz-inlinestat--ok",
   '<span class="nz-inlinestat nz-inlinestat--ok"><i></i>Disponible</span>'),
  ("Stat badge", ".nz-stat-badge",
   '<span class="nz-stat-badge"><b>4,9</b><span>/ 5</span></span>'),
 ],
 9: [
  ("Imagen responsive", ".nz-img",
   '<img class="nz-img nz-img--rounded" src="data:image/svg+xml;utf8,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 width=%27600%27 height=%27338%27%3E%3Crect width=%27600%27 height=%27338%27 fill=%27%23e5e7eb%27/%3E%3C/svg%3E" alt="placeholder">'),
  ("Caja de imagen 16:9", ".nz-cover--16x9",
   '<div class="nz-cover nz-cover--16x9" style="max-width:16rem;background:var(--nz-brand-soft)"></div>'),
  ("Figure", ".nz-figure figcaption",
   '<figure class="nz-figure"><div class="nz-figure__img" style="max-width:16rem;aspect-ratio:4/3;background:var(--nz-bg-inset)"></div><figcaption>Leyenda bajo la imagen.</figcaption></figure>'),
  ("Avatares", ".nz-avatar--sm/_md/_lg",
   '<div style="display:flex;gap:.5rem;align-items:center"><span class="nz-avatar nz-avatar--sm">DA</span><span class="nz-avatar nz-avatar--md">DA</span><span class="nz-avatar nz-avatar--lg">DA</span></div>'),
  ("Grupo de avatares", ".nz-avatar-group",
   '<div class="nz-avatar-group"><span class="nz-avatar nz-avatar--sm">A</span><span class="nz-avatar nz-avatar--sm">B</span><span class="nz-avatar nz-avatar--sm">C</span><span class="nz-avatar nz-avatar--sm nz-avatar-group__more">+2</span></div>'),
  ("Logo marca", ".nz-brand__mark",
   '<span class="nz-brand"><span class="nz-brand__mark">A7</span> Aurora 7</span>'),
  ("Icono en caja", ".nz-icon-tile--accent",
   '<div style="display:flex;gap:.5rem"><span class="nz-icon-tile">◈</span><span class="nz-icon-tile nz-icon-tile--accent">✳</span><span class="nz-icon-tile nz-icon-tile--success">✓</span><span class="nz-icon-tile nz-icon-tile--danger">!</span></div>'),
  ("Media object", ".nz-media",
   '<div class="nz-media"><span class="nz-avatar nz-avatar--md nz-media__fig">AM</span><div class="nz-media__body"><span class="nz-media__title">Ana</span><span class="nz-media__desc">Diseñadora de producto.</span></div></div>'),
  ("Imagen con badge", ".nz-media-badge",
   '<div class="nz-cover nz-cover--16x9" style="max-width:16rem;position:relative;background:var(--nz-bg-inset)"><span class="nz-badge nz-badge--brand nz-media-badge">PRO</span></div>'),
  ("Vídeo", ".nz-video__play",
   '<div class="nz-video" style="max-width:16rem"><button class="nz-video__play" aria-label="reproducir"><i>▶</i></button></div>'),
 ],
 10: [
  ("Precio", ".nz-price",
   '<p class="nz-price"><span class="nz-price__currency">€</span><span class="nz-price__amount">34</span><span class="nz-price__decimal">,90</span><span class="nz-price__old">49 €</span></p>'),
  ("Precio de plan", ".nz-plan__price",
   '<p class="nz-plan__price">12 € <small>/mes</small></p>'),
  ("Calificación", ".nz-stars__star--full",
   '<div class="nz-stars"><span class="nz-stars__row"><span class="nz-stars__star nz-stars__star--full">★</span><span class="nz-stars__star nz-stars__star--full">★</span><span class="nz-stars__star nz-stars__star--full">★</span><span class="nz-stars__star nz-stars__star--full">★</span><span class="nz-stars__star">★</span></span><span class="nz-stars__count">· 4,9 (128)</span></div>'),
  ("Stock", ".nz-stock--in",
   '<span class="nz-stock nz-stock--low"><i></i>Solo 2 en stock</span>'),
  ("Tarjeta de producto", ".nz-product",
   '<div class="nz-product"><div class="nz-product__media"><span class="nz-badge nz-badge--danger nz-product__badge">-20%</span></div><div class="nz-product__body"><span class="nz-product__cat">Equipamiento</span><span class="nz-product__name">Manta térmica</span><span class="nz-product__rate"><span class="nz-stars"><span class="nz-stars__star nz-stars__star--full">★</span>4,8</span></span></div><div class="nz-product__price"><span class="nz-price"><span class="nz-price__amount">24</span><span class="nz-price__old">30 €</span></span></div><div class="nz-product__cta"><button class="nz-btn nz-btn--primary">Añadir</button></div></div>'),
  ("Plan destacado", ".nz-plan--featured",
   '<div class="nz-plan nz-plan--featured" style="max-width:14rem"><span class="nz-badge nz-badge--brand nz-plan__flag">Popular</span><span class="nz-plan__name">Pro</span><span class="nz-plan__price">24 € <small>/mes</small></span><div class="nz-plan__features"><span class="nz-plan__feature"><i></i>Ilimitado</span><span class="nz-plan__feature--no">✕</span></div><button class="nz-btn nz-btn--primary nz-plan__cta">Elegir</button></div>'),
  ("Fila de carrito", ".nz-cart-item",
   '<div class="nz-cart-item"><span class="nz-cart-item__thumb"></span><div class="nz-cart-item__body"><span class="nz-cart-item__name">Manta térmica</span><span class="nz-cart-item__meta">× 2</span></div><div class="nz-cart-item__right"><span class="nz-cart-item__price">48 €</span><button class="nz-cart-item__remove">Quitar</button></div></div>'),
  ("Resumen de compra", ".nz-summary",
   '<div class="nz-summary" style="max-width:16rem"><div class="nz-summary__row"><span>Subtotal</span><span>120 €</span></div><div class="nz-summary__row"><span>Envío</span><span>4 €</span></div><div class="nz-summary__row nz-summary__row--total"><span>Total</span><span>124 €</span></div></div>'),
  ("Descuento badge", ".nz-off",
   '<span class="nz-off">-20%</span> <span class="nz-off nz-off--green">Recomendado</span>'),
 ],
 11: [
  ("Post de feed", ".nz-post",
   '<article class="nz-post"><div class="nz-post__head"><span class="nz-avatar nz-avatar--sm">DA</span><div class="nz-post__byline"><span class="nz-post__author">David Antizar <span class="nz-feed__verify">✓</span></span><span class="nz-post__handle">@ntizar</span></div><span class="nz-post__time">2h</span></div><p class="nz-post__body">Aurora 7, el design system de 565 objetos, ya está online.</p><div class="nz-post__foot"><button class="nz-social">♥ 12</button><button class="nz-social">↻ 4</button><button class="nz-social">➤</button></div></article>'),
  ("Comentario", ".nz-comment",
   '<div class="nz-comment"><span class="nz-avatar nz-avatar--sm">AM</span><div class="nz-comment__body"><div class="nz-comment__head"><span class="nz-comment__author">Ana</span><span class="nz-comment__time">hace 1h</span></div><p class="nz-comment__text">Increíble trabajo 👏</p><div class="nz-comment__actions"><button>Responder</button></div></div></div>'),
  ("Testimonio", ".nz-quote",
   '<figure class="nz-quote"><p>“Aurora nos quitó horas de diseño y dejó todo coherente.”</p><figcaption class="nz-quote__who"><span class="nz-avatar nz-avatar--sm">LM</span><span class="nz-quote__byline"><span class="nz-quote__name">Luis</span><span class="nz-quote__role">CTO</span></span></figcaption></figure>'),
  ("CTA banner", ".nz-cta-banner",
   '<div class="nz-cta-banner"><h3 class="nz-cta-banner__title">Empieza gratis</h3><p class="nz-cta-banner__body">Monta tu web con Aurora 7.</p><div class="nz-cta-banner__actions"><a class="nz-btn" href="#">Crear cuenta</a><a class="nz-btn nz-btn--ghost" href="#">Ver doc</a></div></div>'),
  ("Miembro de equipo", ".nz-team",
   '<div class="nz-team"><span class="nz-avatar nz-avatar--xl nz-team__avatar">DA</span><span class="nz-team__name">David Antizar</span><span class="nz-team__role">Diseñador</span><span class="nz-team__bio">Creador del sistema.</span></div>'),
  ("Username", ".nz-username",
   '<span class="nz-username"><span class="nz-avatar nz-avatar--xs">DA</span><span class="nz-username__name">David</span><span class="nz-username__handle">@ntizar</span></span>'),
  ("Barra de compartir", ".nz-share",
   '<div class="nz-share"><button aria-label="x">𝕏</button><button aria-label="in">in</button><button aria-label="r">r</button></div>'),
  ("Notificación", ".nz-notif",
   '<div class="nz-notif"><span class="nz-notif__icon">♥</span><div class="nz-notif__body"><span class="nz-notif__title">Nuevo like</span><span class="nz-notif__desc">A tu último post.</span></div></div>'),
 ],
 12: [
  ("Skip-link", ".nz-skip:focus",
   '<a class="nz-skip" href="#contenido" style="position:static">Saltar al contenido</a>'),
  ("Visually hidden", ".nz-visually-hidden",
   '<span class="nz-visually-hidden">Texto solo para lectores de pantalla.</span><span class="nz-text--muted">(mira el código)</span>'),
  ("Con contraste AA", ".nz-contrast__status--aa",
   '<div class="nz-contrast"><span class="nz-contrast__pair"><span class="nz-contrast__chip" style="background:var(--nz-brand)"></span><span class="nz-contrast__chip" style="background:#fff"></span>Brand/blanco</span><span class="nz-contrast__ratio">4.6:1</span><span class="nz-contrast__status nz-contrast__status--aa">AA</span></div>'),
  ("Contraste insuficiente", ".nz-contrast__status--fail",
   '<div class="nz-contrast"><span class="nz-contrast__pair"><span class="nz-contrast__chip" style="background:var(--nz-orange-100)"></span><span class="nz-contrast__chip" style="background:#fff"></span>Sutil/blanco</span><span class="nz-contrast__ratio">1.7:1</span><span class="nz-contrast__status nz-contrast__status--fail">Fail</span></div>'),
  ("Estado del sistema", ".nz-sysstatus--ok",
   '<span class="nz-sysstatus nz-sysstatus--ok"><i></i>Operativo</span>'),
  ("Preferencia de movimiento", ".nz-motion-badge",
   '<span class="nz-motion-badge">Movimiento reducido respetado</span>'),
 ],
}

CAT_NAME = {
 2:"Navegación", 3:"Tipografía", 4:"Acciones y botones", 5:"Formularios e inputs",
 6:"Feedback y estados", 7:"Overlays y diálogo", 8:"Datos, tablas y listas",
 9:"Media e iconografía", 10:"Comercio y producto", 11:"Social y marketing",
 12:"Accesibilidad y sistema",
}
CAT_DESC = {
 2:"Menús, sidebar, tabs, breadcrumbs, paginación, TOC, stepper. Todo táctil, sin JS (checkbox hack accesible).",
 3:"Escala fluida móvil-first, prose, listas, bloque, código, etiquetas, cifras y enlaces con vida.",
 4:"Variantes, tamaños, grupos, selector segmentado, FAB y estados de carga. Táctil 44px.",
 5:"Inputs, textarea, select, check/radio/switch, range, OTP, búsqueda, grupos. Focus-ring accesible.",
 6:"Alertas, badges, chips, skeleton, empty/error, progreso y status. Feedback claro con tokens semánticos.",
 7:"Modal, drawer, sheet, popover, tooltip, menú contextual y command palette. Sin JS obligatorio.",
 8:"Tablas, KPIs, registros, timeline, definition lists y estados de datos en vivo.",
 9:"Imágenes responsive, figure, avatares, logotipos, iconos, media object y vídeo.",
 10:"Precio, tarjeta de producto, calificación, stock, planes, carrito y resumen de compra.",
 11:"Post, feed, comentario, testimonio, CTA banner, equipo y compartición.",
 12:"Skip-link, visible-hidden, contraste, estado del sistema y preferencias. El contrato accesible.",
}

COUNTS = {2:31,3:38,4:36,5:44,6:43,7:34,8:38,9:33,10:41,11:36,12:10}

def build_page(num):
    fname = dict((n, f) for n, name, f, css in NAV)[num]
    css = dict((n, c) for n, name, f, c in NAV)[num]
    name = dict((n, nm) for n, nm, f, c in NAV)[num]
    demos = DEMOS[num]
    lines = []
    lines.append('<!DOCTYPE html>')
    lines.append('<html lang="es" data-nz-theme="light">')
    lines.append('<head>')
    lines.append('<meta charset="UTF-8">')
    lines.append('<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">')
    lines.append(f'<title>Aurora 7 · {str(num).zfill(2)} {CAT_NAME[num]}</title>')
    lines.append('<link rel="stylesheet" href="../tokens.css">')
    lines.append(f'<link rel="stylesheet" href="../packs/{css}">')
    lines.append('<link rel="stylesheet" href="../packs/p0-catalog.css">')
    lines.append('</head>')
    lines.append('<body class="nz nz-root">')
    lines.append('  <a class="nz-skip-link" href="#contenido">Saltar al contenido</a>')
    lines.append('  <header class="cat-topbar">')
    lines.append(f'    <a class="cat-brandmark" href="../index.html"><i></i><i></i> Aurora 7</a>')
    lines.append(f'    <span class="cat-count">{str(num).zfill(2)} · {COUNTS[num]} objetos</span>')
    lines.append('    <button class="theme-toggle" id="btnTheme" aria-label="Cambiar tema">◐</button>')
    lines.append('  </header>')
    lines.append('  <nav class="cat-nav-pages" aria-label="Categorías del catálogo">')
    for n, nm, f, c in NAV:
        if n == num:
            lines.append(f'    <a href="{f}" aria-current="page">{nm}</a>')
        else:
            lines.append(f'    <a href="{f}">{nm}</a>')
    lines.append('  </nav>')
    lines.append('  <main class="nz-container cat-main" id="contenido">')
    lines.append('    <div class="cat-pagehead">')
    lines.append(f'      <p class="cat-pagehead__over">Categoría {str(num).zfill(2)} · {COUNTS[num]} objetos</p>')
    lines.append(f'      <h1>{CAT_NAME[num]}</h1>')
    lines.append(f'      <p>{CAT_DESC[num]}</p>')
    lines.append('    </div>')
    # demos
    for i, (title, tag, markup) in enumerate(demos, 1):
        lines.append(f'    <section class="cat-demo nz-in">')
        lines.append(f'      <div class="cat-demo__title"><span class="cat-demo__num">{i}</span><span class="cat-demo__name">{html.escape(title)}</span><span class="cat-demo__tag">{html.escape(tag)}</span></div>')
        lines.append('      <div class="cat-stage">')
        for seg in markup.split("\n"):
            lines.append('        ' + seg)
        lines.append('      </div>')
        lines.append('    </section>')
    lines.append('  </main>')
    lines.append('  <footer class="cat-footer">')
    lines.append('    Aurora 7 · Hecho con ❤️ por David Antizar · 565 objetos, 1 sistema')
    lines.append('  </footer>')
    lines.append('  <script>')
    lines.append("    document.getElementById('btnTheme').addEventListener('click', function(){var h=document.documentElement; h.setAttribute('data-nz-theme', h.getAttribute('data-nz-theme')==='dark'?'light':'dark');});")
    lines.append('  </script>')
    lines.append('</body>')
    lines.append('</html>')
    return fname, "\n".join(lines) + "\n"

# generar solo las paginas que no existen (02-12)
for num in range(2, 13):
    fname, content = build_page(num)
    out = PAG / fname
    out.write_text(content, encoding="utf-8")
    print("generado:", fname, len(content), "bytes")
print("TOTAL paginas:", len(list(PAG.glob('*.html'))))
