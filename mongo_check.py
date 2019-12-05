from pymongo import MongoClient

from packs.check import get_check
from packs.conversor import get_conversor
from packs.insert import get_insert


class Connect(object):

    @staticmethod
    def get_connection():
        try:
            return MongoClient('mongodb://localhost:27017/')
        except:
            print("Could not connect to MongoDB")


if __name__ == "__main__":

    client = Connect.get_connection()
    dict_users = {"mongoadmin": 1713528, "shbd6001": 1579903,
                  "mongodb_exporter": 1713479, "smom6001": ""}

    get_check(client, dict_users, get_conversor, get_insert)
