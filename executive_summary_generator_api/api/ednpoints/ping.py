from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
def ping():
    """ A test endpoint that returns a test response to check if app is alive """
    return {"message": "pong"}
