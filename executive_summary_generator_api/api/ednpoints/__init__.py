from fastapi import APIRouter

from .generate_short_executive_summary import router as capability_executive_summary
from .generate_short_multidomain_capability_summary import router as capability_summary_router
from .ping import router as ping_router

router = APIRouter()
router.include_router(ping_router)
router.include_router(capability_summary_router)
router.include_router(capability_executive_summary)
