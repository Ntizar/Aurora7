---
name: aurora-design-system
description: "Usa al construir o tocar cualquier web con Aurora 7 (Ntizar/Aurora7, v7.2.1). Pide la solución ya generada (LLM.md + components.json) en vez de leer los packs: ahorra ~60k tokens y no inventa clases."
version: "7.2.1"
tags: [css, design-system, aurora, ntizar, agent-ready, movil]
---

# Aurora 7 — doctrina única (va con el repo)

Design system CSS puro, sin build, sin dependencias, namespaced bajo `.nz-`.
**v7.2.1 · 1.900 objetos · 349 familias · 576 demos · 15 packs · 145 tokens.**

> ⚠️ Esta skill **no es un resumen libre**: es el contrato de uso de `Ntizar/Aurora7`.
> Se actualiza **en el mismo ciclo** que el repo. Si la versión de aquí no coincide
> con el último tag de git, gana el repo.
> La v5/v6 (liquid glass, mesh, orbs, skins OKLCH, escenas Three.js) está **JUBILADA**:
> `nz-glass-*`, `nz-aurora-mesh`, `nz-orb`, `nz-card--glass*`, `data-nz-skin`,
> `three-scenes.js` **no existen en v7**. Solo para mantener repos legacy.

## 1. Regla de oro: pide la solución, no la escribas

El repo **ya genera la solución** para agentes. Leerla cuesta ~10 KB; leer los packs
cuesta ~250 KB (≈60k tokens). Nunca pegues CSS de packs en el prompt.

| Necesitas | Pídelo aquí (tag pineado) |
|---|---|
| Decidir qué packs y qué clases | `https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@v7.2.1/LLM.md` |
| API exacta (familias, partes, modificadores, tokens, alias EN→ES) | `.../@v7.2.1/components.json` |
| Página completa que ya funciona | `.../@v7.2.1/examples/` (login, dashboard, landing, chat-ia, forms) |
| Demo viva de un objeto | `https://ntizar.github.io/Aurora7/paginas/NN-*.html` |

```bash
curl -s https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@v7.2.1/LLM.md          # ~10 KB
curl -s https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@v7.2.1/components.json # API completa
```
Si el repo está clonado, tira de disco (más rápido y sin red):
`C:/Users/d_ant/Projects/Aurora-7/{LLM.md,components.json,examples/}`.

**Corolario:** si algo no está en `components.json`, no existe. No lo inventes: o se
usa el objeto que sí existe, o **se añade al sistema** (sección 8) para que el
siguiente proyecto lo herede en vez de reinventarlo. Un patrón resuelto dos veces en
dos proyectos es un fallo del sistema, no del proyecto.

## 2. Contrato de sincronía (skill ↔ repo)

Todo cambio de Aurora 7 cierra con la skill al día, en el mismo commit:

1. Sube la versión en el repo (`scripts/generar-llm-docs.py` → `VERSION`, README, AGENTS.md).
2. Actualiza **`SKILL.md` dentro del repo** (viaja con el código, la CI la valida:
   versión y cifras contra `components.json`).
3. Copia ese `SKILL.md` a esta skill local y sube `version:` en el frontmatter.
4. Tag `vX.Y.Z` **en el último commit verde** (`git push origin vX.Y.Z`).
5. Ajusta el tag pineado del proyecto consumidor y recompila.

Gate del repo: `python scripts/validar-css.py` → si no dice `RESULTADO: VÁLIDO`, no está terminado.
Entre sus puertas está que doc, generador, `SKILL.md` y tag de git digan lo mismo.

## 3. CDN pineado (nunca @master en producción)

```html
<html lang="es" data-nz-theme="light">   <!-- o "dark" -->
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@v7.2.1/tokens.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@v7.2.1/packs/all.css">
</head>
<body class="nz">
```

`all.css` solo para prototipos; en producción enlaza los packs que uses (12-40 KB cada uno).
jsDelivr sirve `@master` desde caché por edge (bug de CSS viejo ya vivido): pinea siempre.
Purga: `curl https://purge.jsdelivr.net/gh/Ntizar/Aurora7@vX.Y.Z/<fichero>`.

## 4. Móvil: ya viene resuelto (v7.2.1) — no lo reinventes por proyecto

Esto es lo que se rompía una y otra vez. Ahora lo garantiza el sistema, sin JS:

| Problema clásico | Objeto del sistema |
|---|---|
| Tabla de datos que se aplasta o desborda la página | `.nz-table-wrap--apilable` > `.nz-table--apilable` con `data-etiqueta="Columna"` en cada `td`. En móvil cada fila es una tarjeta con el nombre de su columna delante; desde 640 px vuelve a ser tabla |
| Tabla ancha de verdad (Gantt, calendario) | `.nz-table-wrap` (scroll propio). **Nunca** una tabla ancha suelta fuera de un wrap: su `min-width: 30rem` estira la página entera |
| Pestañas que se cortan | `.nz-tabs` **envuelve** en varias líneas (todas alcanzables). Una sola línea a propósito: `.nz-tabs--scroll` |
| Acciones de la navbar inalcanzables | `.nz-navbar` y `.nz-navbar__links` **envuelven**: ninguna acción se corta |
| Un hijo de rejilla que desborda | `.nz-dash-grid`, `.nz-split`, `.nz-thirds`, `.nz-bento`, `.nz-grid-12`, `.nz-holy`, `.nz-article` ya traen `min-width: 0` en sus hijos |

Ejemplo apilable (contenido real, una línea de markup por fila):

```html
<div class="nz-table-wrap nz-table-wrap--apilable">
  <table class="nz-table nz-table--apilable">
    <thead><tr><th>Entrega</th><th>Entregable</th><th class="nz-table__right">Horas</th></tr></thead>
    <tbody>
      <tr><th scope="row">Informe de requisitos</th>
        <td data-etiqueta="Entrega">oct 2026</td>
        <td class="nz-table__num nz-table__right" data-etiqueta="Horas">32 h</td></tr>
    </tbody>
  </table>
</div>
```

Regla de dedo: **ancho intrínseco → scroll**; **datos tabulares → apilable**.

## 5. Las reglas duras (la CI las valida)

1. Todo lo público vive bajo `.nz-` (nada de clases globales).
2. Todo valor es un token `var(--nz-*)` — ni un `#2563eb` ni un `16px` a mano.
3. **0 gradientes, 0 `backdrop-filter`, 0 `!important`** (excepciones: `.nz-visually-hidden`, `.nz-print-hide`, helpers de visibilidad con sufijo `[class]`).
4. BEM: `.nz-thing`, `__parte`, `--modificador`, estado `.is-x` o `[aria-*]`.
5. Mobile-first real: base 1 columna, crecer con `@media (min-width: 640/960/1200)`. Nunca `max-width` como estrategia (los `max-width` de consumidor solo para apagar un patrón móvil, nunca para construirlo).
6. Táctil 44px en todo lo que se pulsa.
7. Una clase, un dueño (un pack). El shell del catálogo (`.cat-*`) jamás declara `.nz-*`.
8. Footer exacto: `Hecho con ❤️ por David Antizar` (emoji U+2764, sin variantes).
9. Todo en castellano (clases incluidas cuando toca: `nz-arbol`, `nz-filezona`, `nz-fieldset__leyenda`).

## 6. Flujo del agente para generar HTML con Aurora 7

1. **Lee `LLM.md`** del tag pineado (combos por tipo de página, tabla «necesito X → uso Y», alias, anti-patrones).
2. **Consulta `components.json`** para la API exacta (familias, partes, modificadores, tokens, alias EN→ES: `tree` → `nz-arbol`).
3. **Copia una receta de `examples/`** y quítale lo que no uses.
4. **Verifica el HTML**: `python scripts/auditar-uso.py tu-pagina.html` → clases inventadas, packs que faltan, gradientes, colores a mano, desktop-first, atribución. 0 fallos o no está terminado.
5. **Mídelo en móvil de verdad**, no de vista: viewport a 320/360/390 y comprobar que `document.scrollingElement.scrollWidth == clientWidth` en todas las pestañas/secciones. Es la prueba objetiva de que nada se sale.
6. Verificación visual en preview (el lint no ve la estética). Texto por código (`grep`), no por visión: `vision_analyze` alucina erratas.

## 7. Necesito X → uso Y (verificado contra el censo)

| Necesito | Clases |
|---|---|
| Botón (p4) | `.nz-btn` + `--primary/--accent/--ghost/--soft/--outline/--danger` + `--sm/--lg/--icon` |
| Superficie (p1) | `.nz-article`, `.nz-bento`, `.nz-thirds`, `.nz-hero-bleed` · **`.nz-card` NO existe** |
| Formulario (p5) | `.nz-field` > `__label` + `.nz-input` + `__help`, `.nz-formgrid`, `.nz-fieldset__leyenda` |
| Opciones (p5) | `.nz-checkbox`, `.nz-radio`, `.nz-switch`, `.nz-segmented` |
| Aviso (p6) | `.nz-alert--info/--success/--warning/--danger`, `.nz-callout`, `.nz-badge--*` |
| Tabla ancha (p8) | `.nz-table-wrap` > `.nz-table` (+ `--striped`, `__num`, `__status`) |
| Tabla que debe caber entera (p8) | `.nz-table-wrap--apilable` > `.nz-table--apilable` + `data-etiqueta` |
| KPI (p8) | `.nz-kpi` (`__label/__value/__delta`) |
| Gráfico (p13) | `.nz-chart` + `.nz-chart-bar/-line/-donut/-gauge`, `.nz-heatmap` |
| Diálogo (p7) | `.nz-modal` (sin JS), `.nz-drawer`, `.nz-sheet` |
| Layout (p1) | `.nz-appshell`, `.nz-with-sidebar`, `.nz-split`, `.nz-dash-grid`, `.nz-container` |
| Navegación (p2) | `.nz-navbar`, `.nz-tabs` (+ `--scroll`, `--pill`), `.nz-breadcrumb`, `.nz-stepper`, `.nz-pagination` |
| Chat IA (p14) | `.nz-chat`, `.nz-msg`, `.nz-prompt`, `.nz-toolcall`, `.nz-taskplan`, `.nz-approval` |
| Escritorio (p15) | `.nz-window`, `.nz-appnav`, `.nz-kanban`, `.nz-actbar`, `.nz-statusbar` |

Léxico cerrado de modificadores (igual en los 15 packs): tamaño `--2xs/--xs/--sm/--lg/--xl`,
tono `--brand/--accent/--success/--warning/--danger/--info/--neutral`, énfasis `--solid/--soft/--outline/--ghost`,
disposición `--vertical/--horizontal/--inline/--compact/--spacious/--center/--between/--end`,
forma `--square/--rounded/--pill`, elevación `--flat/--raised`, estados `.is-active/.is-disabled/.is-loading/.is-done/.is-error/.is-empty/.is-selected`.

## 8. Ampliar el sistema (promover, no parchear)

Cuando un proyecto necesita algo que no existe, **se sube al sistema**, no se queda
en el CSS del proyecto:

1. Declara las clases en el pack correspondiente (tokens, sin `!important`, sin gradientes).
2. Añade su demo en `specs/NN.json` (markup en UNA línea, contenido real en castellano, inline solo para geometría con `var(--nz-*)`).
3. Regenera y valida hasta verde: `python scripts/build-catalog.py && python scripts/audit-catalog.py && python scripts/audit-html.py && python scripts/validar-css.py`. Cero «clases declaradas sin demo», cero duplicados entre packs.
4. Sube la versión (`VERSION` + README + AGENTS.md + `SKILL.md`) y tag `vX.Y.Z` en el último commit verde.
5. Actualiza esta skill (versión, cifras, objeto nuevo) y el tag del consumidor.

Criterio de admisión: (a) resuelve un problema real y repetido, (b) es mobile-first sin JS,
(c) encaja en el léxico cerrado, (d) lleva demo viva, (e) no duplica nada que ya exista.

## 9. Anti-patrones (errores reales acumulados)

- ❌ Clases de la v6: `nz-card--glass-liquid-*`, `nz-gradient-text`, `nz-aurora-mesh`, `nz-orb`, `u-nz-text-brand`, `data-nz-skin`. En v7 no existen. Títulos destacados: `.nz-h1--brand`.
- ❌ Inventar clases (auditadas en el pasado: `nz-btn--glass-liquid-secondary`, `nz-fieldset__legend` — lo real es `__leyenda`). Si no está en `components.json`, no existe.
- ❌ Colores a mano o degradados azul→naranja: el azul es primario y el naranja acento, **en elementos separados**. Gradiente solo monocromo si acaso (en v7, ninguno).
- ❌ KPIs gigantes (2.5rem+) y bordes decorativos superiores en cards («look de IA»).
- ❌ Enlazar `@master` en producción, o pegar el CSS de los packs en el prompt.
- ❌ Desborde horizontal: nada puede dejar `scrollWidth > clientWidth` en el documento. Si pasa, es un fallo de entrega, no un detalle.
- ❌ Arreglar el móvil con `max-width` como estrategia, con `overflow-x` a lo bruto en el `body`, o escondiendo columnas con `display:none` (se pierde el dato).
- ❌ `white-space: nowrap` en una tabla que se apila: mata el apilado y fuerza scroll.
- ❌ Dejar el patrón resuelto en el proyecto y no subirlo a Aurora.

## 10. Verificación pre-entrega (checklist)

1. `auditar-uso.py` sobre el HTML → 0 fallos.
2. `<html lang="es" data-nz-theme="light">` + `<body class="nz">` + CDN pineado.
3. Footer exacto con atribución.
4. Móvil medido, no admirado: scrollWidth == clientWidth a 320/360/390 y en todas las pestañas; táctil 44px.
5. Escritorio y print (si es informe) sin regresión.
6. Mirar la página en preview (verificar, no confiar). Texto por código.

## 11. Excepciones vigentes (cuándo NO usar Aurora 7)

- **Design systems corporativos**: si un equipo pide un CSS con los colores de SU marca (ej. Kaizen/Ineco #1A4488), se crea un sistema propio alineado con su manual, no Aurora.
- **Presentaciones consulting / informes ejecutivos** (estilo McKinsey/BCG): fondo blanco elegante, sin estética tech. David rechazó Aurora para esos entregables.

## 12. Migrar de v6.1 a v7

No es cambiar dos URLs: es reescribir markup. Medido en caso real: de 107 clases usadas
solo 22 existían en v7. Sin equivalencia 1:1 (`nz-card` → `nz-article`/`nz-bento`/`nz-thirds`;
mesh/orbs/3D desaparecen). Receta y script de medición en `references/migracion-v6-a-v7.md`.

## 13. Referencias del repo Aurora 7

- `SKILL.md` — esta misma skill, **dentro del repo** (la CI la valida contra `components.json`).
- `AGENTS.md` — reglas duras del repo.
- `LLM.md` — guía de decisión para agentes (la fuente principal; esta skill la resume).
- `components.json` — API machine-readable (familias, tokens, alias, combos).
- `examples/` — 5 recetas completas verificadas con el lint.
- `scripts/auditar-uso.py` — lint del HTML consumidor (selftest incluido).
- `references/migracion-v6-a-v7.md` y el caso Aurora 7 en la skill `design-system-coherence-audit`.

Hecho con ❤️ por David Antizar
