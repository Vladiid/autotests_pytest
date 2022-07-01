from pydantic import BaseModel, validator


class Post(BaseModel):
    bookingid: int

    @validator("bookingid")
    def check(cls, v):
        if v > 100000:
            raise ValueError('Is not less than 2200')
        else:
            return v


class Post_R(BaseModel):
    text: str
    number: int
    type: str




