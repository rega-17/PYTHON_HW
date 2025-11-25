# conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base

TEST_DATABASE_URL = "postgresql://postgres:SQL1@localhost:5432/mydatabase"

@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    yield session
    
    session.rollback()
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
    session.commit()
    session.close()
