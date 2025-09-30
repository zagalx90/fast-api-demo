from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Health(BaseModel):
    status: str = "ok"

@app.get("/")
def root():
    return {"message": "Hola Antonio"}

@app.get("/health", response_model=Health)
def health():
    return Health()
