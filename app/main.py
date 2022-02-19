from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote


# creating the models for tables (not needed any more bc of alembic)
# models.Base.metadata.create_all(bind=engine)


# creating a fastapi instance and storing it in the variable app
app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# connecting the app object to the routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# homepage
@app.get("/")
def root():
    return {"message": "welcome to my world"}





