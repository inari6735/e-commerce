from fastapi import FastAPI

from app.Controller import TestController
from app.Controller import UserController

app = FastAPI(title="e-commerce")

app.include_router(
    TestController.router,
    prefix="/test",
    tags=["test methods"],
    responses={400: {"description": "Error Bad Request"}}
)

app.include_router(
    UserController.router,
    prefix="/user",
    tags=["user methods"],
    responses={400: {"description": "Error Bad Request"}}
)