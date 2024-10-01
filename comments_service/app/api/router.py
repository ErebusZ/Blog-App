from fastapi import APIRouter, Depends, HTTPException
from app.api import models, db_utils, request_api

comments_router = APIRouter()


@comments_router.get("/comments/post/{post_id}", response_model=list[models.CommentOut])
async def list_comments_by_post(post_id: int):
    """Retrieve all comments for a specific post."""
    return await db_utils.get_comments_by_post(post_id)


@comments_router.post("/comment/", response_model=models.CommentOut)
async def create_comment(
        comment: models.CommentIn, user_info: dict = Depends(request_api.validate_token)
):
    """Create a new comment associated with a post."""
    if not user_info:
        raise HTTPException(status_code=401, detail="Authentication required")

    comment_with_user = models.CommentIn(content=comment.content, post_id=comment.post_id)
    comment_id = await db_utils.add_comment(comment_with_user, user_info["user_id"])

    return models.CommentOut(id=comment_id, **comment.dict())


@comments_router.put("/comment/{comment_id}", response_model=models.CommentOut)
async def update_existing_comment(
        comment_id: int,
        comment_update: models.CommentUpdate,
        user_info: dict = Depends(request_api.validate_token),
):
    """Update an existing comment."""
    existing_comment = await db_utils.get_comment(comment_id)
    if existing_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if existing_comment.user_id != user_info["user_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to edit this comment")

    update_data = comment_update.dict(exclude_unset=True)
    # Ensure user_id cannot be changed
    if "user_id" in update_data:
        raise HTTPException(status_code=403, detail="Cannot change the user_id of a comment")

    updated_comment = await db_utils.update_comment(comment_id, update_data)
    return models.CommentOut(id=comment_id, **updated_comment)


@comments_router.delete("/comments/{comment_id}", response_model=dict)
async def delete_existing_comment(
        comment_id: int, user_info: dict = Depends(request_api.validate_token)
):
    """Delete a comment."""
    existing_comment = await db_utils.get_comment(comment_id)
    if existing_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    if existing_comment.user_id != user_info["user_id"]:
        raise HTTPException(status_code=403, detail="Not authorized to delete this comment")

    await db_utils.delete_comment(comment_id)
    return {"detail": "Comment deleted"}
