from pydantic import BaseModel, validator
from src.enums.user_enums import Genders
from src.enums.user_enums import Statuses
from src.enums.user_enums import UserErrors
from src.enums.user_enums import UserID

class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_presented_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)

    @validator('id')
    def check_id_this_a_int(cls, id):
        if id == int:
            return id
        else:
            return ValueError(UserID.WRONG_ID.value)
