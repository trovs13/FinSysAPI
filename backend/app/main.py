from fastapi import FastAPI
from app.database import engine, Base
from app.routers import user, auth

app = FastAPI(title="FinSysAPI")

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "FinSysAPI rodando"}