from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import meta, engine

users = Table("users", meta, Column(
    "id", Integer, primary_key=True),
    Column("documento", Integer, nullable=False, unique=True),
    Column("nombre", String(255), nullable=False),
    Column("apellido", String(255), nullable=False),
    Column("edad", Integer, nullable=False),
    Column("fecha_creacion", DateTime),
    Column("password", String(255)))


meta.create_all(engine)
