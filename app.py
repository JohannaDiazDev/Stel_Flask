from flask import Flask, render_template, url_for, jsonify, request, session, flash, redirect, make_response
import re, time
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from datetime import datetime
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
import MySQLdb
from datetime import datetime
import calendar
import locale
locale.setlocale(locale.LC_TIME, 'Spanish_Colombia')
from collections import defaultdict
from functools import wraps

app = Flask (__name__)
bcrypt = Bcrypt(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'stel'
app.secret_key = 'mysecretkey'
def get_db_connection():
    return MySQLdb.connect(host="localhost", user="root", passwd="", db="stel")

# Inicializar extensiones
mysql = MySQL(app)
bcrypt = Bcrypt()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'pkiduser' not in session:
            flash('Debes iniciar sesión primero','danger')
            return redirect(url_for('ingresar'))
        return f(*args,**kwargs)
    return decorated_function

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.template_filter('datetimeformat')
def datetimeformat(value, format='%A, %d de %B'):
    # Configura el locale a español
    try:
        locale.setlocale(locale.LC_TIME, 'es_ES')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, 'es_CO.utf8')  # Otra alternativa
        except:
            locale.setlocale(locale.LC_TIME, '')  # Por defecto

    if isinstance(value, str):
        value = datetime.strptime(value, '%Y-%m-%d')
    return value.strftime(format)
#@app.route('/usuarios')
#def mostrar_usuarios():
#    usuarios = Usuarios.query.all()  # Obtiene todos los usuarios
#    return {'usuarios': [usuarios.nombre for usuarios in usuarios]}

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/sobre-nosotros')
def sobre_nosotros():
    return render_template('sobre-nosotros.html')

@app.route('/contactanos')
def contactanos():
    return render_template('contactanos.html')

@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    data = request.json
    nombre = data.get('nombre','')
    correo = data.get('correo','')
    asunto = data.get('asunto','')
    mensaje = data.get('mensaje','')

    errores = {}

    if not re.match(r'^[a-zA- Záéíóú\s]{3,60}$', nombre):
        errores['nombre'] = 'Nombre inválido'

    if not re.match(r'^[a-zA-Z0-9._%+-]+@(gmail\.com|hotmail\.com|yahoo\.com)$', correo):
        errores['correo'] = 'Email inválido' 

    if len(asunto) > 100:
        errores['asunto'] = 'El asunto no puede tener más de 100 caracteres'

    if len(mensaje) > 300:
        errores['mensaje'] = 'El mensaje no puede tener más de 300 caracteres'

    if errores:
        return jsonify({'success': False, 'errores': errores}), 400

    return jsonify({'success' : True, 'message': 'Correo enviado exitosamente'})    
        

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT pkiduser, contraseña, rol_id FROM usuarios WHERE correo = %s", (correo,))
        user = cursor.fetchone()
        #cursor.close()
        #db.close()

        if user is None:
            flash('❌ Usuario no encontrado', 'danger')
            return redirect(url_for('ingresar'))
        
        print(f"Contraseña ingresada: {contraseña}")
        print(f"Hash en la BD: {user[1]}")
        print(f"¿Coincide?: {bcrypt.check_password_hash(user[1], contraseña)}")
        print(f"Contraseña en la BD: {user[1]}")

        if user and bcrypt.check_password_hash(user[1], contraseña):  
            session.clear()
            session['loggedin'] = True
            session['pkiduser'] = user[0]
            session['rol_id'] = user[2]

            flash('Inicio de sesión exitoso', 'success')
            
            timestamp = int(time.time())

            if session.get('rol_id') == 1:  
                response = make_response(redirect(url_for('dashboard_admin', _t=timestamp), code=303))
            elif session.get('rol_id') == 2:  
                response = make_response(redirect(url_for('dashboard_residente', _t=timestamp), code=303))
            elif session.get('rol_id') == 3:  
                cursor.execute("SELECT pkidtrabajador FROM trabajador WHERE usuario_id = %s", (user[0],))
                trabajador = cursor.fetchone()

                if trabajador:
                    session['trabajador_id'] = trabajador[0]
                else:
                    flash('No se encontró trabajador asociado a este usuario', 'danger')
                    return redirect(url_for('ingresar'))

                response = make_response(redirect(url_for('dashboard_guarda', _t=timestamp), code=303))
            else:
                flash('Rol no reconocido', 'danger')
                cursor.close()
                db.close()
                return redirect(url_for('ingresar'))
            cursor.close()
            db.close()
            # Configurar cabeceras para evitar caché
            response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response.headers['Pragma'] = 'no-cache'
            response.headers['Expires'] = '0'
            
            return response
        else:
            flash('❌ Credenciales incorrectas', 'danger')

    response = make_response(render_template('ingresar.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response


@app.route('/admin/dashboard_admin')
@login_required
def dashboard_admin():   
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM correspondencia")
    correspondencia_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM parqueadero")
    parqueadero_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM multa")
    multas_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM cartera where estado = 'Paz y Salvo'")
    paz_y_salvo = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM cartera where estado = 'Moroso'")
    moroso = cursor.fetchone()[0]

    cursor.close()
    db.close()

    response = make_response(render_template('admin/dashboard_admin.html',
                                             correspondencia_count=correspondencia_count,
                                             parqueadero_count=parqueadero_count,
                                             multas_count=multas_count,
                                             paz_y_salvo=paz_y_salvo,
                                             moroso=moroso))
    
    # Agregar cabeceras para evitar caché
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0' 
    return response

@app.route('/admin/usuarios', methods=['GET'])
@login_required
def usuarios():
    
    db = get_db_connection()
    cursor = db.cursor()

    page = request.args.get('page', 1, type=int)
    per_page = 5  # Número de usuarios por página
    offset = (page - 1) * per_page

    cedula = request.args.get('cedula', '')

    # Consulta base
    sql = """
        SELECT u.pkiduser, u.nombre, u.cedula, u.celular, u.correo, u.rol_id, r.nombrerol 
        FROM usuarios u
        LEFT JOIN rol r ON u.rol_id = r.pkidrol
    """
    
    params = []
    if cedula:
        sql += " WHERE u.cedula LIKE %s"
        params.append(f"%{cedula}%")

    # Paginación
    sql += " LIMIT %s OFFSET %s"
    params.extend([per_page, offset])

    cursor.execute(sql, params)
    columnas = [col[0] for col in cursor.description]
    usuarios = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    # Consulta para los roles
    cursor.execute("SELECT pkidrol, nombrerol FROM rol")
    columnas_roles = [col[0] for col in cursor.description]
    roles = [dict(zip(columnas_roles, fila)) for fila in cursor.fetchall()]

    # Contar el total de usuarios
    if cedula:
        cursor.execute("SELECT COUNT(*) FROM usuarios WHERE cedula LIKE %s", (f"%{cedula}%",))
    else:
        cursor.execute("SELECT COUNT(*) FROM usuarios")

    total_usuarios = cursor.fetchone()[0]
    total_pages = (total_usuarios + per_page - 1) // per_page

    cursor.close()
    db.close()
  
    response = make_response(render_template('admin/usuarios.html', 
        usuarios=usuarios, 
        roles=roles, 
        page=page, 
        total_pages=total_pages, 
        cedula_buscar=cedula

    ))
    response.headers['Cache-Control'] = 'no-store'
    return response
# Crear un usuario
@app.route('/admin/usuarios', methods=['POST'])
def crear_usuario():
    db = get_db_connection()
    cursor = db.cursor()
    
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    celular = request.form['celular']
    correo = request.form['correo']
    contraseña = request.form['contraseña']
    rol_id = request.form['rol_id']

    sql = "INSERT INTO usuarios (nombre, cedula, celular, correo, contraseña, rol_id) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (nombre, cedula, celular, correo, contraseña, rol_id)
    
    cursor.execute(sql, valores)
    db.commit()
    cursor.close()
    db.close()
    
    return redirect(url_for('usuarios'))

@app.route('/delete/<int:pkiduser>')
def delete(pkiduser):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM usuarios WHERE pkiduser = %s", (pkiduser,))
    db.commit()
    db.close()
    return redirect(url_for('usuarios'))    

@app.route('/admin/usuarios/<int:pkiduser>/editar_usuario', methods=['GET', 'POST'])
def editar_usuario(pkiduser):
    db = get_db_connection()
    cursor = db.cursor()

    if request.method == 'POST':
        print(request.form)  # Verifica qué datos llegan en el formulario

        # Obtener valores del formulario de forma segura
        nombre = request.form.get('nombre')
        cedula = request.form.get('cedula')
        celular = request.form.get('celular')
        correo = request.form.get('correo')
        contraseña = request.form.get('contraseña')
        rol_id = request.form.get('rol_id')

        if not nombre or not correo:  # Verifica que no haya valores vacíos
            flash("Todos los campos son obligatorios", "error")
            return redirect(url_for('editar_usuario', pkiduser=pkiduser))

        # Actualizar usuario
        sql = """UPDATE usuarios SET nombre = %s, cedula = %s, celular = %s, 
                 correo = %s, contraseña = %s, rol_id = %s WHERE pkiduser = %s"""
        valores = (nombre, cedula, celular, correo, contraseña, rol_id, pkiduser)
        cursor.execute(sql, valores)
        db.commit()
        db.close()

        flash("Usuario actualizado correctamente", "success")
        return redirect(url_for('usuarios'))

    cursor.execute("SELECT * FROM usuarios WHERE pkiduser = %s", (pkiduser,))
    usuario = cursor.fetchone()

    # También recupera los roles
    cursor.execute("SELECT * FROM roles")
    roles = cursor.fetchall()

    db.close()

    return redirect(url_for('usuarios', usuario=usuario, roles=roles)) 

@app.route('/admin/inmueble')
@login_required
def inmueble():
    rol_id = session.get('rol_id')

    if rol_id == 1:
        base_template = 'admin/base_dash.html'
    elif rol_id == 3:
        base_template = 'guarda/dash_guarda.html'
    else:
        flash('Acesso no autorizado', 'danger')
        return redirect(url_for('ingresar')) 
    # Distribución de los andenes
    andenes = {
        1: {'min': 1, 'max': 31},
        2: {'min': 32, 'max': 56},
        3: {'min': 64, 'max': 87},
        4: {'min': 88, 'max': 101},
        5: {'min': 102, 'max': 115},
        6: {'min': 116, 'max': 139},
        7: {'min': 140, 'max': 163},
        8: {'min': 164, 'max': 187},
        9: {'min': 188, 'max': 213},
        10: {'min': 214, 'max': 240}
    }
    return render_template('admin/inmueble.html', andenes=andenes, base_template=base_template)

@app.route('/residentes')#----------------------------------------revisar#
def Residentes():
    return "Página de Residentes"

@app.route('/turnos', methods=['GET', 'POST'])
@login_required
def turnos():
    db = get_db_connection()
    cursor = db.cursor()

    # Consulta guardas al principio
    cursor.execute("SELECT pkiduser, nombre FROM usuarios WHERE rol_id = 3")
    columnas = [col[0] for col in cursor.description]
    guardas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    if request.method == 'POST':
        usuario_id = request.form['usuario_id']
        fecha = request.form['fecha']
        hora_inicio = request.form['hora_inicio']
        hora_fin = request.form['hora_fin']

        # Insertar turno
        cursor.execute("""
            INSERT INTO turnos (usuario_id, fecha, hora_inicio, hora_fin)
            VALUES (%s, %s, %s, %s)
        """, (usuario_id, fecha, hora_inicio, hora_fin))
        db.commit()
        cursor.close()
        db.close()

        # Redirigir para evitar reenviar formulario al recargar
        return redirect(url_for('turnos'))

    # Consulta turnos solo si es GET
    cursor.execute("""
        SELECT t.*, u.nombre 
        FROM turnos t
        JOIN usuarios u ON t.usuario_id = u.pkiduser
        ORDER BY t.fecha DESC, t.hora_inicio ASC
    """)
    columnas = [col[0] for col in cursor.description]
    turnos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.close()
    db.close()

    return render_template('/admin/turnos.html', guardas=guardas, turnos=turnos)

@app.route('/admin/multa', methods=['GET'])
@login_required
def multa():

    db = get_db_connection()
    cursor = db.cursor()

    page = request.args.get('page', 1, type=int)
    per_page = 5
    offset = (page - 1) * per_page
    tipo = request.args.get('tipo', '')

    # --- Consulta de multas con nombre de administradora ---
    sql = """
        SELECT m.pkidmulta, m.fecha, m.inmueble_id, m.tipo, m.valor, u.nombre AS nombre_trabajador, m.fecha_pago
        FROM multa m
        LEFT JOIN inmueble i ON m.inmueble_id = i.pkidinmueble
        LEFT JOIN trabajador t ON m.trabajador_id = t.pkidtrabajador
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
    """

    params = []
    if tipo:
        sql += " WHERE m.tipo LIKE %s"
        params.append(f"%{tipo}%")

    sql += " LIMIT %s OFFSET %s"
    params.extend([per_page, offset])

    cursor.execute(sql, params)
    columnas = [col[0] for col in cursor.description]
    multas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    # --- Inmuebles ---
    cursor.execute("SELECT pkidinmueble, numeroinmueble FROM inmueble")
    columnas_inmueble = [col[0] for col in cursor.description]
    inmuebles = [dict(zip(columnas_inmueble, fila)) for fila in cursor.fetchall()]

    # --- Solo administradora como trabajadora ---
    cursor.execute("""
        SELECT t.pkidtrabajador, u.nombre
        FROM trabajador t
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
        WHERE u.pkiduser = 1
    """)
    columnas_trabajador = [col[0] for col in cursor.description]
    trabajadores = [dict(zip(columnas_trabajador, fila)) for fila in cursor.fetchall()]

    # --- Usuarios ---
    cursor.execute("SELECT pkiduser, nombre FROM usuarios")
    columnas_usuario = [col[0] for col in cursor.description]
    usuarios = [dict(zip(columnas_usuario, fila)) for fila in cursor.fetchall()]

    # --- Paginación ---
    if tipo:
        cursor.execute("SELECT COUNT(*) FROM multa WHERE tipo LIKE %s", (f"%{tipo}%",))
    else:
        cursor.execute("SELECT COUNT(*) FROM multa")
    total_multa = cursor.fetchone()[0]
    total_pages = (total_multa + per_page - 1) // per_page

    cursor.close()
    db.close()

    response = make_response(render_template('admin/multa.html', 
        multas=multas, 
        usuarios=usuarios,
        inmuebles=inmuebles,
        trabajadores=trabajadores, 
        page=page, 
        total_pages=total_pages, 
        tipo_buscar=tipo
    ))

    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/admin/multa', methods=['POST'])
def crear_multa():
    db = get_db_connection()
    cursor = db.cursor()

    fecha = request.form['fecha']
    inmueble_id = request.form['inmueble_id']
    tipo = request.form['tipo']
    valor = request.form['valor']
    trabajador_id = request.form['trabajador_id']
    fecha_pago = request.form['fecha_pago']

    sql = "INSERT INTO multa (fecha, inmueble_id, tipo, valor, trabajador_id, fecha_pago) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (fecha, inmueble_id, tipo, valor, trabajador_id, fecha_pago)

    cursor.execute(sql, valores)
    db.commit()
    cursor.close()
    db.close()
    cursor.execute("SELECT pkidtrabajador, nombre FROM trabajador")
    trabajadores = cursor.fetchall()
    cursor.close()
    db.close()
    return redirect(url_for('multa', trabajadores,trabajadores))

@app.route('/delete_multa/<int:pkidmulta>')
def delete_multa(pkidmulta):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM multa WHERE pkidmulta = %s", (pkidmulta,))
    db.commit()
    db.close()
    return redirect(url_for('multa'))

@app.route('/admin/multa/<int:pkidmulta>/editar_multa', methods=['GET','POST'])
def editar_multa(pkidmulta):
    db = get_db_connection()
    cursor = db.cursor()
    
    if request.method == 'POST':

        fecha = request.form.get('fecha')
        inmueble_id = request.form.get('inmueble_id')
        tipo = request.form.get('tipo')
        valor = request.form.get('valor')
        trabajador_id = request.form.get('trabajador_id')
        fecha_pago = request.form.get('fecha_pago')

        sql = """UPDATE multa SET fecha = %s, inmueble_id = %s, tipo = %s, valor = %s, trabajador_id =%s, fecha_pago = %s WHERE pkidmulta = %s"""
        valores = (fecha, inmueble_id, tipo, valor, trabajador_id, fecha_pago, pkidmulta)
        cursor.execute(sql, valores)
        db.commit()
        db.close()

        flash("Multa actualizada correctamente", "success")
        return redirect(url_for('multa'))
    
    cursor.execute("SELECT * FROM multa WHERE pkidmulta = %s", (pkidmulta,))
    multa = cursor.fetchone()
    cursor.execute("SELECT pkidinmueble, numeroinmueble FROM inmueble")
    inmuebles = cursor.fetchall()

    cursor.execute("""
        SELECT t.pkidtrabajador, u.nombre 
        FROM trabajador t 
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser 
        WHERE u.pkiduser = 1
    """)
    trabajadores = cursor.fetchall()

    cursor.close()
    db.close()
        
    return render_template('admin/multa.html', multa=multa, inmuebles=inmuebles, trabajadores=trabajadores)

@app.route('/admin/cartera', methods=['GET'])
@login_required
def cartera():
    db = get_db_connection()
    cursor = db.cursor()

    page = request.args.get('page', 1, type=int)
    per_page = 5
    offset = (page - 1) * per_page
    estado = request.args.get('estado', '')

    sql = """
        SELECT c.pkidestado, c.fecha_actual, c.inmueble_id, c.estado, c.saldo, u.nombre AS nombre_trabajador, c.observaciones
        FROM cartera c
        LEFT JOIN inmueble i ON c.inmueble_id = i.pkidinmueble
        LEFT JOIN trabajador t ON c.trabajador_id = t.pkidtrabajador
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
    """

    params = []
    if estado:
        sql += " WHERE c.estado LIKE %s"
        params.append(f"%{estado}%")
    sql += " LIMIT %s OFFSET %s"
    params.extend([per_page, offset])

    cursor.execute(sql,params)
    columnas = [col[0] for col in cursor.description]
    carteras = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkidinmueble, numeroinmueble FROM inmueble")
    columnas_inmueble = [col[0] for col in cursor.description]
    inmuebles = [dict(zip(columnas_inmueble, fila)) for fila in cursor.fetchall()]

    cursor.execute("""
        SELECT t.pkidtrabajador, u.nombre
        FROM trabajador t
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
        WHERE u.pkiduser = 1
    """)
    columnas_trabajador = [col[0] for col in cursor.description]
    trabajadores = [dict(zip(columnas_trabajador, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkiduser, nombre FROM usuarios")
    columnas_usuario = [col[0] for col in cursor.description]
    usuarios = [dict(zip(columnas_usuario, fila)) for fila in cursor.fetchall()]

    if estado:
        cursor.execute("SELECT COUNT(*) FROM cartera WHERE estado LIKE %s", (f"%{estado}%",))
    else:
        cursor.execute("SELECT COUNT(*) FROM cartera")
    total_cartera = cursor.fetchone()[0]
    total_pages = (total_cartera + per_page - 1 ) // per_page

    cursor.close()
    db.close()

    response = make_response(render_template('admin/cartera.html',
        carteras = carteras, usuarios = usuarios, inmuebles = inmuebles,
        trabajadores = trabajadores, page=page, total_pages=total_pages,estado_buscar=estado
    ))
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/admin/cartera', methods=['POST'])
def crear_cartera():
    db = get_db_connection()
    cursor = db.cursor()

    fecha_actual = request.form['fecha_actual']
    inmueble_id = request.form['inmueble_id']
    estado = request.form['estado']
    saldo = request.form['saldo'] 
    trabajador_id = request.form['trabajador_id']
    observaciones = request.form['observaciones']

    sql = "INSERT INTO cartera (fecha_actual, inmueble_id, estado, saldo, trabajador_id, observaciones) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (fecha_actual, inmueble_id, estado, saldo, trabajador_id, observaciones)

    cursor.execute(sql,valores)
    db.commit()
    
    cursor.execute("SELECT pkidtrabajador FROM trabajador")
    trabajadores = cursor.fetchall()
    cursor.close()
    db.close()
    return redirect(url_for('cartera', trabajadores=trabajadores))

@app.route('/delete_cartera/<int:pkidestado>')
def delete_cartera(pkidestado):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM cartera WHERE pkidestado = %s", (pkidestado,))
    db.commit()
    db.close()
    return redirect(url_for('cartera'))

@app.route('/admin/cartera/<int:pkidestado>/editar_cartera', methods=['GET','POST'])
def editar_cartera(pkidestado):
    db = get_db_connection()
    cursor = db.cursor()

    if request.method == 'POST':
        fecha_actual = request.form.get('fecha_actual')
        inmueble_id = request.form.get('inmueble_id')
        estado = request.form.get('estado')
        saldo = request.form.get('saldo')
        trabajador_id = request.form.get('trabajador_id')
        observaciones = request.form.get('observaciones')

        sql = """UPDATE cartera SET fecha_actual = %s, inmueble_id = %s, estado = %s, saldo = %s, trabajador_id = %s, observaciones = %s WHERE pkidestado = %s """
        valores = (fecha_actual, inmueble_id, estado, saldo, trabajador_id, observaciones, pkidestado)
        cursor.execute(sql,valores)
        db.commit()
        db.close()
        flash("Cartera actualizada correctamente", "success")
        return redirect(url_for('cartera'))

    cursor.execute("SELECT * FROM cartera WHERE pkidestado = %s", (pkidestado,))
    cartera = cursor.fetchone()
    cursor.execute("SELECT pkidinmueble, numeroinmueble FROM inmueble")
    inmuebles = cursor.fetchall()

    cursor.execute("""
        SELECT t.pkidtrabajador, u.nombre
        FROM trabajador t
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
        WHERE u.pkiduser = 1
    """)
    trabajadores = cursor.fetchall()

    cursor.close()
    db.close() 

    return render_template('admin/cartera.html', cartera=cartera, inmuebles=inmuebles, trabajadores=trabajadores)

@app.route('/admin/visitante', methods=['GET'])
@login_required
def visitante():
    db = get_db_connection()
    cursor = db.cursor()

    rol_id = session.get('rol_id')

    if rol_id == 1:
        base_template = 'admin/base_dash.html'
    elif rol_id == 3:
        base_template = 'guarda/dash_guarda.html'
    else:
        flash('Acesso no autorizado', 'danger')
        return redirect(url_for('ingresar')) 
           
    page = request.args.get('page', 1, type=int)
    per_page = 5
    offset = (page - 1)* per_page
    cedula = request.args.get('cedula','')

    sql = """
        SELECT v.pkidvisitante, v.fecha, v.inmueble_id, v.autorizado, v.nombre, v.cedula, v.ingresa_carro
        FROM visitante v
        LEFT JOIN inmueble i ON v.inmueble_id = i.pkidinmueble
    """
    params = []
    if cedula:
        sql += " WHERE v.cedula LIKE %s"
        params.append(f"%{cedula}%")
    sql += "LIMIT %s OFFSET %s"
    params.extend([per_page, offset])

    cursor.execute(sql, params)
    columnas = [col[0] for col in cursor.description]
    visitantes = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkidinmueble, numeroinmueble FROM inmueble")
    columnas_inmueble = [col[0] for col in cursor.description]
    inmuebles = [dict(zip(columnas_inmueble, fila)) for fila in cursor.fetchall()]

    if cedula:
        cursor.execute("SELECT COUNT(*) FROM visitante WHERE cedula LIKE %s", (f"%{cedula}%",))
    else:
        cursor.execute("SELECT COUNT(*) FROM visitante")
    total_visitante = cursor.fetchone()[0]
    total_pages = (total_visitante + per_page - 1)// per_page

    cursor.close()
    db.close()
    response = make_response(render_template('admin/visitante.html',
        visitantes=visitantes, inmuebles=inmuebles, page=page,
        total_pages=total_pages,cedula_buscar=cedula,base_template=base_template
    ))
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/admin/visitante', methods=['POST'])
def crear_visitante():
    db = get_db_connection()
    cursor = db.cursor()

    fecha = request.form['fecha'] 
    inmueble_id = request.form['inmueble_id']
    autorizado = request.form['autorizado']
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    ingresa_carro = request.form['ingresa_carro']

    sql= "INSERT INTO visitante (fecha, inmueble_id, autorizado, nombre, cedula, ingresa_carro) VALUES (%s,%s,%s,%s,%s,%s)"
    valores = (fecha, inmueble_id, autorizado, nombre, cedula, ingresa_carro)

    cursor.execute(sql,valores)
    db.commit()
    cursor.execute("SELECT pkidinmueble FROM inmueble")
    inmuebles = cursor.fetchall()
    cursor.close()
    db.close()
    return redirect(url_for('visitante', inmuebles=inmuebles))

@app.route('/delete_visitante/<int:pkidvisitante>')
def delete_visitante(pkidvisitante):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM visitante WHERE pkidvisitante = %s", (pkidvisitante,))
    db.commit()
    db.close()
    return redirect(url_for('visitante'))

@app.route('/admin/visitante/<int:pkidvisitante>/editar_visitante', methods=['POST'])
def editar_visitante(pkidvisitante):
    db = get_db_connection()
    cursor = db.cursor()

    if session.get('rol_id') == 1:
        flash('No tienes permiso para editar visitantes.', 'danger')
        return redirect(url_for('visitante'))
    if request.method == 'POST':
        fecha = request.form.get('fecha')
        inmueble_id = request.form.get('inmueble_id') 
        autorizado = request.form.get('autorizado') 
        nombre = request.form.get('nombre')
        cedula = request.form.get('cedula')
        ingresa_carro = request.form.get('ingresa_carro')

        sql = "UPDATE visitante SET fecha = %s, inmueble_id = %s, autorizado = %s, nombre = %s, cedula = %s, ingresa_carro = %s WHERE pkidvisitante = %s"
        valores = (fecha, inmueble_id, autorizado, nombre, cedula, ingresa_carro, pkidvisitante)
        cursor.execute(sql,valores)
        db.commit()
        db.close()

        flash("Visitante actualizado correctamente", "success")
        return redirect(url_for('visitante'))
    cursor.execute("SELECT * FROM visitante WHERE pkidvisitante = %s", (pkidvisitante))
    visitante = cursor.fetchone()
    cursor.execute("SELECT * FROM inmueble")
    inmuebles = cursor.fetchall()
    cursor.close()
    db.close()

    return render_template('admin/visitante.html', visitante=visitante, inmuebles=inmuebles)

@app.route('/admin/parqueadero', methods=['GET','POST'])
@login_required
def parqueadero():
    db = get_db_connection()
    cursor = db.cursor()

    hoy = datetime.now()
    mes = request.args.get('mes', hoy.month, type=int)
    mes_nombre = datetime(2025, mes, 1).strftime('%B').capitalize()
    meses = [{'Valor': i, 'nombre': datetime(2025, i, 1).strftime('%B').capitalize()} for i in range(1, 13)]

    cupos_carros = 56
    cupos_motos = 43
    total_cupos = cupos_carros + cupos_motos

    cursor.execute("""
        SELECT COUNT(*) FROM parqueadero
        WHERE MONTH(fecha) = %s AND (estado = 'ocupado' OR estado = 'disponible')
    """, (mes,))
    ocupado = cursor.fetchone()[0]

    disponible = total_cupos - ocupado

    cursor.execute("""
        SELECT COUNT(*) FROM parqueadero
        WHERE MONTH(fecha) = %s AND estado = 'ocupado' AND tipo = 'carro'
    """, (mes,))
    carros_ocupados = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*) FROM parqueadero
        WHERE MONTH(fecha) = %s AND estado = 'ocupado' AND tipo = 'moto'
    """, (mes,))
    motos_ocupadas = cursor.fetchone()[0]

    cursor.execute("""
        SELECT SUM(tarifa) FROM parqueadero
        WHERE tarifa IS NOT NULL AND MONTH(fecha) = %s AND YEAR(fecha) = %s
    """, (mes, hoy.year))
    fila = cursor.fetchone()
    total_ingresos = fila[0] if fila and fila[0] is not None else 0


    cursor.execute("""
        SELECT MONTH(fecha), SUM(tarifa) FROM parqueadero
        WHERE tarifa IS NOT NULL AND YEAR(fecha) = %s
        GROUP BY MONTH(fecha)
        ORDER BY MONTH(fecha)
    """, (hoy.year,))
    resultados_mes = cursor.fetchall()

    meses_graf = [datetime(2025, i, 1).strftime('%B').capitalize() for i in range(1, 13)]
    ingresos_graf = [0] * 12
    for m, ingreso in resultados_mes:
        ingresos_graf[m - 1] = ingreso or 0

    pagina = request.args.get('pagina', 1, type=int)
    por_pagina = 10
    offset = (pagina - 1) * por_pagina

    cursor.execute("""
        SELECT COUNT(*) FROM parqueadero
        WHERE tarifa IS NOT NULL AND hora_salida IS NOT NULL AND MONTH(fecha) = %s
    """, (mes,))
    total_registros = cursor.fetchone()[0]
    total_paginas = (total_registros + por_pagina - 1) // por_pagina

    cursor.execute("""
        SELECT * FROM parqueadero WHERE tarifa IS NOT NULL AND hora_salida IS NOT NULL AND MONTH(fecha) =%s
        ORDER BY fecha DESC LIMIT %s OFFSET %s
    """, (mes, por_pagina, offset))
    registros = cursor.fetchall()
    
    cursor.close()
    db.close()

    response = make_response(render_template('admin/parqueadero.html',
                total_cupos=total_cupos, ocupado=ocupado, hoy=hoy,
                disponible=disponible, total_ingresos=total_ingresos, 
                cupos_carros=cupos_carros, cupos_motos=cupos_motos, carros_ocupados=carros_ocupados,
                mes_actual=mes_nombre, mes_actual_num=mes, meses=meses, motos_ocupadas=motos_ocupadas,
                meses_graf=meses_graf, ingresos_graf=ingresos_graf, registros=registros,pagina=pagina,
                total_paginas=total_paginas))
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/admin/correspondencia', methods=['GET','POST'])
@login_required
def correspondencia():
    db = get_db_connection()
    cursor = db.cursor()
    
    if request.method == 'POST':

        fecha_recibido = request.form['fecha_recibido']
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        trabajador_id = 1
        inmueble_id = None

        sql = """
            INSERT INTO correspondencia (trabajador_id, inmueble_id, fecha_recibido, descripcion, tipo, estado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(trabajador_id, inmueble_id, fecha_recibido, descripcion, tipo,'generado'))
        db.commit()
        cursor.close()
    flash('Carta registrada exitosamente.', 'success')
    response = make_response(render_template('admin/correspondencia.html'))

    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/admin/novedades', methods=['GET'])
@login_required
def novedades():
    db = get_db_connection()
    cursor = db.cursor()

    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page
    estado = request.args.get('estado', '').strip().lower()

    sql = """
        SELECT n.pkidnovedad, u.nombre AS nombre_trabajador, n.fecha, n.inmueble_id, n.tipo, n.asunto, n.descripcion, n.estado 
        FROM novedades n
        LEFT JOIN trabajador t ON n.trabajador_id = t.pkidtrabajador
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
        LEFT JOIN inmueble i ON n.inmueble_id = i.pkidinmueble
    """
    params = []
    if estado:
        sql += "WHERE n.estado LIKE %s"
        params.append(f"%{estado}%")
    sql += " LIMIT %s OFFSET %s"
    params.extend([per_page, offset])            

    cursor.execute(sql, params)
    resultados = cursor.fetchall()
    
    columnas = ['pkidnovedad', 'nombre_trabajador', 'fecha', 'inmueble_id', 'tipo', 'asunto', 'descripcion', 'estado']
    novedades = [dict(zip(columnas, fila)) for fila in resultados]

    # Obtener datos auxiliares
    cursor.execute("SELECT t.pkidtrabajador, u.nombre FROM trabajador t LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser")
    columnas_trabajador = [col[0] for col in cursor.description]
    trabajadores = [dict(zip(columnas_trabajador, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkiduser, nombre FROM usuarios")
    columnas_usuario = [col[0] for col in cursor.description]
    usuarios = [dict(zip(columnas_usuario, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkidinmueble, numeroinmueble FROM inmueble")
    columnas_inmueble = [col[0] for col in cursor.description]
    inmuebles = [dict(zip(columnas_inmueble, fila)) for fila in cursor.fetchall()]

    if estado:
        cursor.execute("SELECT COUNT(*) FROM novedades WHERE estado LIKE %s", (f"%{estado}%",))
    else:
        cursor.execute("SELECT COUNT(*) FROM novedades")
    total_novedad = cursor.fetchone()[0]
    total_pages = (total_novedad + per_page - 1) // per_page    

    cursor.close()
    db.close()
    response = make_response(render_template('admin/novedades.html', novedades=novedades,page=page,total_pages=total_pages, estado_buscar=estado, 
        resultados=resultados, trabajadores=trabajadores, inmuebles=inmuebles, usuarios=usuarios))

    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/admin/novedades', methods=['POST'])
def crear_novedad():
    db = get_db_connection()
    cursor = db.cursor()

    trabajador_id = request.form['trabajador_id']
    fecha = request.form['fecha']
    inmueble_id = request.form['inmueble_id'] or None
    tipo = request.form['tipo']
    asunto = request.form['asunto']
    descripcion = request.form['descripcion']
    estado = request.form['estado']

    sql = """
        INSERT INTO novedades (trabajador_id, fecha, inmueble_id, tipo, asunto, descripcion, estado)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    valores = (trabajador_id, fecha, inmueble_id, tipo, asunto, descripcion, estado)

    cursor.execute(sql, valores)
    db.commit()

    cursor.close()
    db.close()

    flash('Novedad registrada exitosamente.', 'success')
    return redirect(url_for('novedades'))

@app.route('/admin/novedades/<int:pkidnovedad>/editar_novedad', methods=['GET','POST'])
def editar_novedad(pkidnovedad):
    db = get_db_connection()
    cursor = db.cursor()

    if request.method == 'POST':

        trabajador_id = request.form.get('trabajador_id')
        fecha = request.form.get('fecha') 
        inmueble_id = request.form.get('inmueble_id') or None
        tipo = request.form.get('tipo')
        asunto = request.form.get('asunto')
        descripcion = request.form.get('descripcion')
        estado = request.form.get('estado')

        sql = """UPDATE novedades SET trabajador_id = %s, fecha = %s, inmueble_id = %s, tipo = %s, asunto = %s, descripcion = %s, estado = %s WHERE pkidnovedad = %s"""
        valores = (trabajador_id, fecha, inmueble_id, tipo, asunto, descripcion, estado, pkidnovedad)
        cursor.execute(sql, valores)
        db.commit()
        db.close()
        flash("Novedad actualizada correctamente","success")
        return redirect(url_for('novedades'))
    cursor.execute("SELECT * FROM novedades WHERE pkidnovedad = %s", (pkidnovedad,))
    novedad = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template('admin/novedades.html', novedad=novedad)

@app.route('/dashboard_guarda')
@login_required
def dashboard_guarda():
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT COUNT(*) FROM parqueadero")
    parqueadero_contar = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM correspondencia")
    correspondencia_contar = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM novedades")
    novedades_contar = cursor.fetchone()[0]

    cursor.close()
    db.close()

    response = make_response(render_template('guarda/dashboard_guarda.html',
                parqueadero_contar=parqueadero_contar, correspondencia_contar=correspondencia_contar,
                novedades_contar=novedades_contar))
    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/inmueble_guarda')
@login_required
def inmueble_guarda():
    # Distribución de los andenes
    andenes = {
        1: {'min': 1, 'max': 31},
        2: {'min': 32, 'max': 56},
        3: {'min': 64, 'max': 87},
        4: {'min': 88, 'max': 101},
        5: {'min': 102, 'max': 115},
        6: {'min': 116, 'max': 139},
        7: {'min': 140, 'max': 163},
        8: {'min': 164, 'max': 187},
        9: {'min': 188, 'max': 213},
        10: {'min': 214, 'max': 240}
    }
    return render_template('guarda/inmueble_guarda.html', andenes=andenes)

@app.route('/guarda/parqueadero_guarda')
@login_required
def parqueadero_guarda():
    if session.get('rol_id') != 3:
        flash('No tienes permisos para acceder', 'danger')
        return redirect(url_for('ingresar'))
    db = get_db_connection()
    cursor = db.cursor()
    page = request.args.get('page', 1, type=int)
    per_page = 5
    offset = (page - 1) * per_page
    estado = request.args.get('estado', '') 

    sql = """
        SELECT p.*, u.nombre AS nombre_residente, v.nombre
        FROM parqueadero p
        LEFT JOIN residente r ON p.residente_id = r.pkidresidente
        LEFT JOIN usuarios u ON r.usuario_id = u.pkiduser
        LEFT JOIN visitante v ON p.visitante_id = v.pkidvisitante       
    """
    params = []
    if estado:
        sql += " WHERE p.estado LIKE %s"
        params.append(f"%{estado}%")

    sql += " LIMIT %s OFFSET %s"
    params.extend([per_page, offset])

    cursor.execute(sql,params)
    columnas = [col[0] for col in cursor.description]
    parqueos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.execute("""
        SELECT r.pkidresidente, u.nombre AS nombre_residente
        FROM residente r
        LEFT JOIN usuarios u ON r.usuario_id = u.pkiduser
    """)
    columnas_residente = [col[0] for col in cursor.description]
    residentes = [dict(zip(columnas_residente, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkidvisitante, nombre FROM visitante")
    columnas_visitante = [col[0] for col in cursor.description]
    visitantes = [dict(zip(columnas_visitante, fila)) for fila in cursor.fetchall()]

    if estado:
        cursor.execute("SELECT COUNT(*) FROM parqueadero WHERE estado LIKE %s", (f"%{estado}%",))
    else:
        cursor.execute("SELECT COUNT(*) FROM parqueadero")
    total_parqueadero = cursor.fetchone()[0]
    total_pages = (total_parqueadero + per_page - 1 ) // per_page

    cursor.close()
    db.close()

    response = make_response(render_template('guarda/parqueadero_guarda.html',
        parqueos=parqueos, residentes=residentes,visitantes=visitantes, page=page,total_pages=total_pages,estado_buscar=estado))

    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/guarda/parqueadero_guarda', methods=['POST'])
def registrar_parqueo():
    if session.get('rol_id') != 3:
        flash('No tienes permisos para registrar parqueaderos', 'danger')
        return redirect(url_for('ingresar'))
    
    db = get_db_connection()
    cursor = db.cursor()

    cupo = request.form['cupo']
    residente_id = request.form.get('residente_id') or None
    visitante_id = request.form.get('visitante_id') or None
    estado = request.form['estado'] 
    fecha = request.form['fecha']
    tipo = request.form['tipo']
    placa = request.form['placa']
    hora_salida = None
    tarifa = 0

    cursor.execute("""
        INSERT INTO parqueadero (cupo, tarifa, residente_id, visitante_id, estado, fecha, tipo, placa, hora_salida)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (cupo, tarifa, residente_id, visitante_id, estado, fecha, tipo, placa, hora_salida))
    db.commit()
    cursor.close()
    db.close()
    return redirect(url_for('parqueadero_guarda'))

@app.route('/guarda/parqueadero_guarda/<int:pkidparqueadero>/editar_parqueo', methods=['GET', 'POST'])
def editar_parqueo(pkidparqueadero):
    db = get_db_connection()
    cursor = db.cursor()

    if request.method == 'POST':
        cupo = request.form['cupo']
        residente_id = request.form.get('residente_id') or None
        visitante_id = request.form.get('visitante_id') or None
        estado = request.form['estado']
        fecha_str = request.form['fecha']
        tipo = request.form['tipo']
        placa = request.form['placa']
        hora_salida_str = request.form.get('hora_salida')

        # Parseamos fecha y hora
        formato_fecha = "%Y-%m-%dT%H:%M:%S" if len(fecha_str) > 16 else "%Y-%m-%dT%H:%M"
        entrada = datetime.strptime(fecha_str, formato_fecha)
        fecha = entrada.strftime("%Y-%m-%d %H:%M:%S")

        hora_salida = None
        tarifa = 0

        if visitante_id and hora_salida_str:
            formato_salida = "%Y-%m-%dT%H:%M:%S" if len(hora_salida_str) > 16 else "%Y-%m-%dT%H:%M"
            salida = datetime.strptime(hora_salida_str, formato_salida)
            hora_salida = salida.strftime("%Y-%m-%d %H:%M:%S")

            horas = (salida - entrada).total_seconds() / 3600
            horas = max(1, int(horas + 0.5))
            tarifa = horas * 1500
        elif residente_id:
            if tipo == 'carro':
                tarifa = 62000
            elif tipo == 'moto':
                tarifa = 40000

        cursor.execute("""
            UPDATE parqueadero
            SET cupo=%s, tarifa=%s, residente_id=%s, visitante_id=%s, estado=%s,
                fecha=%s, tipo=%s, placa=%s, hora_salida=%s
            WHERE pkidparqueadero = %s
        """, (cupo, tarifa, residente_id, visitante_id, estado, fecha, tipo, placa, hora_salida, pkidparqueadero))
        db.commit()
        flash("Parqueadero actualizado correctamente", "success")

    cursor.execute("""
        SELECT p.*, u.nombre AS nombre_residente, v.nombre
        FROM parqueadero p
        LEFT JOIN residente r ON p.residente_id = r.pkidresidente
        LEFT JOIN usuarios u ON r.usuario_id = u.pkiduser
        LEFT JOIN visitante v ON p.visitante_id = v.pkidvisitante
    """)
    columnas = [col[0] for col in cursor.description]
    parqueos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.execute("""
        SELECT r.pkidresidente, u.nombre AS nombre_residente
        FROM residente r
        LEFT JOIN usuarios u ON r.usuario_id = u.pkiduser
    """)
    columnas_residente = [col[0] for col in cursor.description]
    residentes = [dict(zip(columnas_residente, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkidvisitante, nombre FROM visitante")
    columnas_visitante = [col[0] for col in cursor.description]
    visitantes = [dict(zip(columnas_visitante, fila)) for fila in cursor.fetchall()]

    page = 1
    per_page = 2
    total_parqueadero = len(parqueos)
    total_pages = (total_parqueadero + per_page - 1) // per_page
    cursor.close()
    db.close()

    return render_template('guarda/parqueadero_guarda.html',
        parqueos=parqueos,
        residentes=residentes,
        visitantes=visitantes,
        page=page,
        total_pages=total_pages,
        estado_buscar=""
    )

@app.route('/correspondencia_guarda')
@login_required
def correspondencia_guarda():

    page = int(request.args.get('page', 1))
    por_pagina = 10
    offset = (page - 1) * por_pagina

    db = get_db_connection()
    cursor = db.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM correspondencia")
    total_registros = cursor.fetchone()[0]
    total_paginas = (total_registros + por_pagina - 1) // por_pagina

    trabajador_id = session.get('trabajador_id')
    sql = """
        SELECT c.pkidcorrespondencia, u.nombre AS nombre_trabajador, c.inmueble_id, c.fecha_recibido, c.fecha_entrega, 
        c.descripcion, c.tipo, c.estado FROM correspondencia c
        LEFT JOIN trabajador t ON c.trabajador_id = t.pkidtrabajador
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
        LEFT JOIN inmueble i ON c.inmueble_id = i.pkidinmueble
        WHERE c.trabajador_id = %s
        ORDER BY c.fecha_recibido DESC
        LIMIT %s OFFSET %s
    """
    cursor.execute(sql, (trabajador_id, por_pagina, offset))
    columnas = [col[0] for col in cursor.description]
    correspondencias = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]

    cursor.execute("""SELECT t.pkidtrabajador, u.nombre FROM trabajador t 
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser""")
    col_trabajador = [col[0] for col in cursor.description]
    trabajadores = [dict(zip(col_trabajador, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkiduser, nombre FROM usuarios")
    col_usuario = [col[0] for col in cursor.description]
    usuarios = [dict(zip(col_usuario, fila)) for fila in cursor.fetchall()]

    cursor.execute("SELECT pkidinmueble, numeroinmueble FROM inmueble")
    col_inmueble = [col[0] for col in cursor.description]
    inmuebles = [dict(zip(col_inmueble, fila)) for fila in cursor.fetchall()]

    cursor.close()
    db.close()
    response = make_response(render_template('guarda/correspondencia_guarda.html', correspondencias=correspondencias,
        trabajadores=trabajadores, usuarios=usuarios, inmuebles=inmuebles,total_paginas=total_paginas,
        pagina_actual=page,))

    response.headers['Cache-Control'] = 'no-store'
    return response

@app.route('/guarda/correspondencia_guarda', methods=['POST'])
@login_required
def registrar_correspondencia():
    db = get_db_connection()
    cursor = db.cursor()

    trabajador_id = request.form['trabajador_id']
    inmueble_id = request.form.get('inmueble_id') or None
    fecha_str = request.form.get('fecha_recibido', '').strip()
    fecha_entrega = request.form.get('fecha_entrega') or None
    descripcion = request.form['descripcion']
    tipo = request.form['tipo']
    estado = request.form['estado']

    if fecha_str:
        formato = "%Y-%m-%dT%H:%M:%S" if len(fecha_str) > 16 else "%Y-%m-%dT%H:%M"
        fecha_recibido = datetime.strptime(fecha_str, formato).strftime('%Y-%m-%d %H:%M:%S')
    else:
        # Si no se envía fecha, usar la actual
        fecha_recibido = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    sql = "INSERT INTO correspondencia (trabajador_id, inmueble_id, fecha_recibido, fecha_entrega, descripcion, tipo, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    valores = (trabajador_id, inmueble_id, fecha_recibido, fecha_entrega, descripcion, tipo, estado)
    cursor.execute(sql, valores)
    db.commit()

    cursor.execute("""
        SELECT t.pkidtrabajador, u.nombre 
        FROM trabajador t
        LEFT JOIN usuarios u ON t.usuario_id = u.pkiduser
    """)
    trabajadores = cursor.fetchall()
    cursor.close()
    db.close()
    flash('Correspondencia registrada correctamente', 'success')
    return redirect(url_for('correspondencia_guarda', trabajadores=trabajadores))

@app.route('/guarda/correspondencia_guarda/editar_correspondencia', methods=['GET','POST'])
def editar_correspondencia():
    db = get_db_connection()
    cursor = db.cursor()

    pkidcorrespondencia = request.form['pkidcorrespondencia'] 
    tipo = request.form['tipo']
    descripcion = request.form['descripcion']
    estado = request.form['estado'] 
    fecha_entrega = request.form.get('fecha_entrega') or None

    sql = """
        UPDATE correspondencia
        SET tipo = %s, descripcion = %s, estado = %s, fecha_entrega = %s
        WHERE pkidcorrespondencia = %s
    """
    valores = (tipo, descripcion, estado, fecha_entrega, pkidcorrespondencia)
    cursor.execute(sql, valores)
    db.commit()
    cursor.close()
    db.close()
    flash("Correspondencia actualizada correctamente", "success")
    return redirect(url_for('correspondencia_guarda'))


@app.route('/novedades_guarda')
def novedades_guarda():
    return 'novedades guarda'

@app.route('/dashboard_residente')
def dashboard_residente():
    return 'pagina residente'



@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Elimina 'user_id' si existe
    session.clear()  # Borra toda la sesión
    flash('Has cerrado sesión correctamente', 'success')
    
    response = make_response(redirect(url_for('ingresar')))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True)