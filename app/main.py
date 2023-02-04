import uvicorn
from fastapi import FastAPI
from database.database import engine
from database.models import Base
from .routers import image

# from dependencies import *

app = FastAPI()
app.include_router(image.router)


@app.get("/")
async def root():
    return {"message": "success"}


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(app, host="0.0.0.0", port=8000)
