
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers.general import router

app = FastAPI(title="LiSAH - MongoDB API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"mensaje": "Exito"}
