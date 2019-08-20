from fastapi import APIRouter

from .endpoints.login import router as login_router
from .endpoints.users import router as users_router
from .endpoints.roles import router as roles_router
from .endpoints.apps import router as apps_router
from .endpoints.languages import router as lang_router
from .endpoints.groups import router as group_router
from .endpoints.notifications import router as noti_router


router = APIRouter()

router.include_router(login_router, prefix="/login", tags=["Login"])
router.include_router(users_router, prefix="/users", tags=["Users"])
router.include_router(roles_router, prefix="/roles", tags=["Roles"])
router.include_router(group_router, prefix="/groups", tags=["Group"])
router.include_router(apps_router, prefix="/apps", tags=["Apps"])
router.include_router(noti_router, prefix="/noti", tags=["Notifications"])
router.include_router(lang_router, prefix="/langs", tags=["Languages"])
