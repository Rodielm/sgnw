
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/")
async def read_argument():
    return [{"name": "argument Foo"}, {"name": "argument Bar"}]


@router.get("/{argument_id}")
async def read_argument(argument_id: str):
    return {"name": "Fake Specific argument", "argument_id": argument_id}


@router.put(
    "/{argument_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_argument(argument_id: str):
    if argument_id != "foo":
        raise HTTPException(status_code=403, detail="You can only update the argument: foo")
    return {"argument_id": argument_id, "name": "The Fighters"}