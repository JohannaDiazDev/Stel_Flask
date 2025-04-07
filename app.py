from flask import Flask, render_template, url_for, jsonify, request, session, flash, redirect
import re
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
import MySQLdb
import pymysql

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
  
            session['loggedin'] = True
            session['pkiduser'] = user[0]
            session['rol_id'] = user[2]

            flash('Inicio de sesión exitoso', 'success')
            

            if session.get('rol_id') == 1:  
                print(f"ROL ID en sesión: {session.get('rol_id')}")
                return redirect(url_for('dashboard_admin'))
            else:
                return redirect(url_for('inicio'))  
        else:
            flash('❌ Credenciales incorrectas', 'danger')
    return render_template('ingresar.html')

@app.route('/admin/dashboard_admin')
def dashboard_admin():
    return render_template('admin/dashboard_admin.html')
@app.route('/usuarios')
def Usuarios():
    return "Página de Usuarios"

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

@app.route('/logout')
def logout():
    session.clear()  # Elimina todos los datos de sesión
    return redirect(url_for('ingresar')) 

if __name__ == '__main__':
    app.run(debug=True)