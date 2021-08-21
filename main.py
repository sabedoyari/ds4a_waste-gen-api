from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import prediction

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost:8080/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(prediction.router)

@app.get("/", tags = ["Principal"])
async def root():
    msg = "Welcome to the API developed in order to analize and predict waste generation for Compañía de Alimentos Doria"

    return {
        msg
    }