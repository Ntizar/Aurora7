# Aurora 7

Design system CSS de Ntizar. **565 objetos de frontend** en 12 categorías, listos para montar cualquier web.

## Manifiesto

- **Azul #2563eb** primario · **Naranja #f97316** acento (nunca fundidos)
- **0 gradientes** · **0 glass** · **0 IA-slop**
- **Mobile-first** real (base 1 columna, breakpoints con min-width)
- **Táctil 44px** · safe-area iOS · **light + dark**

## Estructura

```
Aurora-7/
├── index.html        # portada del catálogo (565 objetos, 12 categorías)
├── tokens.css        # fuente única de verdad de tokens (colores, escala, espacio, radios, sombras, movimiento)
├── packs/
│   ├── p0-catalog.css      # shell compartido del catálogo (topbar, tarjetas, hero, demos)
│   ├── p1-layout.css       # 01 · Layout y estructura
│   ├── p2-navigation.css   # 02 · Navegación
│   ├── p3-typography.css   # 03 · Tipografía
│   ├── p4-actions.css      # 04 · Acciones y botones
│   ├── p5-forms.css        # 05 · Formularios e inputs
│   ├── p6-feedback.css     # 06 · Feedback y estados
│   ├── p7-overlays.css     # 07 · Overlays y diálogo
│   ├── p8-data.css         # 08 · Datos, tablas y listas
│   ├── p9-media.css        # 09 · Media e iconografía
│   ├── p10-commerce.css    # 10 · Comercio y producto
│   ├── p11-social.css      # 11 · Social y marketing
│   └── p12-system.css      # 12 · Accesibilidad y sistema
├── paginas/
│   └── 01-…-12-*.html      # catálogo de cada categoría (objetos demo en vivo)
└── scripts/
    └── build-catalog.py    # genera páginas 02-12 desde specs (regenerable)
```

## Uso

Dos opciones:

1. **Página real**: enlaza `tokens.css` + los packs que necesites:
   ```html
   <link rel="stylesheet" href="tokens.css">
   <link rel="stylesheet" href="packs/p4-actions.css">
   ```
2. **Explorar**: abre `index.html` y navega las 12 categorías — cada objeto tiene su demo viva.

Todos los componentes comparten el prefijo `.nz-` y los tokens `--nz-*`. Nada colisiona con otros frameworks.

Hecho con ❤️ por David Antizar
