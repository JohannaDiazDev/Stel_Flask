from flask_bcrypt import Bcrypt
import MySQLdb

# Conectar a la base de datos
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="stel")
cursor = db.cursor()

bcrypt = Bcrypt()

# Seleccionar los usuarios con contraseñas sin hashear
cursor.execute("SELECT pkiduser, contraseña FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    pkiduser, contraseña_plana = usuario
    
    if not contraseña_plana.startswith("$2b$"):  # Verificar si ya está hasheada
        hash_nuevo = bcrypt.generate_password_hash(contraseña_plana).decode('utf-8')

        # Actualizar en la base de datos
        cursor.execute("UPDATE usuarios SET contraseña = %s WHERE pkiduser = %s", (hash_nuevo, pkiduser))

# Guardar cambios
db.commit()
cursor.close()
db.close()

print("✅ Contraseñas actualizadas correctamente.")