from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(name=user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_interests_by_user(db: Session, user: models.User):
    return db.query(models.Interest).filter(models.Interest.user == user.id)


def create_interest(db: Session, interest: schemas.InterestCreate):
    db_interest = models.Interest(name=interest.name, user=interest.user_id)
    db.add(db_interest)
    db.commit()
    db.refrest(db_interest)
    return db_interest
