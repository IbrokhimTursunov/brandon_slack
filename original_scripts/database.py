from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Boolean
from sqlalchemy.exc import NoSuchTableError

from original_scripts.settings import URL_CONNECTION_TO_DATABASE

class Emails:
    def __init__(self):
        engine = create_engine(URL_CONNECTION_TO_DATABASE)
        self.connection = engine.connect()
        self.meta_data = MetaData(bind=self.connection)
        try:
            self.table = Table('emails', self.meta_data, autoload=True, autoload_with=engine)
        except NoSuchTableError:
            self.create_table()
        for rec in self.table.columns:
            print(rec.name)

    def create_table(self):
        self.table = Table('emails', self.meta_data,
                              Column('id', Integer, primary_key=True),
                              Column('email', String),
                              Column('unused', Boolean),
                              Column('status', String),
                              Column('code', String))
        self.meta_data.create_all(self.connection)

    def mark_as_used(self, email, unused=False):
        statement = self.table.update().values(unused=unused).where(self.table.c.email == email)
        self.connection.execute(statement)

    def email_exists(self, email):
        statement = self.table.select().where(self.table.c.email == email)
        return bool(self.connection.execute(statement).fetchall())

    def insert_record(self, email, unused=True, status='', code=''):
        if self.email_exists(email):
            return None
        else:
            statement = self.table.insert().values(email=email, unused=unused, status=status, code=code)
            self.connection.execute(statement)

    def insert_records(self, emails):
        for email in emails:
            self.insert_record(email)

    def get_entire_table(self):
        statement = self.table.select()
        return self.connection.execute(statement).fetchall()

    def get_all_unused_emails(self):
        t = self.get_entire_table()
        return [row[1] for row in t if row[2]]


if __name__ == "__main__":
    pass
    # Emails().update_record_where('')



