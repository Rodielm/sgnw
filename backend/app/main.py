
from fastapi import Depends, FastAPI, Header, HTTPException
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from app.api.api import router as api_router
from app.db.settings import init
from app.core import config

app = FastAPI(config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", init)
app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
