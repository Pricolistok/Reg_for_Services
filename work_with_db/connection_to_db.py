from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.models import database


def connection_db():
    engine = create_engine('sqlite:///database.db', echo=True)
    database.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)
    return session


def close_connection_db(session):
    session.commit()
    session.close()


def main():
    pass

if __name__  ==  '__main__':
    main()