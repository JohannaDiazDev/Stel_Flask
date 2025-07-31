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
    ingresa_carro = form.get('ingresa_carro', '').strip()

    # Validar nombre
    if not nombre or not nombre.replace(" ", "").isalpha() or len(nombre) < 3 or len(nombre) > 50:
        errores.append('El nombre debe tener entre 3 y 50 letras.')

    # Validar cédula
    if not cedula.isdigit() or not (4 <= len(cedula) <= 10):
        errores.append('La cédula debe tener entre 4 y 10 dígitos.')

    # Validar fecha es hoy
    try:
        entrada = datetime.strptime(fecha, "%Y-%m-%dT%H:%M")
    except ValueError:
        errores.append('La fecha no tiene un formato válido.')

    # Validar selectores
    if not inmueble_id:
        errores.append('Debe seleccionar un inmueble.')

    if not autorizado:
        errores.append('Debe indicar quién autorizó.')

    if not ingresa_carro:
        errores.append('Debe seleccionar si ingresa con carro.')

    return errores