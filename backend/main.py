from fastapi import FastAPI
from backend import models, database
from backend.routers import alunos

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="MathTech Lab API")

app.include_router(alunos.router)

@app.get("/")
def root():
    return {"message": "MathTech Lab API ativa"}