from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories import user_repository
from app.schemas.user import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    return user_repository.create_user(db, user)


def get_all_users(db: Session):
    return user_repository.get_all_users(db)


def get_user_by_id(db: Session, user_id: int):
    user = user_repository.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = get_user_by_id(db, user_id)

    update_data = user_data.model_dump(exclude_unset=True)

    if not update_data:
        raise HTTPException(
            status_code=400,
            detail="No update data provided"
        )

    return user_repository.update_user(
        db,
        user,
        update_data
    )


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)

    user_repository.delete_user(db, user)

    return {"message": "User deleted successfully"}