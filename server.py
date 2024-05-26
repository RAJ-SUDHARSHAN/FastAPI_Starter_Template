from contextlib import asynccontextmanager

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1 import test_api
from database.connection import Base, engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    # Code to run on shutdown


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

version = "v1"

prefix = f"/api/{version}"

app.include_router(test_api.router, prefix=prefix)

if __name__ == "__main__":
    uvicorn.run(app, forwarded_allow_ips="*")
