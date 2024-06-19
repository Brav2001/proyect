from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: Optional[str] = None
    documento: int
    nombre: str
    apellido: str
    edad: int
    fecha_creacion: Optional[str] = None
    password: Optional[str] = None

    class Config:
        orm_mode = True
