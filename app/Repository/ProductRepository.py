from app.Class.DatabaseClass import DatabaseClass
from app.Config.config import Config
from app.Model.ProductModel import ProductModel


class ProductRepository:
    def __init__(
        self,
        conf: Config = None,
        db: DatabaseClass = None
    ):
        self.conf = conf,
        self.db = db

    def get_products(
        self
    ):
        query = f"""
            SELECT
                p.product_code,
                p.name,
                p.price,
                p.quantity,
                p.date_add
            FROM product AS p
        """

        return self.db.query_to_array(query)

    def get_product(
        self,
        product_id: int
    ):
        query = f"""
            SELECT
                p.product_code,
                p.name,
                p.price,
                p.quantity,
                p.date_add
            FROM product AS p
            WHERE p.id = %s
        """

        params = (
            product_id,
        )

        return self.db.get_row(query, params)

    def create_product(
        self,
        product_data: ProductModel
    ):
        query = f"""
            INSERT INTO product
            (
                product_code,
                name,
                price,
                quantity
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
            product_data.product_code,
            product_data.name,
            product_data.price,
            product_data.quantity,
        )

        self.db.query(query, params)

    def update_product(
        self,
        product_id: int,
        product_data: ProductModel
    ):
        query = f"""
                    UPDATE product
                    SET
                        product_code = %s,
                        name = %s,
                        price = %s,
                        quantity = %s
                    WHERE id = %s
                """

        params = (
            product_data.product_code,
            product_data.name,
            product_data.price,
            product_data.quantity,
            product_id
        )

        self.db.query(query, params)

    def delete_product(
        self,
        product_id: int
    ):
        query = f"""
                    DELETE FROM product
                    WHERE id = %s
                """

        self.db.query(query, (product_id,))
