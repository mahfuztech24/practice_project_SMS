from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL ="mysql+pymysql://root:root@localhost:3306/students"
#DATABASE_URL = "postgresql+psycopg2://training_h90n_user:s7aDpCDO3U5OjoFt0rAz4geTDwsf8FVC@dpg-dbbfmqc9v7es73f33rq0-a.oregon-postgres.render.com/training_h90n"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
      