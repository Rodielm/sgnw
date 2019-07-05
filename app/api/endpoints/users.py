
from fastapi import APIRouter
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)


router = APIRouter()


@router.get("/")
def read_users():
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.get("/{id}")
def find_user(id: int):
    return [{"username": "Foo"}, {"username": "Bar"}]


@router.post("/", status_code=HTTP_201_CREATED)
def create_users(username: str):
    return {"username": "fakecurrentuser"}


@router.put("/{id}")
def update_user(username: str):
    return {"username": username}


@router.delete("/{id}")
def delete_user(username: str):
    return {"username": username}
