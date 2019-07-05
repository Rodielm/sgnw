
from fastapi import Depends, FastAPI, Header, HTTPException

from app.routers.users import router as api_router

app = FastAPI()

app.include_router(api_router)

