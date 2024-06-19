from fastapi import FastAPI
from routes.users import userRoute

app = FastAPI()

app.include_router(userRoute)
