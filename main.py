from fastapi.responses import ORJSONResponse
from fastapi import FastAPI
from Vacinacao.routes.postos import router as postos_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(default_response_class=ORJSONResponse)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(postos_router)

@app.get("/")
def home():
    index_path = Path ("static/index.html")
    return FileResponse(index_path)
