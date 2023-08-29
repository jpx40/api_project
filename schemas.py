from pydantic import BaseModel








class User(BaseModel):
    id: int
    user: str

    class Config:
        from_attributes = True
