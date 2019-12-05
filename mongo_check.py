from pymongo import MongoClient

from packs.conversor import get_conversor
from packs.insert import get_insert


class Connect(object):

    @staticmethod
    def get_connection():
        try:
            return MongoClient('mongodb://localhost:27017/')
        except:
            print("Could not connect to MongoDB")


def get_check(dict_users):
    client = Connect.get_connection()
    db = client.admin
    listing = db.command('usersInfo')
    lista_users = [document['user'] for document in listing['users']]

    try:
        try:
            custom_data = [get_conversor(document['customData']['ga'])
                           for document in listing['users']]
        except KeyError:
            custom_data = [get_conversor(document['customData']['ars'])
                           for document in listing['users']]
    except Exception:
        custom_data = 'empty'

    print(custom_data)
    for user, ga in dict_users.items():
        if user in lista_users:
            if custom_data is not 'empty' and ga in custom_data:
                print(f'Nada a ser feito para o usuário {user}')
            else:
                print(f'Custom Data não encontrada no documento do {user}')
                get_insert(db, user, ga)
        else:
            print(f'O usuário {user} não consta neste db')


if __name__ == "__main__":
    dict_users = {"mongoadmin": 1713528, "shbd6001": 1579903,
                  "mongodb_exporter": 1713479, "smom6001": ""}
    get_check(dict_users)
