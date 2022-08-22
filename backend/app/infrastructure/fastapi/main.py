import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from app.infrastructure.database.db_class import TestTable
from app.infrastructure.database.db_conn import engineconn

app = FastAPI()
engine = engineconn()
session = engine.sessionmaker()


@app.get("/")
async def root():
    message = session.query(TestTable).all()[0]
    return message


if __name__ == "__main__":
    # init_db()

    uvicorn.run(
        "app.infrastructure.fastapi.main:app", host="0.0.0.0", port=8000, reload=True
    )

    from fastapi import FastAPI
