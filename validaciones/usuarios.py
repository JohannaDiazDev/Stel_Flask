from flask import flash
import re

def validar_datos_usuario(form):
    errores = {}

    nombre = form.get('nombre', '').strip()
    cedula = form.get('cedula', '').strip()
    celular = form.get('celular', '').strip()
    correo = form.get('correo', '').strip()
    password = form.get('password', '').strip()
    rol_id = form.get('rol_id', '').strip()

    regex_nombre = re.compile(r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{3,50}$')
    regex_cedula = re.compile(r'^\d{4,10}$')
    regex_correo = re.compile(r'^[a-zA-Z0-9._%+-]+@(gmail\.com|hotmail\.com|yahoo\.com)$')
    regex_celular = re.compile(r'^3\d{9}$')
    regex_password = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$')

    if not regex_nombre.match(nombre):
        errores["nombre"] = 'El nombre debe tener mínimo 3 caracteres.'

    if not regex_cedula.match(cedula):
        errores["cedula"] = 'La cédula debe contener entre 4 y 10 dígitos.'

    if not regex_celular.match(celular):
        errores["celular"] = 'El celular debe tener 10 dígitos y comenzar por 3.'

    if not regex_correo.match(correo):
        errores["correo"] = 'Correo inválido. Solo Gmail, Hotmail o Yahoo.'

    if password and not regex_password.match(password):
        errores["password"] = (
            'La contraseña debe tener mínimo 8 caracteres, '
            'incluyendo mayúscula, minúscula, número y un carácter especial.'
        )

    if not rol_id:
        errores["rol_id"] = 'Debe seleccionar un rol.'

    return errores
