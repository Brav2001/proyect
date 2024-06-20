from pydantic import BaseModel, Field


class Auth(BaseModel):
    documento: int
    password: str

    class Config:
        from_attributes = True
