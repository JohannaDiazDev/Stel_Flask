import re
from flask import flash
from datetime import datetime

def validar_datos_visitante(form):
    errores = []

    fecha = form.get('fecha', '').strip()
    inmueble_id = form.get('inmueble_id', '').strip()
    autorizado = form.get('autorizado', '').strip()
    nombre = form.get('nombre', '').strip()
    cedula = form.get('cedula', '').strip()
    carro = form.get('ingresa_carro', '').strip()

    # nombre
    if not re.match(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{3,50}$', nombre):
        errores.append('El nombre debe tener entre 3 y 50 letras.')

    # cédula
    if not cedula.isdigit() or not (4 <= len(cedula) <= 10):
        errores.append('La cédula debe tener entre 4 y 10 dígitos.')

    # fecha formato
    if not fecha:
        errores.append('Debe ingresar una fecha.')
    else:
        try:
            datetime.strptime(fecha, '%Y-%m-%dT%H:%M') 
        except ValueError:
            errores.append('La fecha no tiene un formato válido.')

    # inmueble
    if not inmueble_id or not inmueble_id.isdigit():
        errores.append('Debe seleccionar un inmueble válido.')

   
    if autorizado not in ['Si', 'No']:
        errores.append('Debe indicar si el ingreso es autorizado.')

    if carro not in ['Si', 'No']:
        errores.append('Debe seleccionar si ingresa con carro.')

    return errores
