from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.config import POSTGRESURI

engine = create_engine(POSTGRESURI)

session = sessionmaker(bind=engine)
# session = Session(bind=engine)

