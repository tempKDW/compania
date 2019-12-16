from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./compania.db'
SQLALCHEMY_TEST_DATABASE_URL = 'sqlite:///./test_compania.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

test_engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL, connect_args={'check_same_thread': False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

