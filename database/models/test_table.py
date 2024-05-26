from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.connection import Base


class TestTable(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
