from fastapi import APIRouter
from fastapi.responses import PlainTextResponse

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def list():
    return PlainTextResponse("respond with a resource")
