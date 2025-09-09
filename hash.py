
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
#70r3n@ residente
#ju4pd* guarda
#Al12@* admin
password = "70r3n@" 
hashed = bcrypt.generate_password_hash(password).decode('utf-8')

print("Hash generado:", hashed)