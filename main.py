from fastapi import FastAPI

from routers import entitle

app = FastAPI()

app.include_router(entitle.router)
