from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# Настройки бдшки. Конфиграция, все дела.

DATABASE_URL = "postgresql://root:test@localhost/test"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

metadata = MetaData()
metadata.bind = engine


def get_db():
    '''Метод для доступа к базе данных'''
    db = Session()
    try:
        yield db
    finally:
        db.close()
