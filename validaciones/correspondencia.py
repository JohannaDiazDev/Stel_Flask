from flask import flash
from datetime import datetime

def validar_datos_correspondencia(form):
    errores = []

    inmueble_id = form.get('inmueble_id').strip()
    descripcion = form.get('descripcion', '').strip()


    if not inmueble_id or not inmueble_id.isdigit():
        errores.append('Debe seleccionar un inmueble.')

    if not descripcion or len(descripcion) < 3 or len(descripcion) > 200:
        errores.append('La descripción debe tener entre 3 y 200 caracteres.')

    return errores

def validar_edicion_correspondencia(form):
    errores = []

    descripcion = form.get('descripcion','')
    estado = form.get('estado','')
    fecha_entrega = form.get('fecha_entrega','')
    fecha_recibido = form.get('fecha_recibido','')

    if not descripcion or len(descripcion) < 3 or len(descripcion) > 200:
        errores.append('La descripción debe tener entre 3 y 200 caracteres.')

    if estado not in ['Entregado', 'No Entregado']:
        errores.append('Estado inválido.')

    if fecha_entrega and fecha_recibido:
        try:
            f_entrega = datetime.strptime(fecha_entrega, '%Y-%m-%dT%H:%M')
            f_recibido = datetime.strptime(fecha_recibido, '%Y-%m-%dT%H:%M')
            if f_entrega < f_recibido:
                errores.append('La fecha de entrega no puede ser anterior a la fecha de recibido.')
        except ValueError:
            errores.append('Formato de fecha inválido.')

    return errores                    

