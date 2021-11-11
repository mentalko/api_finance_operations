from fastapi.applications import FastAPI
from . import api 

app = FastAPI()
app.include_router(api.router)
