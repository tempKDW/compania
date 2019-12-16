from typing import List

from pydantic import BaseModel


class InterestBase(BaseModel):
    name: str


class InterestCreate(InterestBase):
    user_id: int


class Interest(InterestBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    interests: List[Interest] = []

    class Config:
        orm_mode = True
