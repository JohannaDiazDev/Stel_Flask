from models import db

class Role(db.Model):
    __tablename__ = 'role'  # Nombre exacto de la tabla en PostgreSQL

    pkidrol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombrerol = db.Column(db.String(50), nullable=False, unique=True)

    # Relación con Usuario (debe coincidir el nombre en Usuario)
    usuarios = db.relationship('Usuarios', back_populates='role', lazy=True)
    trabajador = db.relationship('Trabajador', back_populates = 'role')
    residente = db.relationship('Residente', back_populates='role')

class Usuarios(db.Model):
    __tablename__ = 'usuarios'  # Nombre exacto de la tabla en PostgreSQL

    pkiduser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rol_id = db.Column(db.Integer, db.ForeignKey('role.pkidrol'), nullable=False)
    cedula = db.Column(db.String(12), unique=True, nullable=False)
    correo = db.Column(db.String(50), unique=True, nullable=False)
    contraseña = db.Column(db.String(15), nullable=False)
    celular = db.Column(db.String(15), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)

    # Relación con Role (asegúrate de que el nombre coincida con el back_populates en Role)
    role = db.relationship('Role', back_populates='usuarios')
    residente = db.relationship('Residente', back_populates='usuarios')
    trabajador = db.relationship('Trabajador', back_populates='usuarios')
    def __repr__(self):
        return f"<Usuarios {self.nombre}>"

class Trabajador(db.Model):
    __tablename__ = 'trabajador'

    pkidtrabajador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.pkiduser'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('role.pkidrol'), nullable=False)
    empresa = db.Column(db.String(30), nullable=False)
    cargo = db.Column(db.String(30), nullable=False)

    # Solo mantenemos el backref en Role
    role = db.relationship('Role', back_populates='trabajador')
    usuarios = db.relationship('Usuarios', back_populates='trabajador')
    correspondencias = db.relationship('Correspondencia', backref='trabajador_ref', lazy=True)
    
    # La relación con Usuarios ya se maneja con backref en la otra tabla

    def __repr__(self):
        return f'<Trabajador {self.pkidtrabajador}, Usuarios {self.usuario_id}, Role {self.rol_id}>'

class Inmueble(db.Model):
    __tablename__ = 'inmueble'

    pkidinmueble = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numeroinmueble = db.Column(db.Integer, nullable=False)
    anden = db.Column(db.Integer, nullable=False)
    
    # Relación corregida
    residentes = db.relationship('Residente', back_populates='inmueble', lazy=True)
    correspondencias = db.relationship('Correspondencia', backref='inmueble_ref', lazy=True)

    def __repr__(self):
        return f'<Inmueble {self.pkidinmueble}, Numero {self.numeroinmueble}>'

class Residente(db.Model):
    __tablename__ = 'residente'

    pkidresidente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.pkiduser'), nullable=False)
    inmueble_id = db.Column(db.Integer, db.ForeignKey('inmueble.pkidinmueble'), nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('role.pkidrol'), nullable=False)

    usuarios = db.relationship('Usuarios', back_populates='residente') 
    inmueble = db.relationship('Inmueble', back_populates='residentes')
    role = db.relationship('Role', back_populates='residente')

    def __repr__(self):
        return f'<Residente {self.pkidresidente}, Usuarios {self.usuarios.nombre}, Inmueble {self.inmueble.numeroinmueble}, Role {self.role.nombre}>'
    
class Visitante(db.Model):
    __tablename__ = 'visitante'

    pkidvisitante = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(30), unique=True, nullable=False)
    cedula = db.Column(db.String(15), unique=True, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    autorizado = db.Column(db.Boolean, nullable=False)
    ingresa_carro = db.Column(db.Boolean, nullable=False)
    inmueble_id = db.Column(db.Integer, db.ForeignKey('inmueble.pkidinmueble'), nullable=False)
    residente_id = db.Column(db.Integer, db.ForeignKey('residente.pkidresidente'), nullable=False)

    inmueble = db.relationship('Inmueble',backref=db.backref('visitante', lazy=True))
    residente = db.relationship('Residente',backref=db.backref('visitante', lazy=True))

    def __repr__(self):
        return f'<Visitante {self.pkidvisitante}, Inmueble {self.inmueble.numeroinmueble}, Residente {self.residente.nombre}'

class Estado_cartera(db.Model):
    __tablename__ = 'estado_cartera'

    pkidestado = db.Column(db.Integer, primary_key =True, autoincrement = True)
    trabajador_id = db.Column(db.Integer, db.ForeignKey('trabajador.pkidtrabajador'), nullable=False)
    fecha_actual = db.Column(db.DateTime, nullable=False)
    saldo = db.Column(db.Integer, nullable=False)
    inmueble_id = db.Column(db.Integer, db.ForeignKey('inmueble.pkidinmueble'),nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    observaciones = db.Column(db.Text,nullable=False)

    trabajador = db.relationship('Trabajador',backref=db.backref('estado_cartera',lazy=True))
    inmueble = db.relationship('Inmueble',backref=db.backref('estado_cartera',lazy=True))

    def __repr__(self):
        return f'<Estado_cartera {self.pkidestado}, Trabajador {self.trabajador.nombre},Inmueble {self.inmueble.numeroinmueble}'

class Multa(db.Model):
    __tablename__ = 'multa'

    pkidmulta = db.Column(db.Integer, primary_key = True, autoincrement=True)
    trabajador_id = db.Column(db.Integer, db.ForeignKey('trabajador.pkidtrabajador'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    inmueble_id = db.Column(db.Integer, db.ForeignKey('inmueble.pkidinmueble'), nullable=False)
    fecha_pago = db.Column(db.DateTime, nullable=True)
    tipo = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Integer, nullable=False)

    trabajador = db.relationship('Trabajador',backref=db.backref('multa',lazy=True)) 
    inmueble = db.relationship('Inmueble',backref=db.backref('multa',lazy=True))
    
    def __repr__(self):
        return f'<Multa {self.pkidmulta},Trabajador {self.trabajador.nombre},Inmueble {self.inmueble.numeroinmueble}'

class Parqueadero(db.Model):
    __tablename__ = 'parqueadero'

    pkidparqueadero = db.Column(db.Integer, primary_key = True, autoincrement=True)
    cupo = db.Column(db.Integer, nullable=False)
    tarifa = db.Column(db.Integer, nullable=False)
    residente_id = db.Column(db.Integer,db.ForeignKey('residente.pkidresidente'))
    visitante_id = db.Column(db.Integer, db.ForeignKey('visitante.pkidvisitante'))
    estado = db.Column(db.Boolean, nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    tipo = db.Column(db.String(10),nullable=False)
    placa = db.Column(db.String(5),nullable=False)

    residente = db.relationship('Residente',backref=db.backref('parqueadero',lazy=True))
    visitante = db.relationship('Visitante',backref=db.backref('parqueadero',lazy=True))

    def __repr__(self):
        return f'<Parqueadero {self.pkidparqueadero},Residente {self.residente.cedula}, Visitante {self.visitante.cedula}'

class Correspondencia(db.Model):
    __tablename__ = 'correspondencia'

    pkidcorrespondencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    inmueble_id = db.Column(db.Integer, db.ForeignKey('inmueble.pkidinmueble'))
    trabajador_id = db.Column(db.Integer, db.ForeignKey('trabajador.pkidtrabajador'))
    tipo = db.Column(db.String(50), nullable=False)
    fecha_recibido = db.Column(db.DateTime, nullable=True)
    fecha_entrega = db.Column(db.DateTime, nullable=True)
    estado = db.Column(db.String(20),nullable=False)
    observaciones = db.Column(db.Text,nullable=False)

    trabajador = db.relationship('Trabajador', backref='trabajador_correspondencias')  
    inmueble = db.relationship('Inmueble', backref='inmueble_correspondencias')
    def __repr__(self):
        return f'<Correspondencia {self.pkidcorrespondencia},Inmueble {self.inmueble.numeroinmueble},Trabajador {self.trabajador.nombre}'

class Novedades(db.Model):
    __tablename__ = 'novedades'
    pkidnovedad = db.Column(db.Integer, primary_key= True, autoincrement=True)        
    inmueble_id = db.Column(db.Integer, db.ForeignKey('inmueble.pkidinmueble'), nullable = True)
    trabajador_id = db.Column(db.Integer, db.ForeignKey('trabajador.pkidtrabajador'))
    fecha = db.Column(db.DateTime, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    asunto = db.Column(db.String(40), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(20), nullable=False)

    inmueble = db.relationship('Inmueble',backref = db.backref('novedades',lazy=True))
    trabajador = db.relationship('Trabajador',backref=db.backref('novedades',lazy=True))

    def __repr__(self):
        return f'<Novedades {self.pkidnovedad},Inmueble {self.inmueble.numeroinmueble},Trabajador {self.trabajador.nombre}'