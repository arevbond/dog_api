import uvicorn
from fastapi import FastAPI
from database.database import engine, SessionLocal
from database.models import Base



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "success"}


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(app, host="0.0.0.0", port=8000)
