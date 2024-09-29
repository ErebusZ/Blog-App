from fastapi import APIRouter, HTTPException

from app.api import models, db_utils


comments_router = APIRouter()

@comments_router.get("/comments/{comment_id}", response_model=models.CommentOut)
async def read_comment(comment_id: int):
    comment = await db_utils.get_comment(comment_id)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@comments_router.get("/comments/posts/{post_id}", response_model=list[models.CommentOut])
async def read_comments_by_post(post_id: int):
    return await db_utils.get_comments_by_post(post_id)


@comments_router.get("/comments/users/{user_id}", response_model=list[models.CommentOut])
async def read_comments_by_user(user_id: int):
    return await db_utils.get_comments_by_user(user_id)
    

@comments_router.post("/comments/", response_model=models.CommentOut)
async def create_comment(comment: models.CommentIn):
    comment_id = await db_utils.add_comment(comment)
    return {**comment.dict(), "id": comment_id}


@comments_router.put("/comments/{comment_id}", response_model=models.CommentOut)
async def update_existing_comment(comment_id: int, comment: models.CommentIn):
    updated_comment = await db_utils.update_comment(comment_id, comment)
    if updated_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {**comment.dict(), "id": comment_id}


@comments_router.delete("/comments/{comment_id}", response_model=dict)
async def delete_existing_comment(comment_id: int):
    deleted_comment = await db_utils.delete_comment(comment_id)
    if deleted_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"detail": "Comment deleted"}

