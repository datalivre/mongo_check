from pymongo import MongoClient

from packs.check import get_check
from packs.conversor import get_conversor
from packs.insert import get_insert
from packs.args import get_args


class Connect(object):

    @staticmethod
    def get_connection():
        try:
            return MongoClient('mongodb://localhost:27017/')
        except:
            print("Could not connect to MongoDB")


if __name__ == "__main__":

    client = Connect.get_connection()
    dict_users = get_args(get_conversor, 'confiles/mongocheck.properties')
    get_check(client, dict_users, get_conversor, get_insert)
