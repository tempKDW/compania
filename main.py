from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

import crud
import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/users/{user_id}', response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail='User not found.')
    return db_user


@app.post('/users/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, user.name)
    if db_user:
        raise HTTPException(status_code=404, detail='user name is already taken.')
    return crud.create_user(db, user)
