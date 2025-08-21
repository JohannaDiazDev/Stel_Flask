from flask import flash
from datetime import datetime

def validar_datos_cartera(form):
    errores = {}

    fecha_actual = form.get("fecha_actual","").strip()
    inmueble_id = form.get("inmueble_id","").strip() 
    estado = form.get("estado","").strip()
    saldo = form.get("saldo","").strip()
    trabajador_id = form.get("trabajador_id","").strip()
    observaciones = form.get("observaciones","").strip()

    estados_validos = ["Paz y Salvo", "Moroso", "Acuerdo de Pago", "Cobro Juridico"]

    if not fecha_actual:
        errores["fecha_actual"] = "Debe ingresar una fecha."
    else:
        try:
            datetime.strptime(fecha_actual,'%Y-%m-%dT%H:%M') 
        except ValueError:
            errores["fecha_actual"] = "La fecha no tiene un formato válido."

    if not inmueble_id:
        errores["inmueble_id"] = "Debe seleccionar un inmueble."

    if not estado or estado not in estados_validos:
        errores["estado"] = "Estado inválido."

    try:
        saldo_num = float(saldo)
        if saldo_num < 0:
            errores["saldo"] = "El saldo no puede ser negativo."                
    except ValueError:
        errores["saldo"] = "El saldo debe ser numérico."

    if not trabajador_id:
        errores["trabajador_id"] = "Debe seleccionar un trabajador."

    if len(observaciones) > 200:
        errores["observaciones"] = "Las observaciones no deben superar los 200 caracteres."

    return errores
