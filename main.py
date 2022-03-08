from fastapi import FastAPI

from app.Controller import TestController

app = FastAPI(title="e-commerce")

app.include_router(
    TestController.router,
    prefix="/test",
    tags=["test methods"],
    responses={400: {"description": "Error Bad Request"}}
)