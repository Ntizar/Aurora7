# -*- coding: utf-8 -*-
"""Tanda A de ampliacion: p14-ai, p5-forms, p6-feedback (CSS + demos en specs)."""
import re, json, pathlib

# ============ p14-ai.css ============
css14 = pathlib.Path('packs/p14-ai.css').read_text(encoding='utf-8')
bloque14 = '''

/* ============================================================
   Variantes de tono y estado (lexico cerrado)                  */
.nz-msg--usuario .nz-msg__bubble { background: var(--nz-brand-soft); border-color: var(--nz-brand); }
.nz-msg--asistente .nz-msg__bubble { background: var(--nz-surface); }
.nz-msg--neutral .nz-msg__bubble { background: var(--nz-bg-inset); }
.nz-msg--danger .nz-msg__bubble { background: var(--nz-danger-soft); border-color: var(--nz-danger); }
.nz-msg--success .nz-msg__bubble { background: var(--nz-success-soft); border-color: var(--nz-success); }
.nz-toolcall.is-error { border-color: var(--nz-danger); background: var(--nz-danger-soft); }
.nz-toolcall.is-done { border-color: var(--nz-success); }
.nz-approval.is-done { border-color: var(--nz-success); background: var(--nz-success-soft); }
.nz-approval.is-rejected { border-color: var(--nz-danger); background: var(--nz-danger-soft); }
.nz-attach__item.is-error { color: var(--nz-danger); }
.nz-attach__item.is-uploading { color: var(--nz-text-mute); }
.nz-chat--compacto .nz-chat__body { gap: var(--nz-space-2); padding: var(--nz-space-2) var(--nz-space-3); }
.nz-chat--compacto .nz-msg { gap: var(--nz-space-2); }
.nz-chat--compacto .nz-msg__bubble { padding: var(--nz-space-2) var(--nz-space-3); font-size: var(--nz-text-sm); }
'''
if 'nz-chat--compacto' not in css14:
    pathlib.Path('packs/p14-ai.css').write_text(css14 + bloque14, encoding='utf-8')
    print('p14-ai.css: +14 reglas')

# ============ p5-forms.css ============
css5 = pathlib.Path('packs/p5-forms.css').read_text(encoding='utf-8')
bloque5 = '''

/* ============================================================
   Variantes de fieldset y estado de subida (lexico cerrado)    */
.nz-fieldset--compact { gap: var(--nz-space-2); padding: var(--nz-space-3); }
.nz-fieldset--spacious { gap: var(--nz-space-5); padding: var(--nz-space-6); }
.nz-fieldset--inline { flex-direction: row; flex-wrap: wrap; align-items: end; }
.nz-fieldset--plain { background: transparent; border-color: transparent; padding-inline: 0; }
.nz-fieldset--danger { border-color: var(--nz-danger); background: var(--nz-danger-soft); }
.nz-password.is-revealed .nz-password__toggle { color: var(--nz-brand); }
.nz-filezona.is-error { border-color: var(--nz-danger); background: var(--nz-danger-soft); color: var(--nz-danger); }
.nz-filezona.is-success { border-color: var(--nz-success); background: var(--nz-success-soft); color: var(--nz-success); }
'''
if 'nz-fieldset--compact' not in css5:
    pathlib.Path('packs/p5-forms.css').write_text(css5 + bloque5, encoding='utf-8')
    print('p5-forms.css: +8 reglas')

# ============ p6-feedback.css ============
css6 = pathlib.Path('packs/p6-feedback.css').read_text(encoding='utf-8')
bloque6 = '''

/* ============================================================
   Tono semantico de contadores, cargas y estados               */
.nz-countdown--warning { background: var(--nz-warning-soft); color: var(--nz-warning); }
.nz-countdown--danger { background: var(--nz-danger-soft); color: var(--nz-danger); }
.nz-countdown--success { background: var(--nz-success-soft); color: var(--nz-success); }
.nz-countdown--flat { background: transparent; padding-inline: 0; }
.nz-errorstate--neutral { background: var(--nz-bg-soft); }
.nz-errorstate--warning { background: var(--nz-warning-soft); }
.nz-loading-bar__bar--brand { background: var(--nz-brand); }
.nz-loading-bar__bar--success { background: var(--nz-success); }
.nz-loading-bar__bar--warning { background: var(--nz-warning); }
.nz-loading-bar__bar--danger { background: var(--nz-danger); }
'''
if 'nz-loading-bar__bar--brand' not in css6:
    pathlib.Path('packs/p6-feedback.css').write_text(css6 + bloque6, encoding='utf-8')
    print('p6-feedback.css: +10 reglas')


# ============ Demos en specs ============
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


def msg(tono):
    return ('<div class="nz-msg nz-msg--' + tono + '"><span class="nz-msg__avatar" aria-hidden="true"></span>'
            '<div class="nz-msg__body"><div class="nz-msg__author">' + tono + '</div>'
            '<div class="nz-msg__bubble"><p class="nz-msg__text">Mensaje de ejemplo con tono ' + tono + '.</p>'
            '</div></div></div>')


agregar(14, [
    {"titulo": "Mensaje · tono del interlocutor", "tag": ".nz-msg--usuario / --asistente / --danger",
     "markup": msg("usuario") + msg("asistente") + msg("danger")},
    {"titulo": "Herramienta · estados", "tag": ".nz-toolcall.is-done / .is-error",
     "markup": ('<div class="nz-toolcall is-done"><div class="nz-toolcall__head"><span class="nz-toolcall__name">buscar</span>'
                '<span class="nz-toolcall__status nz-toolcall__status--ok">completado</span></div>'
                '<div class="nz-toolcall__result">12 resultados</div></div>'
                '<div class="nz-toolcall is-error"><div class="nz-toolcall__head"><span class="nz-toolcall__name">escribir_fichero</span>'
                '<span class="nz-toolcall__status nz-toolcall__status--error">error</span></div>'
                '<div class="nz-toolcall__result">Permiso denegado</div></div>')},
    {"titulo": "Aprobacion · resuelta y rechazada", "tag": ".nz-approval.is-done / .is-rejected",
     "markup": ('<div class="nz-approval is-done"><h4>Ejecutar migracion</h4><p>Aprobada hace 2 min.</p>'
                '<div class="nz-msg__actions"><span class="nz-btn nz-btn--sm nz-btn--success">Aprobada</span></div></div>'
                '<div class="nz-approval is-rejected"><h4>Borrar ficheros</h4><p>Rechazada por el usuario.</p>'
                '<div class="nz-msg__actions"><span class="nz-btn nz-btn--sm nz-btn--danger">Rechazada</span></div></div>')},
    {"titulo": "Adjuntos · estado", "tag": ".nz-attach__item.is-uploading / .is-error",
     "markup": ('<div class="nz-stack"><span class="nz-attach__item is-uploading">informe.pdf · subiendo</span>'
                '<span class="nz-attach__item is-error">foto.png · fallo</span></div>')},
    {"titulo": "Chat compacto", "tag": ".nz-chat--compacto",
     "markup": ('<div class="nz-chat nz-chat--compacto"><div class="nz-chat__head"><span class="nz-chat__title">Soporte</span>'
                '<span class="nz-chat__status">en linea</span></div><div class="nz-chat__body">'
                + msg("usuario") + msg("asistente") + '</div></div>')},
])

agregar(5, [
    {"titulo": "Fieldset · densidad y disposicion", "tag": ".nz-fieldset--compact / --spacious / --inline / --plain",
     "markup": ('<div class="nz-fieldset--compact nz-fieldset"><label class="nz-label" for="c1">Compacto</label>'
                '<input class="nz-input nz-input--sm" id="c1"></div>'
                '<div class="nz-fieldset--spacious nz-fieldset"><label class="nz-label" for="c2">Amplio</label>'
                '<input class="nz-input" id="c2"></div>'
                '<div class="nz-fieldset--inline nz-fieldset"><label class="nz-label" for="c3">Ciudad</label>'
                '<input class="nz-input nz-input--sm" id="c3"></div>'
                '<div class="nz-fieldset--plain nz-fieldset"><label class="nz-label" for="c4">Plano</label>'
                '<input class="nz-input" id="c4"></div>')},
    {"titulo": "Fieldset semantico", "tag": ".nz-fieldset--danger",
     "markup": ('<div class="nz-fieldset--danger nz-fieldset"><span class="nz-fieldset__leyenda">Datos fiscales</span>'
                '<input class="nz-input nz-input--error" aria-invalid="true" value="X-9321"></div>')},
    {"titulo": "Contrasena · revelada", "tag": ".nz-password.is-revealed",
     "markup": ('<div class="nz-password is-revealed"><input class="nz-input" type="text" value="Secreta-1234">'
                '<button class="nz-password__toggle" type="button" aria-label="Ocultar">Ocultar</button></div>')},
    {"titulo": "Zona de archivos · resultado", "tag": ".nz-filezona.is-error / .is-success",
     "markup": ('<div class="nz-filezona is-success"><span class="nz-filezona__icono" aria-hidden="true">OK</span>'
                '<span class="nz-filezona__texto">plan.pdf cargado</span></div>'
                '<div class="nz-filezona is-error"><span class="nz-filezona__icono" aria-hidden="true">X</span>'
                '<span class="nz-filezona__texto">modelo.obj supera 10 MB</span></div>')},
])

agregar(6, [
    {"titulo": "Cuenta atras · tono", "tag": ".nz-countdown--warning / --danger / --success / --flat",
     "markup": ('<div class="nz-stack"><span class="nz-countdown nz-countdown--warning"><strong>05:00</strong> restantes</span>'
                '<span class="nz-countdown nz-countdown--danger"><strong>00:30</strong> restantes</span>'
                '<span class="nz-countdown nz-countdown--success"><strong>00:00</strong> cerrado</span>'
                '<span class="nz-countdown nz-countdown--flat"><strong>12:45</strong></span></div>')},
    {"titulo": "Estado de error · tono", "tag": ".nz-errorstate--neutral / --warning",
     "markup": ('<div class="nz-errorstate nz-errorstate--neutral"><h3>Sin conexion</h3><p>Revisa tu red y reintenta.</p></div>'
                '<div class="nz-errorstate nz-errorstate--warning"><h3>Limite cerca</h3>'
                '<p>Queda el 10% del almacenamiento.</p></div>')},
    {"titulo": "Barra de carga · tono", "tag": ".nz-loading-bar__bar--brand / --success / --warning / --danger",
     "markup": ('<div class="nz-stack"><div class="nz-loading-bar" role="progressbar">'
                '<div class="nz-loading-bar__bar nz-loading-bar__bar--brand"></div></div>'
                '<div class="nz-loading-bar" role="progressbar"><div class="nz-loading-bar__bar nz-loading-bar__bar--success"></div></div>'
                '<div class="nz-loading-bar" role="progressbar"><div class="nz-loading-bar__bar nz-loading-bar__bar--warning"></div></div>'
                '<div class="nz-loading-bar" role="progressbar"><div class="nz-loading-bar__bar nz-loading-bar__bar--danger"></div></div></div>')},
])

print('TANDA A COMPLETA')
