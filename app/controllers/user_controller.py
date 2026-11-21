from sqlalchemy.orm import Session

from app.services import user_service
from app.schemas.user import UserCreate, UserUpdate


def create_user(db: Session, user: UserCreate):
    return user_service.create_user(db, user)


def get_all_users(db: Session):
    return user_service.get_all_users(db)


def get_user_by_id(db: Session, user_id: int):
    return user_service.get_user_by_id(db, user_id)


def update_user(db: Session, user_id: int, user_data: UserUpdate):
    return user_service.update_user(db, user_id, user_data)


def delete_user(db: Session, user_id: int):
    return user_service.delete_user(db, user_id)