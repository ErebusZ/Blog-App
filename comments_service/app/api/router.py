from fastapi import APIRouter, Depends, HTTPException
from app.api import models, db_utils, request_api


comments_router = APIRouter()


@comments_router.get("/comments/post/{post_id}", response_model=list[models.CommentOut])
async def list_comments_by_post(post_id: int):
    return await db_utils.get_comments_by_post(post_id)


@comments_router.post("/comment/", response_model=models.CommentOut)
async def create_comment(
    comment: models.CommentIn, user_info: dict = Depends(request_api.validate_token)
):
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")
    if comment.user_id != user_info["user_id"]:
        raise HTTPException(
            status_code=403,
            detail="User ID in comment does not match authenticated user",
        )
    comment_id = await db_utils.add_comment(comment)
    return {**comment.dict(), "id": comment_id}


@comments_router.put("/comment/{comment_id}", response_model=models.CommentOut)
async def update_existing_comment(
    comment_id: int,
    comment_update: models.CommentUpdate,
    user_info: dict = Depends(request_api.validate_token),
):
    existing_comment = await db_utils.get_comment(comment_id)
    if existing_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if existing_comment.user_id != user_info["user_id"]:
        raise HTTPException(
            status_code=403, detail="Not authorized to edit this comment"
        )

    update_data = comment_update.dict(exclude_unset=True)
    if "user_id" in update_data and update_data["user_id"] != user_info["user_id"]:
        raise HTTPException(
            status_code=403, detail="Cannot change the user_id of a comment"
        )

    updated_comment = await db_utils.update_comment(comment_id, update_data)
    return updated_comment


@comments_router.delete("/comments/{comment_id}", response_model=dict)
async def delete_existing_comment(
    comment_id: int, user_info: dict = Depends(request_api.validate_token)
):
    existing_comment = await db_utils.get_comment(comment_id)
    if existing_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if existing_comment.user_id != user_info["user_id"]:
        raise HTTPException(
            status_code=403, detail="Not authorized to delete this comment"
        )
    await db_utils.delete_comment(comment_id)
    return {"detail": "Comment deleted"}
