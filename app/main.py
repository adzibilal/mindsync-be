from fastapi import FastAPI
from app.routers import router
from app.database import init

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    await init()

app.include_router(router)