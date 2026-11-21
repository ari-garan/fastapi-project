from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int

    model_config = ConfigDict(from_attributes=True)