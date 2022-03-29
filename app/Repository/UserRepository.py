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

    def get_user_by_id(
        self,
        user_id: int
    ):
        query = f"""
            SELECT
                u.email,
                u.name,
                u.lastname,
                u.date_add
            FROM
                user AS u
            WHERE
                u.id = %s
        """

        params = (user_id,)

        return self.db.get_row(query, params)

    def get_users(
        self,
    ):
        query = f"""
            SELECT
                u.email,
                u.name,
                u.lastname,
                u.date_add
            FROM
                user AS u
        """

        return self.db.query_to_array(query)

    def update_user(
        self,
        user_id: int,
        user_data: UserModel
    ):
        query = f"""
            UPDATE user
            SET
                email = %s,
                password = %s,
                name = %s,
                lastname = %s
            WHERE
                id = %s
        """

        params = (
            user_data.email,
            user_data.password,
            user_data.name,
            user_data.lastname,
            user_id
        )

        self.db.query(query, params)

    def delete_user(
        self,
        user_id: int
    ):
        query = f"""
            DELETE FROM user
            WHERE id = %s
        """

        params = (user_id,)

        self.db.query(query, params)
