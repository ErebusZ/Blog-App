from pydantic import BaseModel


class Comment(BaseModel):
    content: str
    user_id: int
    post_id: int


class CommentIn(BaseModel):
    content: str
    user_id: int
    post_id: int


class CommentOut(CommentIn):
    id: int
    user_id: int


class CommentUpdate(CommentIn):
    content: str | None
    user_id: int | None
    post_id: int | None
