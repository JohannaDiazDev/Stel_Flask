"""import mysql.connector
import bcrypt

# Conéctate a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_password",
    database="ruralic"
)
cursor = conexion.cursor()

# Usuario que solicitó el cambio de contraseña
email_usuario = "usuario@example.com"

# Nueva contraseña a hashear
nueva_contraseña = "nuevaClave123".encode('utf-8')
nuevo_hash = bcrypt.hashpw(nueva_contraseña, bcrypt.gensalt(12)).decode()

# Actualiza la contraseña en la base de datos
cursor.execute("UPDATE usuarios SET password_hash = %s WHERE email = %s", (nuevo_hash, email_usuario))

conexion.commit()
cursor.close()
conexion.close()"""
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = "ju4pd*" 
hashed = bcrypt.generate_password_hash(password).decode('utf-8')

print("Hash generado:", hashed)