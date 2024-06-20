from fastapi import APIRouter, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from typing import Optional
from datetime import datetime, timedelta
from config.db import conn
from models.user import users
from schemas.auth import Auth
import bcrypt

from dotenv import load_dotenv
import os

load_dotenv()

authRoute = APIRouter()

secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


@authRoute.post("/login", response_model=dict, status_code=200)
def create_user(user: Auth):
    try:

        result = conn.execute(users.select().where(
            users.c.documento == user.documento)).first()

        if not verify_password(user.password, result.password):
            raise
        else:
            access_token_expires = timedelta(
                minutes=access_token_expire_minutes)
            access_token = create_access_token(
                data={"nombre": result.nombre, "documento": result.documento}, expires_delta=access_token_expires
            )
            return {"token": str(access_token)}
    except Exception as e:
        raise HTTPException(
            status_code=401, detail=f"Document or password incorrect: {str(e)}")
