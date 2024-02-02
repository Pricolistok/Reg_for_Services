from sqlalchemy import Column, Integer, String, Float, DateTime, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

database = declarative_base()
meta = MetaData()


class User(database):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    login = Column(String)
    password = Column(String)


class Administrator(database):
    __tablename__ = 'administrator'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    age = Column(Integer)
    login = Column(String)
    password = Column(String)


class Services(database):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    type_id = Column(Integer, ForeignKey('type_of_services.id'))
    name_service = Column(String)
    price_service = Column(Float)
    time = Column(DateTime)


class Type_services(database):
    __tablename__ = 'type_of_services'
    id = Column(Integer, primary_key=True)
    type_name = Column(String)
    administrator_id = Column(Integer, ForeignKey('administrator.id'))


class Information_of_services(database):
    __tablename__ = 'information_about_services'
    id = Column(Integer, primary_key=True)
    time = Column(DateTime)
    duration = Column(DateTime)
    service_id = Column(Integer, ForeignKey('services.id'))
    amount_all = Column(Integer)
    amount_now = Column(Integer)


class Registration(database):
    __tablename__ = 'Registrtion for servisec'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    information_id = Column(Integer, ForeignKey('information_about_services.id'))
    service_id = Column(Integer, ForeignKey('services.id'))




