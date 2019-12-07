# _*_ coding:utf-8 _*_
# @author Robert Carlos                 #
# email robert.carlos@linuxmail.org     #
# 2019-Dec (CC BY 3.0 BR)               #


def get_insert(db, user, ga):
    collection = db.system.users
    cursor = collection.find_one_and_update(
        {"user": user},
        {"$set": {"customData.ga": ga}},
        projection={'user': True, 'customData': True, '_id': False},
        upsert=True)
    print(cursor)


if __name__ == "__main__":
    pass
