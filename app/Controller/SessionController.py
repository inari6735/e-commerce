import random
from datetime import timedelta
from typing import Any
from fastapi import Depends, APIRouter, Request, Response
from fastapi_redis_session import deleteSession, getSession, getSessionId, getSessionStorage, setSession, SessionStorage, basicConfig
from app.Model.SessionModel import SessionRequestModel
from app.Model.CartRedisModel import CartRedisModel

router = APIRouter()

basicConfig(
    redisURL="redis://:Piotrek120@redis:6379/1",
    expireTime=timedelta(days=1),
    )


@router.post("/set")
async def _set_session(
    date: SessionRequestModel,
    request: Request,
    response: Response,
    session_storage: SessionStorage = Depends(getSessionStorage)
):
    session_data = await request.json()
    setSession(response, session_data, session_storage)


@router.get("/get")
async def _get_session(
    session: Any = Depends(getSession)
):
    return session


@router.delete("/delete")
async def _delete_session(
    session_id: str = Depends(getSessionId),
    session_storage: SessionStorage = Depends(getSessionStorage)
):
    cart_redis = CartRedisModel()
    cart_redis.delete(session_id)
    deleteSession(session_id, session_storage)
    return None
