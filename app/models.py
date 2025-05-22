from pydantic import BaseModel

class RelatedPost(BaseModel):
    id: int
    title: str
