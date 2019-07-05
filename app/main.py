
from fastapi import Depends, FastAPI, Header, HTTPException

from app.api.api import router as api_router
from app.db.settings import init


app = FastAPI()

app.add_event_handler("startup",init)
app.include_router(api_router,prefix="/api")

