from typing import List

from app.Class.DatabaseClass import DatabaseClass
from app.Config.config import Config
from app.Model.UserModel import UserModel


class UserRepository:
    def __init__(
        self,
        conf: Config = None,
        db: DatabaseClass = None
    ):
        self.conf = conf,
        self.db = db

    def create_user(
        self,
        user: UserModel
    ):
        query = f"""
            INSERT INTO user
            (
                email,
                password,
                name,
                lastname
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s
            )
        """

        params = (
            user.email,
            user.password,
            user.name,
            user.lastname
        )

        self.db.query(query, params)
