from fastapi import FastAPI

from app.Controller import SessionController, UserController, ProductController, CartRedisController

app = FastAPI(title="e-commerce")


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

app.include_router(
    CartRedisController.router,
    prefix="/cart_redis",
    tags=["cart_redis methods"],
    responses={400: {"description": "Error Bad Request"}}
)
