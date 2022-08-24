from sqlalchemy import Column, BIGINT, VARCHAR
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TestTable(Base):
    __tablename__ = 'test_table'
    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    message = Column(VARCHAR, nullable=False)