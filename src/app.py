from fastapi.applications import FastAPI
from src.api import router
from src.settings import settings

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        'app:app',
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
