from sqlalchemy import create_engine

from settings import DATABASE_NAME, DATABASE_USERNAME, DATABASE_PASSWORD

engine = create_engine('postgresql://{0}:{1}@localhost:5433/{2}'.format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_NAME))
print(engine)