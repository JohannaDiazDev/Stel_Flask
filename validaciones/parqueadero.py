from flask import flash
from datetime import datetime

def validar_datos_parqueadero(form):
    errores = []

    cupo = form['cupo'].strip()
    residente_id = form.get('residente_id') or None
    visitante_id = form.get('visitante_id') or None
    estado = form['estado'].strip()
    fecha = form['fecha'].strip()
    tipo = form['tipo'].strip()
    placa = form['placa'].strip()

    tipos_validos = ['carro', 'moto']
    estados_validos = ['disponible', 'ocupado']
    if not tipo or tipo not in tipos_validos:
        errores.append('Tipo de vehículo inválido.')

    if not estado or estado not in estados_validos:
        errores.append('Estado inválido.')    

    if not placa or len(placa) < 6 or len(placa) > 7:
        errores.append('La placa debe tener entre 6 y 7 caracteres.')

    if not cupo.isdigit():
        errores.append('El cupo debe ser un número.')
    else:
        cupo = int(cupo)
        if tipo == 'carro' and not (1 <= cupo <= 55):
            errores.append('Para carros, el cupo debe estar entre 1 y 55.')
        elif tipo == 'moto' and not (1 <= cupo <= 35):
            errores.append('Para motos, el cupo debe estar entre 1 y 35.')

    if not residente_id and not visitante_id:
        errores.append('Debe seleccionar al menos un residente o un visitante.')

    try:
        entrada = datetime.strptime(fecha, "%Y-%m-%dT%H:%M")
    except ValueError:
        errores.append('La fecha no tiene un formato válido.')

    return errores