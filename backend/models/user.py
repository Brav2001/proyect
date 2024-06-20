from sqlalchemy import Table, Column, select
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.exc import IntegrityError
from config.db import meta, engine
import bcrypt
from datetime import datetime

users = Table("users", meta, Column(
    "id", Integer, primary_key=True),
    Column("documento", Integer, nullable=False, unique=True),
    Column("nombre", String(255), nullable=False),
    Column("apellido", String(255), nullable=False),
    Column("edad", Integer, nullable=False),
    Column("fecha_creacion", DateTime),
    Column("password", String(255)))


meta.create_all(engine)


def insert_user(documento, nombre, apellido, edad, password):
    try:
        # Intentar insertar un nuevo usuario
        ins = users.insert().values(
            documento=documento,
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            password=password,
            fecha_creacion=datetime.now()
        )
        conn = engine.connect()
        conn.execute(ins)
        conn.commit()
        conn.close()
        print("Usuario insertado correctamente.")
    except IntegrityError as e:
        # Manejar la excepción de integridad (documento duplicado)
        print(f"Error: No se pudo insertar el usuario. {e.orig}")


documento_base = 111111111
stmt = users.select().where(users.c.documento == documento_base)
conn = engine.connect()
result = conn.execute(stmt)

if result.rowcount == 0:
    insert_user(
        documento=documento_base,
        nombre="Usuario Base",
        apellido="Ejemplo",
        edad=30,
        password=bcrypt.hashpw("password".encode(
            'utf-8'), bcrypt.gensalt()).decode('utf-8')
    )
else:
    print("El usuario base ya existe en la base de datos.")

conn.close()
