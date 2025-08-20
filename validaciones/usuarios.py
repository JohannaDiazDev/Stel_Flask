from flask import flash
import re 

def validar_datos_usuario(form):
    errores = []

    nombre = form['nombre'].strip()
    cedula = form['cedula'].strip()
    celular = form['celular'].strip()
    correo = form['correo'].strip()
    contraseña = form['contraseña'].strip()
    rol_id = form['rol_id'].strip()

    regex_nombre = re.compile(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{3,50}$')
    regex_cedula = re.compile(r'^\d{4,10}$')
    regex_correo = re.compile(r'^[a-zA-Z0-9._%+-]+@(gmail\.com|hotmail\.com|yahoo\.com)$')

    if not regex_nombre.match(nombre):
        errores.append('El nombre debe tener mínimo 3 caracteres.')

    if not regex_cedula.match(cedula):
        errores.append('la cédula debe contener mínimo 4 caracteres.')

    if not celular.isdigit() or len(celular) < 10:
        errores.append('El celular debe tener al menos 10 dígitos.')

    if not regex_correo.match(correo):
        errores.append('Correo Inválido.')       

    if not contraseña:
        errores.append('La contraseña es obligatoria.')

    if not rol_id:
        errores.append('Debe seleccionar un rol.')

    return errores    