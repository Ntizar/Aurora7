# AGENTS.md — reglas duras para trabajar en Aurora 7

Este repositorio es un **design system CSS puro**, sin build y sin dependencias.
Si eres un agente (o una persona con prisa), lee esto antes de tocar nada.

> Aurora 7 **no** es `Ntizar-Aurora` (la versión v5/v6 con liquid glass, mesh y skins).
> Aquí el manifiesto es otro: sólido, sin gradientes, sin glass. No mezcles sus clases.

---

## 1. Las 7 reglas del sistema

1. **Todo lo público vive bajo `.nz-`**. Nada de clases globales sueltas.
2. **Todo valor es un token `--nz-*`**. Ni un `#2563eb` ni un `16px` de diseño a mano.
3. **Sin gradientes, sin `backdrop-filter`, sin `!important`**
   (solo se admiten en `.nz-visually-hidden`, `.nz-vh` y `.nz-print-hide`).
4. **BEM**: `.nz-thing`, `.nz-thing__parte`, `.nz-thing--modificador`, estado `.is-x` o `[aria-*]`.
5. **Mobile-first de verdad**: base 1 columna y se crece con `@media (min-width: …)`
   (640 / 960 / 1200). Nunca `max-width` como estrategia.
6. **Táctil 44px** en todo lo que se pulsa.
7. **Una clase, un dueño**: una clase se declara en un solo pack.

## 2. Dónde va cada cosa

| Archivo | Qué es | ¿Se edita a mano? |
|---|---|---|
| `tokens.css` | Fuente única de verdad de los tokens | Sí |
| `packs/pN-*.css` | Los 15 packs, uno por categoría | Sí |
| `packs/p0-catalog.css` | Shell del catálogo (`.cat-*`) | Sí, pero **solo con clases `.cat-*`** |
| `specs/NN.json` | **Fuente de verdad de las demos** (titulo, tag, markup) | Sí |
| `paginas/*.html` | Catálogo generado | **No** — se regenera |
| `index.html` | Portada generada | **No** — se regenera |
| `datos/objetos.json` | Índice para el buscador | **No** — se regenera |
| `audit/` | Informe de auditoría | **No** — se regenera |
| `js/catalog.js` | Buscador, filtro, tema, «ver código» | Sí |

### ⚠️ El error que costó más caro

`p0-catalog.css` **no puede declarar clases del sistema**. Si el shell define `.nz-btn`,
como el catálogo carga el shell después de los packs, **pisa el componente real** y el
catálogo enseña algo que no es el sistema. El shell solo tiene clases propias: `.cat-*`
y `.demo-*`.

## 3. Cómo añadir o ampliar un objeto

1. Declara sus clases en el pack que le corresponda.
2. Añade su demo en `specs/NN.json` (una línea de markup, contenido real, sin JavaScript).
3. Regenera y valida:

```bash
python scripts/build-catalog.py     # páginas + portada + índice del buscador
python scripts/audit-catalog.py     # auditoría campo a campo → audit/AUDITORIA.md
python scripts/audit-html.py        # informe navegable → audit/index.html
python scripts/validar-css.py       # manifiesto + cobertura (esto es lo que corre CI)
```

4. Si `validar-css.py` no dice `RESULTADO: VÁLIDO`, no está terminado.

## 4. Léxico de modificadores

Los 15 packs hablan el mismo idioma. Usa estos modificadores, y solo estos:

| Eje | Modificadores |
|---|---|
| Tamaño | `--2xs` `--xs` `--sm` `--lg` `--xl` |
| Tono | `--brand` `--accent` `--success` `--warning` `--danger` `--info` `--neutral` |
| Énfasis | `--solid` `--soft` `--outline` `--ghost` |
| Disposición | `--vertical` `--horizontal` `--inline` `--compact` `--spacious` `--center` `--between` `--end` |
| Forma | `--square` `--rounded` `--pill` |
| Elevación | `--flat` `--raised` |
| Estado | `.is-active` `.is-disabled` `.is-loading` `.is-done` `.is-error` `.is-empty` `.is-selected` o `[aria-current]` `[aria-selected]` `[aria-expanded]` |

## 5. Consumir el sistema (tú, agente, desde otro proyecto)

- `LLM.md` — guía de decisión (~4 KB): qué pack cargar y qué clases usar.
- `components.json` — API completa machine-readable: familia → pack, clases, modificadores, partes y página de demo.
- `examples/` — 5 recetas completas (login, dashboard, landing, chat-ia, forms) que puedes copiar y adaptar.
- `paginas/` — catálogo con una demo viva por objeto.
- Léxico cerrado de modificadores: tamaño `--2xs/--xs/--sm/--lg/--xl`, tono `--brand/--accent/--success/--warning/--danger/--info/--neutral`, énfasis `--solid/--soft/--outline/--ghost`, disposición `--compact/--spacious/--center`, estados `.is-*`.

**No pegues los packs CSS en el prompt** (≈340 KB). Enlaza por CDN (siempre pineado, nunca @master):

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@v7.2.0/tokens.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Ntizar/Aurora7@v7.2.0/packs/all.css">
```

## 6. Atribución

Todo HTML generado lleva el pie exacto:

```
Hecho con ❤️ por David Antizar
```

Sin variantes, sin «via Mastermind», sin `(L)`.
