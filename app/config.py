import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://e_shop_user:123456@localhost/e_shop_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False