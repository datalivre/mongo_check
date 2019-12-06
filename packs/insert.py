

def get_insert(db, user, ga):
    collection = db.system.users
    cursor = collection.find_one_and_update(
        {"user": user},
        {"$set": {"customData.ga": ga}},
        projection={'user': True, 'customData':True, '_id': False},
        upsert=True)
    print(cursor)


if __name__ == "__main__":
    pass
