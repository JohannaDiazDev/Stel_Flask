from datetime import datetime

def _parse_dt(s):
    for fmt in ('%Y-%m-%dT%H:%M', '%Y-%m-%d'):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    raise ValueError('Formato inválido')

def validar_datos_multa(form):
    errores = []

    fecha = form.get('fecha', '').strip()
    inmueble_id = form.get('inmueble_id')
    tipo = form.get('tipo', '').strip()
    valor = form.get('valor', '').strip()
    trabajador_id = form.get('trabajador_id')
    fecha_pago = form.get('fecha_pago', '').strip()

    # fecha (obligatoria)
    if not fecha:
        errores.append('Debe ingresar una fecha.')
    else:
        try:
            fecha_dt = _parse_dt(fecha)
        except ValueError:
            errores.append('La fecha no tiene un formato válido.')

    # inmueble
    if not inmueble_id:
        errores.append('Debe seleccionar un inmueble.')

    # tipo
    tipos_validos = [
        'Ruido Excesivo', 'Estacionamiento indebido', 'Mascota sin correa',
        'Problemas con los vecinos', 'Daños a zonas comunes',
        'Problemas con mascotas', 'Inasistencia asamblea', 'Carro rayado'
    ]
    if not tipo or tipo not in tipos_validos:
        errores.append('Tipo de multa inválido.')

    # valor
    try:
        valor_float = float(valor)
        if valor_float < 50000 or valor_float > 250000:
            errores.append('El valor debe estar entre 50,000 y 250,000.')
    except (ValueError, TypeError):
        errores.append('El valor debe ser un número válido.')

    # trabajador
    if not trabajador_id:
        errores.append('Debe seleccionar un trabajador.')

    # fecha de pago (opcional, pero si viene: >= fecha)
    if fecha_pago:
        try:
            fecha_pago_dt = _parse_dt(fecha_pago)
            if 'fecha_dt' in locals() and fecha_pago_dt < fecha_dt:
                errores.append('La fecha de pago debe ser igual o posterior a la fecha de la multa.')
        except ValueError:
            errores.append('La fecha de pago no tiene un formato válido.')

    return errores
