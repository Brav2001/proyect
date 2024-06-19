from fastapi import FastAPI, Header, HTTPException, Depends, APIRouter
import jwt
from jwt import PyJWTError
from typing import Optional
from config.db import conn
from models.user import users
from schemas.user import User
from datetime import datetime
import bcrypt


userRoute = APIRouter()

SECRET_KEY = "SECRET"  
ALGORITHM = "HS256"  
ACCESS_TOKEN_EXPIRE_MINUTES = 1600


def verify_token(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Token missing")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")

    token = authorization.split("Bearer ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload.get("sub")
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")




@userRoute.get("/users", response_model=list[dict], status_code=200)
def get_users(current_user: str = Depends(verify_token)):
    try:
        user_records = conn.execute(users.select()).fetchall()
        users_list = []
        for user in user_records:
            user_dict = {
                "id": str(user.id) if user.id is not None else None,
                "nombre": user.nombre,
                "apellido": user.apellido,
                "documento": user.documento,
                "edad": user.edad,
                "fecha_creacion": str(user.fecha_creacion)
            }
            users_list.append(user_dict)

        return users_list
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to retrieve users: {str(e)}")


@userRoute.get("/users/{id}", response_model=dict, status_code=200)
def get_user(id: str, current_user: str = Depends(verify_token)):
    try:
        result = conn.execute(users.select().where(users.c.id == id)).first()
        if result:
            res = {
                "id": str(result.id) if result.id is not None else None,
                "nombre": result.nombre,
                "apellido": result.apellido,
                "documento": result.documento,
                "edad": result.edad,
                "fecha_creacion": str(result.fecha_creacion)
            }

            return res
        else:
            raise HTTPException(
                status_code=404, detail=f"Failed to retrieve user: Not Found")
    except Exception as e:
        raise HTTPException(
            status_code=404, detail=f"Failed to retrieve user: {str(e)}")


@userRoute.post("/users", response_model=User, status_code=201)
def create_user(user: User, current_user: str = Depends(verify_token)):
    try:
        new_user = {
            "nombre": user.nombre,
            "apellido": user.apellido,
            "documento": user.documento,
            "edad": user.edad,
            "fecha_creacion": datetime.now(),
            "password": bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        }

        result = conn.execute(users.insert().values(new_user))
        conn.commit()
        inserted_user = conn.execute(users.select().where(
            users.c.id == result.lastrowid)).first()
        return User(
            id=str(inserted_user.id),
            nombre=inserted_user.nombre,
            apellido=inserted_user.apellido,
            documento=inserted_user.documento,
            edad=inserted_user.edad,
            fecha_creacion=str(inserted_user.fecha_creacion),
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to register user: {str(e)}")


@userRoute.put("/users/{id}",  response_model=User, status_code=200)
def get_user(id: str, user: User, current_user: str = Depends(verify_token)):
    try:
        find = conn.execute(users.select().where(users.c.id == id)).first()

        if find:

            conn.execute(users.update().values(
                nombre=user.nombre,
                apellido=user.apellido,
                documento=user.documento,
                edad=user.edad,
                password=bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')).where(users.c.id == id))
            conn.commit()
            result = conn.execute(users.select().where(
                users.c.id == id)).first()
            return User(
                id=str(result.id),
                nombre=result.nombre,
                apellido=result.apellido,
                documento=result.documento,
                edad=result.edad,
                fecha_creacion=str(result.fecha_creacion),
            )
        else:
            raise HTTPException(
                status_code=404, detail=f"User don't exists")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to updated user: {str(e)}")


@userRoute.delete("/users/{id}",  status_code=204)
def get_user(id: str, current_user: str = Depends(verify_token)):
    try:
        conn.execute(users.delete().where(users.c.id == id))
        conn.commit
        return
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to delete user: {str(e)}")
