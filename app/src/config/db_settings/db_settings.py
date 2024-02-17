from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/asyncalchemy"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

db = Session()