from fastapi import FastAPI

from app.Controller import TestController, SessionController, UserController, ProductController

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

app.include_router(
    ProductController.router,
    prefix="/product",
    tags=["product methods"],
    responses={400: {"description": "Error Bad Request"}}
)

app.include_router(
    SessionController.router,
    prefix="/session",
    tags=["session methods"],
    responses={400: {"description": "Error Bad Request"}}
)
