from datetime import datetime

def _parse_dt(s):
    for fmt in ('%Y-%m-%dT%H:%M', '%Y-%m-%d'):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    raise ValueError('Formato inválido')

def validar_datos_multa(form):
    errores = {}

    fecha = form.get('fecha', '').strip()
    inmueble_id = form.get('inmueble_id')
    tipo = form.get('tipo', '').strip()
    valor = form.get('valor', '').strip()
    trabajador_id = form.get('trabajador_id')
    fecha_pago = form.get('fecha_pago', '').strip()

    tipos_validos = [
        "Ruido Excesivo", "Estacionamiento indebido", "Mascota sin correa",
        "Problemas con los vecinos", "Daños a zonas comunes",
        "Problemas con mascotas", "Inasistencia asamblea", "Carro rayado"
    ]

    # fecha obligatoria
    if not fecha:
        errores["fecha"] = "Debe ingresar una fecha."
    else:
        try:
            fecha_dt = datetime.strptime(fecha, "%Y-%m-%dT%H:%M")
        except ValueError:
            try:
                fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                errores["fecha"] = "La fecha no tiene un formato válido."
                fecha_dt = None

    # inmueble
    if not inmueble_id:
        errores["inmueble_id"] = "Debe seleccionar un inmueble."

    # tipo
    if not tipo or tipo not in tipos_validos:
        errores["tipo"] = "Debe seleccionar un tipo de multa válido."

    # valor
    try:
        valor_num = float(valor)
        if valor_num < 50000 or valor_num > 250000:
            errores["valor"] = "El valor debe estar entre 50,000 y 250,000."
    except ValueError:
        errores["valor"] = "El valor debe ser numérico."

    # trabajador
    if not trabajador_id:
        errores["trabajador_id"] = "Debe seleccionar un trabajador."

    # fecha de pago (opcional, pero si existe debe ser >= fecha multa)
    if fecha_pago:
        try:
            fecha_pago_dt = datetime.strptime(fecha_pago, "%Y-%m-%dT%H:%M")
        except ValueError:
            try:
                fecha_pago_dt = datetime.strptime(fecha_pago, "%Y-%m-%d")
            except ValueError:
                errores["fecha_pago"] = "La fecha de pago no tiene un formato válido."
                fecha_pago_dt = None
        if "fecha" not in errores and fecha_pago_dt and fecha_dt and fecha_pago_dt < fecha_dt:
            errores["fecha_pago"] = "La fecha de pago debe ser igual o posterior a la fecha de la multa."

    return errores