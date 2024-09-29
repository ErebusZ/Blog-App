import os

from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine
from databases import Database

DATABASE_URL = (
    f"postgresql://{os.environ.get("DB_USER", "comments_user")}:"
    f"{os.environ.get("DB_PASS", "comments_password")}@{os.environ.get("DB_HOST", "localhost")}"
    f"/{os.environ.get("DB_NAME", "comments_db")}"
)

engine = create_engine(DATABASE_URL)
metadata = MetaData()

comments = Table(
    "comments",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("content", String(500)),
    Column("user_id", Integer),
    Column("post_id", Integer),
)

database = Database(DATABASE_URL)
