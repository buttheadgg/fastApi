from fastapi import FastAPI

from app import api

app = FastAPI(
    title='API',
    description='Post, get and delete files'
)
app.include_router(api.router)


