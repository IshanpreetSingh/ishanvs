from pydantic import BaseModel

class WordBase(BaseModel):
    word: str
    rating: str

class WordCreate(WordBase):
    pass

class Word(WordBase):
    id: int

    class Config:
        orm_mode = True