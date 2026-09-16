# -*- coding: utf-8 -*-
"""Escribe specs/04.json (Acciones y botones) y comprueba la cobertura clase↔demo."""
import json
import pathlib
import sys

ROOT = pathlib.Path(r"C:\Users\d_ant\Projects\Aurora-7")
sys.path.insert(0, str(ROOT / "scripts"))
from importlib import import_module

bc = import_module("build-catalog")
D = []


def d(t, tag, m):
    D.append({"titulo": t, "tag": tag, "markup": m})


d("Acción principal y tonos", ".nz-btn--primary · --accent · --success · --warning · --danger · --info · --neutral",
  '<div class="nz-cluster"><button class="nz-btn nz-btn--primary">Primario</button><button class="nz-btn nz-btn--accent">Acento</button><button class="nz-btn nz-btn--success">Correcto</button><button class="nz-btn nz-btn--warning">Aviso</button><button class="nz-btn nz-btn--danger">Peligro</button><button class="nz-btn nz-btn--info">Info</button><button class="nz-btn nz-btn--neutral">Neutro</button></div>')

d("Énfasis del botón", ".nz-btn--soft · --soft-accent · --soft-success · --soft-danger · --ghost · --outline",
  '<div class="nz-cluster"><button class="nz-btn nz-btn--soft">Suave</button><button class="nz-btn nz-btn--soft-accent">Suave acento</button><button class="nz-btn nz-btn--soft-success">Suave ok</button><button class="nz-btn nz-btn--soft-danger">Suave peligro</button><button class="nz-btn nz-btn--ghost">Fantasma</button><button class="nz-btn nz-btn--outline">Contorno</button></div>')

d("Botones de texto", ".nz-btn--link · --text · --danger-text",
  '<div class="nz-cluster"><button class="nz-btn nz-btn--link">Enlace subrayado</button><button class="nz-btn nz-btn--text">Texto</button><button class="nz-btn nz-btn--text nz-btn--danger-text">Eliminar</button></div>')

d("Tamaños de botón", ".nz-btn--2xs · --xs · --sm · --lg · --xl · --2xl",
  '<div class="nz-cluster"><button class="nz-btn nz-btn--primary nz-btn--2xs">2XS</button><button class="nz-btn nz-btn--primary nz-btn--xs">XS</button><button class="nz-btn nz-btn--primary nz-btn--sm">SM</button><button class="nz-btn nz-btn--primary">Base</button><button class="nz-btn nz-btn--primary nz-btn--lg">LG</button><button class="nz-btn nz-btn--primary nz-btn--xl">XL</button><button class="nz-btn nz-btn--primary nz-btn--2xl">2XL</button></div>')

d("Formas y anchos", ".nz-btn--square · --rounded · --pill · --block · --full · --auto",
  '<div class="nz-stack nz-stack--sm"><div class="nz-cluster"><button class="nz-btn nz-btn--primary nz-btn--square">Cuadrado</button><button class="nz-btn nz-btn--primary nz-btn--rounded">Redondeado</button><button class="nz-btn nz-btn--primary nz-btn--pill">Píldora</button><button class="nz-btn nz-btn--primary nz-btn--auto">Automático</button></div><div style="max-width:22rem"><button class="nz-btn nz-btn--primary nz-btn--block">Ancho completo</button></div><div style="max-width:22rem"><button class="nz-btn nz-btn--ghost nz-btn--full">Extremos separados<span class="nz-btn__icon">→</span></button></div></div>')

d("Botón con icono y flecha", ".nz-btn__icon · __arrow · __arrow--right · __arrow--left",
  '<div class="nz-cluster"><button class="nz-btn nz-btn--primary"><span class="nz-btn__icon">＋</span> Crear</button><button class="nz-btn nz-btn--ghost">Siguiente<span class="nz-btn__arrow nz-btn__arrow--right">→</span></button><button class="nz-btn nz-btn--ghost"><span class="nz-btn__arrow nz-btn__arrow--left">←</span> Anterior</button></div>')

d("Botones de solo icono", ".nz-btn--icon · --icon-sm · --icon-lg · --icon-square",
  '<div class="nz-cluster"><button class="nz-btn nz-btn--primary nz-btn--icon" aria-label="Añadir">＋</button><button class="nz-btn nz-btn--ghost nz-btn--icon-sm" aria-label="Editar">✎</button><button class="nz-btn nz-btn--primary nz-btn--icon-lg" aria-label="Reproducir">▶</button><button class="nz-btn nz-btn--ghost nz-btn--icon-square" aria-label="Ajustes">⚙</button></div>')

d("Botón con contador", ".nz-btn--badged · .nz-btn__badge",
  '<button class="nz-btn nz-btn--ghost nz-btn--badged">Mensajes<span class="nz-btn__badge">7</span></button> <button class="nz-btn nz-btn--primary nz-btn--badged">Notificaciones<span class="nz-btn__badge">12</span></button>')

d("Estados del botón", ".is-busy · .is-loading · .is-ok · .is-copied · :disabled · [aria-pressed]",
  '<div class="nz-cluster"><button class="nz-btn nz-btn--primary is-busy" aria-busy="true">Guardando…</button><button class="nz-btn nz-btn--primary is-loading">Cargando…</button><button class="nz-btn nz-btn--primary is-ok">✓ Guardado</button><button class="nz-btn nz-btn--ghost is-copied">✓ Copiado</button><button class="nz-btn nz-btn--primary" disabled>Deshabilitado</button><button class="nz-btn nz-btn--ghost" aria-pressed="true">Activo</button><button class="nz-btn nz-btn--ghost" aria-pressed="false">Inactivo</button></div>')

d("Botón con progreso interno", ".nz-btn--progress · .nz-btn__progress",
  '<button class="nz-btn nz-btn--primary nz-btn--progress">Subiendo archivo…<span class="nz-btn__progress"></span></button>')

d("Grupo de botones", ".nz-btn-group · --joined · --vertical · --split · __caret",
  '<div class="nz-stack nz-stack--sm"><div class="nz-btn-group"><button class="nz-btn nz-btn--ghost">Uno</button><button class="nz-btn nz-btn--ghost">Dos</button><button class="nz-btn nz-btn--ghost">Tres</button></div><div class="nz-btn-group nz-btn-group--joined"><button class="nz-btn nz-btn--ghost">Izquierda</button><button class="nz-btn nz-btn--ghost">Centro</button><button class="nz-btn nz-btn--ghost">Derecha</button></div><div class="nz-btn-group nz-btn-group--vertical" style="max-width:12rem"><button class="nz-btn nz-btn--ghost">Arriba</button><button class="nz-btn nz-btn--ghost">Medio</button><button class="nz-btn nz-btn--ghost">Abajo</button></div><div class="nz-btn-group nz-btn-group--split"><button class="nz-btn nz-btn--primary">Guardar</button><button class="nz-btn nz-btn--primary nz-btn-group__caret" aria-label="Más opciones">▾</button></div></div>')

d("Selector segmentado", ".nz-segmented · --sm · --lg · --vertical · --full · --brand · --accent",
  '<div class="nz-stack nz-stack--sm"><div class="nz-segmented"><button aria-selected="true">Lista</button><button aria-selected="false">Cuadrícula</button><button aria-selected="false">Mapa</button></div><div class="nz-segmented nz-segmented--sm"><button aria-selected="true">Hoy</button><button aria-selected="false">Semana</button></div><div class="nz-segmented nz-segmented--lg"><button aria-selected="true">Mensual</button><button aria-selected="false">Anual</button></div><div class="nz-segmented nz-segmented--vertical" style="max-width:10rem"><button aria-selected="true">Perfil</button><button aria-selected="false">Cuenta</button><button aria-selected="false">Facturas</button></div><div class="nz-segmented nz-segmented--full"><button aria-selected="true">Todo</button><button aria-selected="false">Abiertos</button><button aria-selected="false">Cerrados</button></div><div class="nz-segmented nz-segmented--brand"><button aria-selected="true">Marca</button><button aria-selected="false">Otra</button></div><div class="nz-segmented nz-segmented--accent"><button aria-selected="true">Acento</button><button aria-selected="false">Otra</button></div></div>')

d("Botones flotantes (FAB)", ".nz-fab · --accent · --lg · --sm · --extended · --bottom-left",
  '<div class="nz-cluster"><button class="nz-fab nz-fab--sm" aria-label="Nuevo pequeño">＋</button><button class="nz-fab" aria-label="Nuevo">＋</button><button class="nz-fab nz-fab--lg" aria-label="Nuevo grande">＋</button><button class="nz-fab nz-fab--accent" aria-label="Nuevo acento">＋</button><button class="nz-fab nz-fab--extended">＋ Crear pedido</button><button class="nz-fab nz-fab--bottom-left" aria-label="Nuevo a la izquierda">＋</button></div>')

d("Cargadores en línea", ".nz-spin · --sm · --lg · --brand · --accent",
  '<div class="nz-cluster"><span class="nz-spin nz-spin--sm"></span><span class="nz-spin"></span><span class="nz-spin nz-spin--lg"></span><span class="nz-spin nz-spin--brand"></span><span class="nz-spin nz-spin--accent"></span><span class="nz-btn nz-btn--primary"><span class="nz-spin nz-spin--sm"></span> Procesando…</span></div>')

d("Enlaces de acción", ".nz-cta · __arrow · --accent · --sm · --lg · --muted · --underline",
  '<div class="nz-cluster"><a class="nz-cta" href="#">Explorar<span class="nz-cta__arrow">→</span></a><a class="nz-cta nz-cta--accent" href="#">Comprar</a><a class="nz-cta nz-cta--sm" href="#">Pequeño</a><a class="nz-cta nz-cta--lg" href="#">Grande</a><a class="nz-cta nz-cta--muted" href="#">Discreto</a><a class="nz-cta nz-cta--underline" href="#">Subrayado</a></div>')

d("Barra de herramientas", ".nz-toolbar · __spacer · __group · __divider · --compact · --sticky · --brand",
  '<div class="nz-stack nz-stack--sm"><div class="nz-toolbar"><button class="nz-btn nz-btn--ghost nz-btn--sm">Abrir</button><button class="nz-btn nz-btn--ghost nz-btn--sm">Editar</button><span class="nz-toolbar__divider"></span><div class="nz-toolbar__group"><button class="nz-btn nz-btn--ghost nz-btn--sm" aria-label="Negrita">B</button><button class="nz-btn nz-btn--ghost nz-btn--sm" aria-label="Cursiva">I</button></div><span class="nz-toolbar__spacer"></span><button class="nz-btn nz-btn--primary nz-btn--sm">Exportar</button></div><div class="nz-toolbar nz-toolbar--compact"><button class="nz-btn nz-btn--ghost nz-btn--xs">Corto</button><button class="nz-btn nz-btn--ghost nz-btn--xs">Compacto</button></div><div class="nz-toolbar nz-toolbar--brand"><button class="nz-btn nz-btn--ghost nz-btn--sm">Marca</button><span class="nz-toolbar__spacer"></span><button class="nz-btn nz-btn--accent nz-btn--sm">Destacar</button></div><div class="nz-toolbar nz-toolbar--sticky"><button class="nz-btn nz-btn--ghost nz-btn--sm">Pegajosa</button></div></div>')

spec = {
    "cat": 4,
    "nombre": "Acciones y botones",
    "desc": "Botones con sus tonos, énfasis, tamaños y formas; grupos, selector segmentado, botones flotantes, cargadores, enlaces de acción y barras de herramientas. Todo con el objetivo táctil de 44px.",
    "pack": "p4-actions.css",
    "fichero": "04-actions.html",
    "demos": D,
}

(ROOT / "specs" / "04.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"specs/04.json escrito · {len(D)} demos")

declaradas = bc.clases_declaradas(ROOT / "packs" / "p4-actions.css")
usadas = set()
for demo in D:
    usadas |= bc.clases_de_markup(demo["markup"])
existentes = {c for p in bc.PACKS_COMPONENTES if (bc.PACKS / p).exists()
              for c in bc.clases_declaradas(bc.PACKS / p)}
print(f"declaradas: {len(declaradas)} · usadas: {len(usadas)}")
print("SIN DEMO:", sorted(c for c in declaradas if c not in usadas) or "ninguna ✅")
print("USADAS INEXISTENTES:", sorted(c for c in usadas if c not in existentes) or "ninguna ✅")
