# -*- coding: utf-8 -*-
"""Escribe specs/14.json (IA y agentes) y comprueba la cobertura clase↔demo."""
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


d("Panel de conversación completo", ".nz-chat · __head · __title · __status · __body · __foot",
  '<div class="nz-chat"><div class="nz-chat__head"><span class="cat-brandmark" aria-hidden="true"><i></i><i></i></span><span class="nz-chat__title">Asistente de obra</span><span class="nz-chat__status">gpt-4o · 1.240 tokens</span></div><div class="nz-chat__body"><div class="nz-msg nz-msg--user"><div class="nz-msg__body"><span class="nz-msg__author">Tú</span><div class="nz-msg__bubble"><span class="nz-msg__text">Resume el pliego del lote 3.</span></div><span class="nz-msg__time">10:02</span></div></div><div class="nz-msg nz-msg--assistant"><div class="nz-msg__body"><span class="nz-msg__author">Asistente</span><div class="nz-msg__bubble"><span class="nz-msg__text">El lote 3 exige 3 años de experiencia y solvencia de 120.000 €.</span></div><span class="nz-msg__time">10:02</span></div></div></div><div class="nz-chat__foot"><div class="nz-prompt"><button class="nz-prompt__attach" aria-label="Adjuntar">+</button><textarea class="nz-prompt__input" rows="1" placeholder="Escribe tu pregunta…"></textarea><button class="nz-prompt__send">Enviar</button></div></div></div>')

d("Tamaños y variantes del panel", ".nz-chat--sm · --bordered",
  '<div class="nz-stack nz-stack--sm"><div class="nz-chat nz-chat--sm nz-chat--bordered"><div class="nz-chat__head"><span class="nz-chat__title">Chat compacto</span></div><div class="nz-chat__body"><div class="nz-msg"><div class="nz-msg__body"><div class="nz-msg__bubble"><span class="nz-msg__text">Sin sombra, con borde.</span></div></div></div></div></div></div>')

d("Mensajes por rol y estado", ".nz-msg--user · --assistant · --error",
  '<div class="nz-stack nz-stack--sm"><div class="nz-msg nz-msg--assistant"><span class="nz-avatar nz-avatar--sm nz-msg__avatar">IA</span><div class="nz-msg__body"><span class="nz-msg__author">Asistente</span><div class="nz-msg__bubble"><span class="nz-msg__text">He encontrado 12 expedientes.</span></div><div class="nz-msg__actions"><button class="nz-btn nz-btn--ghost nz-btn--sm">Copiar</button><button class="nz-btn nz-btn--ghost nz-btn--sm">Regenerar</button></div></div></div><div class="nz-msg nz-msg--user"><span class="nz-avatar nz-avatar--sm nz-msg__avatar">DA</span><div class="nz-msg__body"><div class="nz-msg__bubble"><span class="nz-msg__text">Muéstrame solo los de Madrid.</span></div><span class="nz-msg__time">hace 1 min</span></div></div><div class="nz-msg nz-msg--error"><div class="nz-msg__body"><div class="nz-msg__bubble"><span class="nz-msg__text">No he podido conectar con la fuente de datos.</span></div></div></div></div>')

d("Cursor de escritura y pensando", ".nz-msg__caret · __caret--on · .nz-thinking · __dot · --2 · --3",
  '<div class="nz-stack nz-stack--sm"><div class="nz-msg nz-msg--assistant"><div class="nz-msg__body"><div class="nz-msg__bubble"><span class="nz-msg__text">Redactando el informe<span class="nz-msg__caret nz-msg__caret--on"></span></span></div></div></div><div class="nz-thinking"><span class="nz-thinking__dot"></span><span class="nz-thinking__dot nz-thinking__dot--2"></span><span class="nz-thinking__dot nz-thinking__dot--3"></span> Pensando…</div></div>')

d("Herramientas usadas", ".nz-toolrow · __chip · __chip--active",
  '<div class="nz-toolrow"><span class="nz-toolrow__chip nz-toolrow__chip--active">buscar_expediente</span><span class="nz-toolrow__chip">leer_pdf</span><span class="nz-toolrow__chip">guardar_nota</span></div>')

d("Llamada a herramienta", ".nz-toolcall · __head · __name · __args · __result · __status · --ok · --error · --running",
  '<div class="nz-stack nz-stack--sm"><div class="nz-toolcall"><div class="nz-toolcall__head"><span class="nz-toolcall__name">buscar_expediente</span><span class="nz-toolcall__status nz-toolcall__status--ok">✓ ok</span></div><div class="nz-toolcall__args">{ "año": 2026, "lote": 3 }</div><div class="nz-toolcall__result">12 resultados en 240 ms</div></div><div class="nz-toolcall"><div class="nz-toolcall__head"><span class="nz-toolcall__name">leer_pdf</span><span class="nz-toolcall__status nz-toolcall__status--running">⋯ en curso</span></div><div class="nz-toolcall__args">{ "ruta": "pliego.pdf" }</div></div><div class="nz-toolcall"><div class="nz-toolcall__head"><span class="nz-toolcall__name">guardar_nota</span><span class="nz-toolcall__status nz-toolcall__status--error">✗ error</span></div><div class="nz-toolcall__args">{ "texto": "…" }</div><div class="nz-toolcall__result">Permiso denegado por política</div></div></div>')

d("Barra de prompt", ".nz-prompt · __input · __attach · __send · __hint",
  '<div><div class="nz-prompt"><button class="nz-prompt__attach" aria-label="Adjuntar archivo">+</button><textarea class="nz-prompt__input" rows="1" placeholder="Pregunta lo que quieras…"></textarea><button class="nz-prompt__send">Enviar</button></div><p class="nz-prompt__hint">Pulsa Intro para enviar · Mayús+Intro para salto de línea</p></div>')

d("Adjuntos", ".nz-attach · __item · __thumb · __name · __remove",
  '<div class="nz-attach"><span class="nz-attach__item"><span class="nz-attach__thumb">PDF</span><span class="nz-attach__name">pliego-lote-3.pdf</span><button class="nz-attach__remove" aria-label="Quitar">✕</button></span><span class="nz-attach__item"><span class="nz-attach__thumb">CSV</span><span class="nz-attach__name">presupuesto.csv</span><button class="nz-attach__remove" aria-label="Quitar">✕</button></span></div>')

d("Selector de modelo", ".nz-modelpick · __btn · __list · __item · __item--active · __meta",
  '<div class="nz-modelpick"><button class="nz-modelpick__btn">modelo: qwen3.8-flash ▾</button><div class="nz-modelpick__list"><span class="nz-modelpick__item nz-modelpick__item--active">qwen3.8-flash<span class="nz-modelpick__meta">rápido</span></span><span class="nz-modelpick__item">glm5.3-flash<span class="nz-modelpick__meta">preciso</span></span><span class="nz-modelpick__item">qwen3-vl<span class="nz-modelpick__meta">visión</span></span></div></div>')

d("Contexto y consumo", ".nz-context-meter · __bar · __fill · __value · --warn · --full · .nz-tokens · __label · __num · __cost",
  '<div class="nz-cluster"><div class="nz-context-meter" style="min-width:12rem"><div class="nz-context-meter__bar"><span class="nz-context-meter__fill" style="width:62%"></span></div><span class="nz-context-meter__value">62% de la ventana</span></div><div class="nz-context-meter nz-context-meter--warn" style="min-width:12rem"><div class="nz-context-meter__bar"><span class="nz-context-meter__fill" style="width:84%"></span></div><span class="nz-context-meter__value">84% · queda poco</span></div><div class="nz-context-meter nz-context-meter--full" style="min-width:12rem"><div class="nz-context-meter__bar"><span class="nz-context-meter__fill" style="width:100%"></span></div><span class="nz-context-meter__value">100% · lleno</span></div><div class="nz-tokens"><span class="nz-tokens__label">tokens</span><span class="nz-tokens__num">12.480</span><span class="nz-tokens__cost">0,018 €</span></div></div>')

d("Plan por pasos", ".nz-taskplan · __step · __num · __label · __detail · --done · --active · --error",
  '<div class="nz-taskplan"><div class="nz-taskplan__step nz-taskplan__step--done"><span class="nz-taskplan__num">1</span><div><span class="nz-taskplan__label">Leer el pliego</span><span class="nz-taskplan__detail">PDF de 42 páginas</span></div></div><div class="nz-taskplan__step nz-taskplan__step--active"><span class="nz-taskplan__num">2</span><div><span class="nz-taskplan__label">Extraer requisitos</span><span class="nz-taskplan__detail">trabajando…</span></div></div><div class="nz-taskplan__step"><span class="nz-taskplan__num">3</span><div><span class="nz-taskplan__label">Redactar informe</span></div></div><div class="nz-taskplan__step nz-taskplan__step--error"><span class="nz-taskplan__num">4</span><div><span class="nz-taskplan__label">Firmar</span><span class="nz-taskplan__detail">sin credenciales</span></div></div></div>')

d("Aprobación humana", ".nz-approval · __title · __body · __actions · --danger",
  '<div class="nz-stack nz-stack--sm"><div class="nz-approval"><span class="nz-approval__title">El agente quiere borrar 3 registros</span><span class="nz-approval__body">Acción irreversible sobre la tabla expedientes_2025.</span><div class="nz-approval__actions"><button class="nz-btn nz-btn--primary nz-btn--sm">Aprobar</button><button class="nz-btn nz-btn--ghost nz-btn--sm">Rechazar</button></div></div><div class="nz-approval nz-approval--danger"><span class="nz-approval__title">Operación bloqueada</span><span class="nz-approval__body">La política prohíbe escrituras en producción.</span><div class="nz-approval__actions"><button class="nz-btn nz-btn--ghost nz-btn--sm">Ver política</button></div></div></div>')

d("Diferencias de código", ".nz-diff · __line · __num · __code · --add · --del · --ctx",
  '<div class="nz-diff"><div class="nz-diff__line nz-diff__line--ctx"><span class="nz-diff__num">10</span><span class="nz-diff__code">function total(a, b) {</span></div><div class="nz-diff__line nz-diff__line--del"><span class="nz-diff__num">11</span><span class="nz-diff__code">-  return a + b</span></div><div class="nz-diff__line nz-diff__line--add"><span class="nz-diff__num">11</span><span class="nz-diff__code">+  return Number(a) + Number(b)</span></div><div class="nz-diff__line nz-diff__line--ctx"><span class="nz-diff__num">12</span><span class="nz-diff__code">}</span></div></div>')

d("Citas y razonamiento", ".nz-cite · __num · __title · __url · __meta · .nz-reason · __summary · __body",
  '<div class="nz-stack nz-stack--sm"><div class="nz-msg nz-msg--assistant"><div class="nz-msg__body"><div class="nz-msg__bubble"><span class="nz-msg__text">El plazo es de 30 días naturales <a class="nz-cite" href="#"><span class="nz-cite__num">1</span><span class="nz-cite__title">Pliego de cláusulas</span></a>.</span></div></div></div><div class="nz-cluster"><a class="nz-cite" href="#"><span class="nz-cite__num">1</span><span class="nz-cite__title">Pliego de cláusulas administrativas</span><span class="nz-cite__url">placsp.gob.es</span><span class="nz-cite__meta">pág. 14</span></a></div><details class="nz-reason"><summary class="nz-reason__summary">Ver razonamiento (3 pasos)</summary><p class="nz-reason__body">Comprobé el plazo en dos fuentes, descarté la fecha de publicación por ser festivo local y apliqué el cómputo desde el día siguiente.</p></details></div>')

d("Tarjeta de agente", ".nz-agent-card · __row · __name · __role · __state · --idle · --busy · --error · __caps · __cap",
  '<div class="nz-stack nz-stack--sm"><div class="nz-agent-card"><div class="nz-agent-card__row"><span class="nz-avatar nz-avatar--sm nz-avatar--accent">EX</span><span class="nz-agent-card__name">Extractor</span><span class="nz-agent-card__role">lectura de pliegos</span><span class="nz-agent-card__state nz-agent-card__state--busy"><i></i>trabajando</span></div><div class="nz-agent-card__caps"><span class="nz-agent-card__cap">pdf</span><span class="nz-agent-card__cap">ocr</span><span class="nz-agent-card__cap">tablas</span></div></div><div class="nz-agent-card"><div class="nz-agent-card__row"><span class="nz-avatar nz-avatar--sm">RE</span><span class="nz-agent-card__name">Redactor</span><span class="nz-agent-card__role">informes</span><span class="nz-agent-card__state nz-agent-card__state--idle"><i></i>en espera</span></div><div class="nz-agent-card__caps"><span class="nz-agent-card__cap">markdown</span><span class="nz-agent-card__cap">citas</span></div></div><div class="nz-agent-card"><div class="nz-agent-card__row"><span class="nz-avatar nz-avatar--sm">VA</span><span class="nz-agent-card__name">Validador</span><span class="nz-agent-card__role">QA</span><span class="nz-agent-card__state nz-agent-card__state--error"><i></i>caído</span></div></div></div>')

d("Registro de ejecución", ".nz-runlog · __line · __time · __level--info · --warn · --error · __msg",
  '<div class="nz-runlog"><div class="nz-runlog__line"><span class="nz-runlog__time">10:02:11</span><span class="nz-runlog__level--info">INFO</span><span class="nz-runlog__msg">run iniciado (agente=extractor)</span></div><div class="nz-runlog__line"><span class="nz-runlog__time">10:02:14</span><span class="nz-runlog__level--warn">WARN</span><span class="nz-runlog__msg">pdf sin capa de texto, se usa OCR</span></div><div class="nz-runlog__line"><span class="nz-runlog__time">10:02:19</span><span class="nz-runlog__level--error">ERROR</span><span class="nz-runlog__msg">timeout al guardar la nota</span></div></div>')

d("Puntuación de evaluación", ".nz-score · __bar · __fill · __value · __label · __verdict · --low",
  '<div class="nz-cluster"><div class="nz-score" style="min-width:12rem"><span class="nz-score__value">0,92</span><span class="nz-score__label">precisión de la extracción</span><div class="nz-score__bar"><span class="nz-score__fill" style="width:92%"></span></div><span class="nz-score__verdict">aprobado</span></div><div class="nz-score nz-score--low" style="min-width:12rem"><span class="nz-score__value">0,41</span><span class="nz-score__label">cobertura de citas</span><div class="nz-score__bar"><span class="nz-score__fill" style="width:41%"></span></div><span class="nz-score__verdict">por debajo del umbral</span></div></div>')

d("Guardarraíl y retroalimentación", ".nz-guardrail · __icon · __title · __msg · --block · .nz-feedback · __btn · __btn--on",
  '<div class="nz-stack nz-stack--sm"><div class="nz-guardrail"><span class="nz-guardrail__icon">⚠</span><div><span class="nz-guardrail__title">Datos personales detectados</span><span class="nz-guardrail__msg">Se ha anonimizado el DNI antes de enviarlo al modelo.</span></div></div><div class="nz-guardrail nz-guardrail--block"><span class="nz-guardrail__icon">⛔</span><div><span class="nz-guardrail__title">Petición bloqueada</span><span class="nz-guardrail__msg">La política impide enviar credenciales a un modelo externo.</span></div></div><div class="nz-feedback"><button class="nz-feedback__btn nz-feedback__btn--on" aria-label="Buena respuesta">▲</button><button class="nz-feedback__btn" aria-label="Mala respuesta">▼</button></div></div>')

d("Plantilla de prompt", ".nz-ptemplate · __var · __block · __preview",
  '<div><div class="nz-ptemplate">Resume el <span class="nz-ptemplate__var">{{documento}}</span> en 5 puntos.<span class="nz-ptemplate__block">{{#si hay tablas}}</span> Incluye los importes.<span class="nz-ptemplate__block">{{/si}}</span></div><p class="nz-ptemplate__preview">Vista previa con documento=pliego.pdf → «Resume el pliego.pdf en 5 puntos. Incluye los importes.»</p></div>')

d("Estado del flujo", ".nz-stream-status · __dot · --live · --done · --stopped",
  '<div class="nz-cluster"><span class="nz-stream-status nz-stream-status--live"><i class="nz-stream-status__dot"></i>generando</span><span class="nz-stream-status nz-stream-status--done"><i class="nz-stream-status__dot"></i>completo</span><span class="nz-stream-status nz-stream-status--stopped"><i class="nz-stream-status__dot"></i>detenido</span></div>')

d("Rejilla de vectores", ".nz-embed-grid · __cell · __cell--1..4 · __label",
  '<div><div class="nz-embed-grid"><span class="nz-embed-grid__cell nz-embed-grid__cell--1"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--3"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--4"></span><span class="nz-embed-grid__cell"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--2"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--4"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--1"></span><span class="nz-embed-grid__cell"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--2"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--3"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--4"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--1"></span><span class="nz-embed-grid__cell"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--2"></span><span class="nz-embed-grid__cell nz-embed-grid__cell--3"></span><span class="nz-embed-grid__cell"></span></div><span class="nz-embed-grid__label">Similitud de 16 fragmentos del pliego</span></div>')

d("Grafo de conocimiento", ".nz-kgraph · __svg · __edge · __node · --brand · --accent · --muted · __label",
  '<div class="nz-kgraph"><svg class="nz-kgraph__svg" viewBox="0 0 200 120" role="img" aria-label="Grafo de conocimiento"><line class="nz-kgraph__edge" x1="100" y1="60" x2="40" y2="30"></line><line class="nz-kgraph__edge" x1="100" y1="60" x2="160" y2="30"></line><line class="nz-kgraph__edge" x1="100" y1="60" x2="60" y2="100"></line><line class="nz-kgraph__edge" x1="100" y1="60" x2="150" y2="95"></line><circle class="nz-kgraph__node nz-kgraph__node--brand" cx="100" cy="60" r="12"></circle><circle class="nz-kgraph__node nz-kgraph__node--accent" cx="40" cy="30" r="8"></circle><circle class="nz-kgraph__node nz-kgraph__node--accent" cx="160" cy="30" r="8"></circle><circle class="nz-kgraph__node nz-kgraph__node--muted" cx="60" cy="100" r="6"></circle><circle class="nz-kgraph__node" cx="150" cy="95" r="6"></circle><text class="nz-kgraph__label" x="100" y="84">Pliego</text><text class="nz-kgraph__label" x="18" y="24">Lote 3</text></svg></div>')

d("Comparador de dos respuestas", ".nz-model-compare · __side · --a · --b · __head · __body · __foot",
  '<div class="nz-model-compare"><div class="nz-model-compare__side nz-model-compare__side--a"><span class="nz-model-compare__head">qwen3.8-flash</span><p class="nz-model-compare__body">El plazo es de 30 días naturales desde la publicación.</p><span class="nz-model-compare__foot">1,2 s · 0,004 €</span></div><div class="nz-model-compare__side nz-model-compare__side--b"><span class="nz-model-compare__head">glm5.3-flash</span><p class="nz-model-compare__body">Existen 30 días naturales, computados desde el día siguiente a la publicación del anuncio.</p><span class="nz-model-compare__foot">2,8 s · 0,011 €</span></div></div>')

d("Cuota de uso", ".nz-cuota · __bar · __fill · __value · __reset · --warn · --full",
  '<div class="nz-stack nz-stack--sm"><div class="nz-cuota"><div class="nz-cuota__bar"><span class="nz-cuota__fill" style="width:38%"></span></div><span class="nz-cuota__value">38% de la cuota mensual</span><span class="nz-cuota__reset">Se renueva el 1 de octubre</span></div><div class="nz-cuota nz-cuota--warn"><div class="nz-cuota__bar"><span class="nz-cuota__fill" style="width:82%"></span></div><span class="nz-cuota__value">82% · vigila el gasto</span></div><div class="nz-cuota nz-cuota--full"><div class="nz-cuota__bar"><span class="nz-cuota__fill" style="width:100%"></span></div><span class="nz-cuota__value">100% · agotada</span></div></div>')

d("Historial de conversaciones", ".nz-chat-history · __title · __item · __item--active · __time",
  '<div class="nz-chat-history"><span class="nz-chat-history__title">Recientes</span><a class="nz-chat-history__item nz-chat-history__item--active" href="#">Pliego lote 3<span class="nz-chat-history__time">10:02</span></a><a class="nz-chat-history__item" href="#">Presupuesto obra<span class="nz-chat-history__time">ayer</span></a><a class="nz-chat-history__item" href="#">Normativa CTE<span class="nz-chat-history__time">lunes</span></a></div>')

d("Chat vacío con sugerencias", ".nz-chat__empty · __suggests · __suggest · .nz-chat-empty · __icon · __title · __text · __suggests",
  '<div class="nz-stack nz-stack--sm"><div class="nz-chat nz-chat--sm"><div class="nz-chat__empty"><b>Empieza una conversación</b><span>Pregunta lo que necesites sobre los pliegos.</span><div class="nz-chat__suggests"><button class="nz-chat__suggest">Resume un pliego</button><button class="nz-chat__suggest">Compara dos lotes</button><button class="nz-chat__suggest">Busca por importe</button></div></div></div><div class="nz-chat-empty"><span class="nz-chat-empty__icon">◈</span><span class="nz-chat-empty__title">Tu asistente de licitaciones</span><p class="nz-chat-empty__text">Lee pliegos, extrae requisitos y redacta borradores con citas verificables.</p><div class="nz-chat-empty__suggests"><button class="nz-chat__suggest">Ver ejemplo</button><button class="nz-chat__suggest">Cómo funciona</button></div></div></div>')

spec = {
    "cat": 14,
    "nombre": "IA y agentes",
    "desc": "Conversación, streaming, herramientas, aprobación humana, diferencias, citas, razonamiento, agentes, ejecuciones, evaluación y coste. La interfaz de la IA sin brillos ni humo: jerarquía, estado y control.",
    "pack": "p14-ai.css",
    "fichero": "14-ai.html",
    "demos": D,
}

(ROOT / "specs" / "14.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"specs/14.json escrito · {len(D)} demos")

declaradas = bc.clases_declaradas(ROOT / "packs" / "p14-ai.css")
usadas = set()
for demo in D:
    usadas |= bc.clases_de_markup(demo["markup"])
existentes = {c for p in bc.PACKS_COMPONENTES if (bc.PACKS / p).exists()
              for c in bc.clases_declaradas(bc.PACKS / p)}
faltan = sorted(c for c in declaradas if c not in usadas)
sobran = sorted(c for c in usadas if c not in existentes)
print(f"declaradas: {len(declaradas)} · usadas: {len(usadas)}")
print("SIN DEMO:", faltan if faltan else "ninguna ✅")
print("USADAS INEXISTENTES:", sobran if sobran else "ninguna ✅")
