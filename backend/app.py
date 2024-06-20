from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import userRoute
from routes.auth import authRoute
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(userRoute)
app.include_router(authRoute)
