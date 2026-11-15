import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import create_engine, text
from routers.auth import router as auth_router

load_dotenv(Path(__file__).parent / ".env")

database_url = os.environ["DATABASE_URL"]

# SQLAlchemy needs the psycopg driver name in the URL.
if database_url.startswith("postgresql://"):
    database_url = database_url.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1,
    )

engine = create_engine(
    database_url,
    connect_args={"sslmode": "require"},
    pool_pre_ping=True,
)

app = FastAPI()
app.include_router(auth_router)


@app.get("/health/db")
def check_database():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database(), current_user")
        ).one()

    return {
        "database": result[0],
        "connected_as": result[1],
    }