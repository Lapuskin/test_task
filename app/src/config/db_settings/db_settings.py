from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://root:test@localhost/test"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

metadata = MetaData()
metadata.bind = engine

SessionLocal = Session()