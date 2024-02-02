from connection_to_db import connection_db, close_connection_db
from Models.models import User, Administrator, Type_services


def create_new_user():
    new_user = User(name='Petr', surname='Ivanov', patronymic='Aleksandrovich',
                    age=8, login='pEtR', password='12345')
    new_session = connection_db()
    new_session.add(new_user)
    close_connection_db(new_session)


def create_new_admin():
    new_admin = Administrator(name='Admin3', surname='Adminov3', patronymic='Aleksandrovich',
                              age=18, login='Admin3', password='12345')
    new_session = connection_db()
    new_session.add(new_admin)
    close_connection_db(new_session)


def type_of_service():
    new_session = connection_db()
    new_type_service = Type_services(type_name='photo', administrator_id=new_session.query(Administrator.id).filter(
        Administrator.login == 'Admin'))
    new_session.add(new_type_service)
    close_connection_db(new_session)

def main():
    type_of_service()


if __name__ == '__main__':
    main()
