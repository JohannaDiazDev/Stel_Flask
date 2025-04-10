from flask import Flask, render_template, url_for, jsonify, request, session, flash, redirect, make_response
import re, time
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
import MySQLdb
import pymysql
import mysql.connector
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

@app.route('/')
def inicio():
    return render_template('inicio.html')

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
        

        # Conectar a la base de datos
        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("SELECT pkiduser, contraseña, rol_id FROM usuarios WHERE correo = %s", (correo,))
        user = cursor.fetchone()
        cursor.close()
        db.close()
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
                response = make_response(redirect(url_for('dashboard_guarda', _t=timestamp), code=303))
            else:
                flash('Rol no reconocido', 'danger')
                return redirect(url_for('ingresar'))

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
def dashboard_admin():
    if 'pkiduser' not in session:
        flash('Debes iniciar sesión primero', 'danger')
        return redirect(url_for('ingresar'))
        
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

    cursor.execute("SELECT COUNT(*) FROM cartera where estado = 'Mora'")
    mora = cursor.fetchone()[0]

    cursor.close()
    db.close()

    response = make_response(render_template('admin/dashboard_admin.html',
                                             correspondencia_count=correspondencia_count,
                                             parqueadero_count=parqueadero_count,
                                             multas_count=multas_count,
                                             paz_y_salvo=paz_y_salvo,
                                             mora=mora))
    
    # Agregar cabeceras para evitar caché
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    
    return response

@app.route('/admin/usuarios', methods=['GET'])
def usuarios():
    db = get_db_connection()
    cursor = db.cursor()

    sql = """
        SELECT u.pkiduser, u.nombre, u.cedula, u.celular, u.correo, u.rol_id, r.nombrerol 
        FROM usuarios u
        LEFT JOIN rol r ON u.rol_id = r.pkidrol
    """
    cursor.execute(sql)
    columnas = [col[0] for col in cursor.description]  # Obtener los nombres de las columnas
    usuarios = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]  # Convertir a diccionario

    cursor.execute("SELECT pkidrol, nombrerol FROM rol")
    columnas_roles = [col[0] for col in cursor.description]
    roles = [dict(zip(columnas_roles, fila)) for fila in cursor.fetchall()]

    cursor.close()
    db.close()

    return render_template('admin/usuarios.html', usuarios=usuarios, roles=roles)
    
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

#@app.route('/admin/usuarios/editar/<int:pkiduser>')
#def obtener_usuario(pkiduser):
#    db = get_db_connection()
#    cursor = db.cursor()
#    cursor.execute("SELECT * FROM usuarios WHERE pkiduser = %s", (pkiduser,))
#    usuario = cursor.fetchone()
#    db.close()

#    if not usuario:
#        return "Usuario no encontrado", 404

#    return render_template('admin/usuarios.html', usuario=usuario)

#@app.route('/admin/usuarios/actualizar/<int:pkiduser>', methods=['POST'])
#def actualizar_usuario(pkiduser):
    #if request.method == 'POST':
    #    nombre = request.form['nombre']
    #    cedula = request.form['cedula']
    #    celular = request.form['celular']
    #    correo = request.form['correo']
    #    rol_id = request.form['rol_id']

    #    db = get_db_connection()
    #    cursor = db.cursor()
    #    cursor.execute("""
    #        UPDATE usuarios 
    #        SET nombre=%s, cedula=%s, celular=%s, correo=%s, rol_id=%s 
    #        WHERE pkiduser=%s
    #    """, (nombre, cedula, celular, correo, rol_id, pkiduser))
    #    db.commit()
    #    db.close()

#        return redirect(url_for('usuarios'))

# Eliminar usuario
#@app.route('/admin/usuarios/eliminar/<int:pkiduser>', methods=['DELETE'])
#def eliminar_usuario(pkiduser):
#    db = get_db_connection()
#    cursor = db.cursor()
#    cursor.execute("DELETE FROM usuarios WHERE pkiduser=%s", (pkiduser,))
#    db.commit()
#    cursor.close()
#    db.close()

#    return jsonify({"mensaje": "Usuario eliminado correctamente"})
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

    # Si es una petición GET, recupera los datos del usuario
    cursor.execute("SELECT * FROM usuarios WHERE pkiduser = %s", (pkiduser,))
    usuario = cursor.fetchone()
    db.close()

    return redirect(url_for('usuarios')) 


@app.route('/inmuebles')
def Inmuebles():
    return "Página de Inmuebles"

@app.route('/residentes')
def Residentes():
    return "Página de Residentes"

@app.route('/trabajadores')
def Trabajadores():
    return "Página de Trabajadores"

@app.route('/multas')
def Multas():
    return "Página de Multas"

@app.route('/cartera')
def Cartera():
    return "Página de Cartera"

@app.route('/visitantes')
def Visitantes():
    return "Página de Visitantes"

@app.route('/parqueadero')
def Parqueadero():
    return "Página de Parqueadero"

@app.route('/dashboard_guarda')
def dashboard_guarda():
    return 'pagina guarda'

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