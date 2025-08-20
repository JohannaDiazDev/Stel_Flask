from flask import flash
from datetime import datetime

def validar_datos_novedad(form):
    errores = []

    trabajador_id = form.get('trabajador_id')
    fecha = form.get('fecha', '').strip()
    inmueble_id = form.get('inmueble_id') or None
    tipo = form.get('tipo', '').strip()
    asunto = form.get('asunto', '').strip()
    descripcion = form.get('descripcion', '').strip()
    estado = form.get('estado', '').strip()

    tipos_validos = ['Solicitud', 'Queja', 'Reporte']
    estados_validos = ['Pendiente', 'Proceso', 'Resuelto']

    if not trabajador_id:
        errores.append('Debe seleccionar un trabajador.')

    if not fecha:
        errores.append('Debe ingresar una fecha.')
    else:
        try:
            datetime.strptime(fecha, '%Y-%m-%dT%H:%M') 
        except ValueError:
            errores.append('La fecha no tiene un formato válido.')

    if not tipo or tipo not in tipos_validos:
        errores.append('Debe seleccionar un tipo válido.')

    if not asunto or len(asunto) < 5 or len(asunto) > 100:
        errores.append('El asunto debe tener entre 5 y 100 caracteres.')

    if not descripcion or len(descripcion) < 10 or len(descripcion) > 500:
        errores.append('La descripción debe tener entre 10 y 500 caracteres.')

    if not estado or estado not in estados_validos:
        errores.append('Debe seleccionar un estado válido.')

    return errores    