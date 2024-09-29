from app.api import models
from app.api import db


async def add_comment(payload):
    query = models.comments.insert().values(
        content=payload.content,
        user_id=payload.user_id,
        post_id=payload.post_id
    )
    return await db.database.execute(query=query)


async def get_comments_by_post(post_id: int):
    query = models.comments.select().where(models.comments.c.post_id == post_id)
    return await db.database.fetch_all(query=query)

async def get_comments_by_user(user_id: int):
    query = models.comments.select().where(models.comments.c.post_id == user_id)
    return await db.database.fetch_all(query=query)

async def get_comment(id: int):
    query = models.comments.select().where(models.comments.c.id == id)
    return await db.database.fetch_one(query=query)

async def delete_comment(id: int):
    query = models.comments.delete().where(models.comments.c.id == id)
    return await db.database.execute(query=query)

async def delete_comments_by_post(post_id: int):
    query = models.comments.delete().where(models.comments.c.post_id == post_id)
    return await db.database.execute(query=query)

async def update_comment(id: int, payload):
    query = (
        models.comments.update()
        .where(models.comments.c.id == id)
        .values(
            content=payload.content,
            user_id=payload.user_id,
            post_id=payload.post_id
        )
    )
    return await db.database.execute(query=query)
