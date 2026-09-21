# -*- coding: utf-8 -*-
"""Tanda B de ampliacion: p15-apps, p12-system, p11-social (CSS + demos en specs)."""
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


# ============ p15-apps.css ============
css_add('packs/p15-apps.css', '''

/* ============================================================
   Estados de ventanas, kanban, agenda y dock (lexico cerrado)  */
.nz-window.is-active { border-color: var(--nz-brand); box-shadow: var(--nz-shadow-xl); }
.nz-window.is-max { border-radius: 0; }
.nz-window.is-error { border-color: var(--nz-danger); }
.nz-window--sm { max-width: 24rem; }
.nz-window--lg { max-width: 64rem; }
.nz-kanban__col.is-over { border-color: var(--nz-brand); border-style: dashed; background: var(--nz-brand-soft); }
.nz-kanban__col.is-done { border-color: var(--nz-success); background: var(--nz-success-soft); }
.nz-kanban__card.is-selected { box-shadow: 0 0 0 2px var(--nz-brand), var(--nz-shadow-xs); }
.nz-kanban__card.is-error { border-left-color: var(--nz-danger); }
.nz-agenda__slot.is-now { background: var(--nz-brand-soft); }
.nz-agenda__slot.is-busy { background: var(--nz-bg-soft); }
.nz-dock--sm .nz-dock__item { min-width: 36px; min-height: 36px; font-size: var(--nz-text-sm); }
.nz-dock--lg .nz-dock__item { min-width: 56px; min-height: 56px; font-size: var(--nz-text-lg); }
.nz-dock__item.is-active { background: var(--nz-brand-soft); color: var(--nz-brand); }
''', 'nz-kanban__col.is-over')

# ============ p12-system.css ============
css_add('packs/p12-system.css', '''

/* ============================================================
   Severidad de incidencias (lexico cerrado)                    */
.nz-incident--danger .nz-incident__tag { background: var(--nz-danger-soft); color: var(--nz-danger); }
.nz-incident--warning .nz-incident__tag { background: var(--nz-warning-soft); color: var(--nz-warning); }
.nz-incident--success .nz-incident__tag { background: var(--nz-success-soft); color: var(--nz-success); }
''', 'nz-incident--danger')

# ============ p11-social.css ============
css_add('packs/p11-social.css', '''

/* ============================================================
   Destacados y tono de notificaciones (lexico cerrado)         */
.nz-activity__item.is-highlight { background: var(--nz-brand-soft); border-radius: var(--nz-radius-md); padding-inline: var(--nz-space-3); }
.nz-notif--success { box-shadow: inset 3px 0 0 var(--nz-success), var(--nz-shadow-md); }
.nz-notif--danger { box-shadow: inset 3px 0 0 var(--nz-danger), var(--nz-shadow-md); }
.nz-notif--warning { box-shadow: inset 3px 0 0 var(--nz-warning), var(--nz-shadow-md); }
.nz-team--sm .nz-team__avatar { width: 48px; height: 48px; }
.nz-team--lg .nz-team__avatar { width: 112px; height: 112px; }
''', 'nz-activity__item.is-highlight')

# ============ Demos ============
slot = lambda h, txt, cls='': (f'<div class="nz-agenda__slot{cls}"><span>{h}</span><div>{txt}</div></div>')
win = lambda t, cls='': (f'<div class="nz-window{cls}"><div class="nz-window__titlebar"><strong>{t}</strong></div>'
                         '<div class="nz-window__body"><p>Contenido de la ventana.</p></div></div>')
card = lambda t, cls='': f'<div class="nz-kanban__card{cls}">{t}</div>'

agregar(15, [
    {"titulo": "Ventana · estados y tamaño", "tag": ".nz-window.is-active / .is-max / --sm",
     "markup": win("Normal") + win("Activa", " is-active") + win("nota.txt", " nz-window--sm is-error")},
    {"titulo": "Kanban · destino de arrastre y columna resuelta", "tag": ".nz-kanban__col.is-over / .is-done",
     "markup": ('<div class="nz-kanban"><div class="nz-kanban__col"><strong>Por hacer</strong>' + card("Revisar copys") + '</div>'
                '<div class="nz-kanban__col is-over"><strong>Soltar aqui</strong>' + card("Maquetar hero") + '</div>'
                '<div class="nz-kanban__col is-done"><strong>Hecho</strong>' + card("Redactar brief") + '</div></div>')},
    {"titulo": "Kanban · tarjeta seleccionada y con error", "tag": ".nz-kanban__card.is-selected / .is-error",
     "markup": card("Tarea seleccionada", " is-selected") + card("Tarea bloqueada", " is-error")},
    {"titulo": "Agenda · franja actual y ocupada", "tag": ".nz-agenda__slot.is-now / .is-busy",
     "markup": ('<div class="nz-agenda">' + slot("09:00", "Reunion de equipo", " is-busy")
                + slot("10:00", "Ahora mismo", " is-now") + slot("11:00", "Libre") + '</div>')},
    {"titulo": "Dock · tamaño y elemento activo", "tag": ".nz-dock--sm / --lg / __item.is-active",
     "markup": ('<div class="nz-dock nz-dock--sm"><a class="nz-dock__item" href="#">A</a>'
                '<a class="nz-dock__item is-active" href="#">B</a><a class="nz-dock__item" href="#">C</a></div>'
                '<div class="nz-dock nz-dock--lg"><a class="nz-dock__item" href="#">A</a>'
                '<a class="nz-dock__item" href="#">B</a><a class="nz-dock__item is-active" href="#">C</a></div>')},
])

agregar(12, [
    {"titulo": "Incidencia · severidad", "tag": ".nz-incident--danger / --warning / --success",
     "markup": ('<div class="nz-incident nz-incident--danger"><span class="nz-incident__tag">critica</span>'
                '<span class="nz-incident__title">API de pagos caida</span><time class="nz-incident__time">10:42</time>'
                '<p class="nz-incident__body">Sin respuesta desde el 10:31.</p></div>'
                '<div class="nz-incident nz-incident--warning"><span class="nz-incident__tag">degradada</span>'
                '<span class="nz-incident__title">Latencia x4 en busqueda</span><time class="nz-incident__time">11:05</time>'
                '<p class="nz-incident__body">Se investiga el cluster de indices.</p></div>'
                '<div class="nz-incident nz-incident--success"><span class="nz-incident__tag">resuelta</span>'
                '<span class="nz-incident__title">Cola de emails vaciada</span><time class="nz-incident__time">11:20</time>'
                '<p class="nz-incident__body">Retardo en cero.</p></div>')},
])

agregar(11, [
    {"titulo": "Actividad · item destacado", "tag": ".nz-activity__item.is-highlight",
     "markup": ('<div class="nz-activity"><div class="nz-activity__item"><span class="nz-activity__icon" aria-hidden="true">*</span>'
                '<div>Maria ha comentado tu publicacion</div><time class="nz-activity__time">2h</time></div>'
                '<div class="nz-activity__item is-highlight"><span class="nz-activity__icon" aria-hidden="true">*</span>'
                '<div>Tu repo alcanza 100 stars</div><time class="nz-activity__time">ahora</time></div></div>')},
    {"titulo": "Notificacion · tono semantico", "tag": ".nz-notif--success / --danger / --warning",
     "markup": ('<div class="nz-notif nz-notif--success">Pago de 49 EUR recibido</div>'
                '<div class="nz-notif nz-notif--danger">El envio 2841 ha fallado</div>'
                '<div class="nz-notif nz-notif--warning">El certificado caduca en 7 dias</div>')},
])

print('TANDA B COMPLETA')
