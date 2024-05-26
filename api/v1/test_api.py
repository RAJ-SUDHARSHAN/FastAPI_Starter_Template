from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from database.connection import get_db
from database.models.test_table import TestTable

router = APIRouter()


@router.get("/test_table")
def get_test_table(db: Session = Depends(get_db)):
    return db.query(TestTable).all()
