import uvicorn
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from database.database import engine
from database.models import Base
from .routers import image, home

from .auth.db import User
from .auth.schemas import UserCreate, UserRead, UserUpdate
from .auth.users import auth_backend, current_active_user, fastapi_users

app = FastAPI()
app.include_router(image.router)
app.include_router(home.router)
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/images", StaticFiles(directory="Images"), name="images")


@app.get("/")
async def root():
    return {"message": "success"}


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    uvicorn.run(app, host="0.0.0.0", port=8000)
