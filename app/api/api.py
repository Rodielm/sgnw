from fastapi import APIRouter

from .endpoints.arguments import router as arguments_router
from .endpoints.users import router as users_router


router = APIRouter()

router.include_router(arguments_router)
router.include_router(users_router,prefix="/users")