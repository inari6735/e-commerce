from pydantic import BaseModel


class SessionRequestModel(BaseModel):
    user_id: int
    lang: str = "pl"
