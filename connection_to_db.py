from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.models import db, User

engine = create_engine('sqlite:///database.db', echo=True)
db.metadata.create_all(engine)
Session = sessionmaker()
session = Session(bind=engine)

new_user = User(name=input('Input name: '), surname=input('Input surname: '), age=12)
session.add(new_user)
session.commit()
session.close()
