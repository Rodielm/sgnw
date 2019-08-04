
from fastapi import Depends, FastAPI, Header, HTTPException
import uvicorn

from app.api.api import router as api_router
from app.db.settings import init

# from fastapi.security import OAuth2PasswordBearer
# uvicorn app.main:app --reload
app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
# @app.get("/items/")
# async def read_items(token:str = Depends(oauth2_scheme)):
#     return {"token": token}

app.add_event_handler("startup", init)
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
