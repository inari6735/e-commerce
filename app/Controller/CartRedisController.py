import traceback
from datetime import timedelta

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from redis_om import NotFoundError

from app.Model.CartRedisModel import CartRedisModel, ProductRedisModel, CartRedisResponseModel
from fastapi_redis_session import getSessionId

router = APIRouter()


@router.post("/add", response_model=CartRedisResponseModel)
async def add_product_to_cart(
    product_redis: ProductRedisModel,
    session_id: str = Depends(getSessionId)
):
    success = True
    cart_redis = None

    try:
        if session_id == "" or None:
            raise Exception("Session does not exist")
        cart_redis = CartRedisModel.get(session_id)
        cart_redis.product += [product_redis]
        cart_redis.save()

    except NotFoundError:
        cart_redis = CartRedisModel()
        cart_redis.pk = session_id
        cart_redis.product = [product_redis]
        cart_redis.save()
        cart_redis.expire(timedelta(days=1))

    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))
        success = False

    return jsonable_encoder({"data": cart_redis, "success": success})


@router.get("/get", response_model=CartRedisResponseModel)
async def get_cart(
    session_id: str = Depends(getSessionId)
):
    success = True
    cart_redis = None
    try:
        cart_redis = CartRedisModel.get(session_id)

    except NotFoundError:
        pass

    except Exception as e:
        print(type(e), e)
        print("".join(traceback.TracebackException.from_exception(e).format()))
        success = False

    return jsonable_encoder({"data": cart_redis, "success": success})
