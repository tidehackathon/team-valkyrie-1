from fastapi import FastAPI

from api.ednpoints import router

app = FastAPI()
app.include_router(router)
