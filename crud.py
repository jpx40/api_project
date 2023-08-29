
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import select

import schemas
import models
#import sql_tool

session = Session(engine)


result = session.execute(select(models.User)).all()

print(result)
"""
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
"""