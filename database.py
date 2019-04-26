from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Boolean

from settings import URL_CONNECTION_TO_DATABASE

class Emails:
    def __init__(self):
        engine = create_engine(URL_CONNECTION_TO_DATABASE)
        self.connection = engine.connect()
        self.meta_data = MetaData(bind=self.connection)
        # self.create_table()
        self.table = Table('emails')

    def create_table(self):
        Table('emails', self.meta_data,
              Column('id', Integer, primary_key=True),
              Column('email', String),
              Column('unused', Boolean),
              Column('status', String),
              Column('code', String))
        self.meta_data.create_all(self.connection)

    def update_record_where(self, email, unused=True, status='', code=''):
        table = Table('emails', self.meta_data)
        table.insert(values=(email, unused, status, code))

    def all_unused_emails(self):
        pass

    def make_email_used(self, email):
        pass

if __name__ == "__main__":
    Emails().update_record_where('')



