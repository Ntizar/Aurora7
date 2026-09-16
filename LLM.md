# Aurora 7 — guía de decisión para agentes

Design system CSS puro, sin dependencias ni build. 1829 objetos en 15 categorías.
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
| 01 · Layout y estructura | `p1-layout.css` | `nz-appshell`, `nz-article`, `nz-aside`, `nz-aspect`… |
| 02 · Navegación | `p2-navigation.css` | `nz-breadcrumb`, `nz-dropdown`, `nz-menu`, `nz-navbar`… |
| 03 · Tipografía | `p3-typography.css` | `nz--leading-normal`, `nz--leading-snug`, `nz--leading-tight`, `nz--tracking-caps`… |
| 04 · Acciones y botones | `p4-actions.css` | `nz-btn`, `nz-btn-group`, `nz-cta`, `nz-fab`… |
| 05 · Formularios e inputs | `p5-forms.css` | `nz-checkbox`, `nz-field`, `nz-fieldset`, `nz-filezona`… |
| 06 · Feedback y estados | `p6-feedback.css` | `nz-alert`, `nz-badge`, `nz-banner`, `nz-callout`… |
| 07 · Overlays y diálogo | `p7-overlays.css` | `nz-backdrop`, `nz-cmd`, `nz-confirm`, `nz-drawer`… |
| 08 · Datos, tablas y listas | `p8-data.css` | `nz-arbol`, `nz-compare`, `nz-datagrid`, `nz-dl`… |
| 09 · Media e iconografía | `p9-media.css` | `nz-audio`, `nz-avatar`, `nz-avatar-group`, `nz-bgimg`… |
| 10 · Comercio y producto | `p10-commerce.css` | `nz-cart`, `nz-cart-item`, `nz-checkout-steps`, `nz-compare-bar`… |
| 11 · Social y marketing | `p11-social.css` | `nz-activity`, `nz-comment`, `nz-cta-banner`, `nz-feed`… |
| 12 · Accesibilidad y sistema | `p12-system.css` | `nz-a11y-badge`, `nz-atajo-teclado`, `nz-contrast`, `nz-focus-accent`… |
| 13 · Gráficos y visualización | `p13-charts.css` | `nz-bullet`, `nz-chart`, `nz-chart-bar`, `nz-chart-compare`… |
| 14 · IA y agentes | `p14-ai.css` | `nz-agent-card`, `nz-approval`, `nz-attach`, `nz-chat`… |
| 15 · Apps y escritorio | `p15-apps.css` | `nz-actbar`, `nz-agenda`, `nz-appempty`, `nz-appnav`… |

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
:root {
  --nz-brand: #2563eb;          /* color primario */
  --nz-accent: #f97316;         /* acento, nunca fundido con el primario */
  --nz-font: "Inter", system-ui, sans-serif;
  --nz-radius-md: 10px;
  --nz-container-max: 72rem;
}
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
