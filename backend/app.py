from fastapi import FastAPI
from routes.users import userRoute
from routes.auth import authRoute

app = FastAPI()

app.include_router(userRoute)
app.include_router(authRoute)
