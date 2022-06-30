from fastapi import APIRouter
from .fileoperation import router as fileoperations_router
from .auth import router as auth_router


router = APIRouter()
router.include_router(auth_router)
router.include_router(fileoperations_router)