from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_url = os.getenv("DATABASE_URL")
db_port = os.getenv("DATABASE_PORT")
db_name = os.getenv("DATABASE_NAME")

connection_string = f"mysql+pymysql://{db_user}:{db_password}@{db_url}:{db_port}/{db_name}"

engine = create_engine(connection_string)

meta = MetaData()

conn = engine.connect()
