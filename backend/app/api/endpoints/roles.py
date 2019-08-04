
from fastapi import APIRouter
from app.models.rol import (RoleBase, ManyRolesInResponse, RoleInResponse, RoleInDB, RoleInUpdate)
from app.crud import rol as db_role
from fastapi.encoders import jsonable_encoder
from app.core.utils import create_aliased_response
from typing import List

from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

router = APIRouter()

@router.get("/", response_model=List[RoleInResponse])
def read_roles():
    roles = db_role.read_roles()
    return roles


@router.get("/{name}",response_model=RoleInResponse)
def read_rol_by_name(name: str):
    row = db_role.read_role_name(name)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Rol not exist",
                            )
    return row


@router.post("/", status_code=HTTP_201_CREATED)
def create_role(rol: RoleInDB):
    return db_role.create_rol(rol)


@router.put("/{id}")
def update_rol(id:int,rol: RoleInUpdate):
    row = db_role.update_rol(id,rol)
    if not row:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail="Role not exist",
                            )
    return row


@router.delete("/{id}")
def delete_rol(id: int):
    db_role.delete_role(id)
