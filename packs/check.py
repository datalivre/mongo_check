

def get_check(client, dict_users, func_get_conversor, func_get_insert):

    db = client.admin
    listing = db.command('usersInfo')
    lista_users_db = [document['user'] for document in listing['users']]

    for user, ga in dict_users.items():
        if user in lista_users_db:
            try:
                try:
                    custom_data = [func_get_conversor(doc['customData']['ga'])
                                   for doc in listing['users'] if user in doc['user']]
                except KeyError:
                    custom_data = [func_get_conversor(doc['customData']['ars'])
                                   for doc in listing['users'] if user in doc['user']]
            except Exception:
                custom_data = 'empty'
            if custom_data is not 'empty' and ga in custom_data:
                print(f'Nada a ser feito para o usuário {user}')
            else:
                print(
                    f'Custom Data {custom_data} não encontrado ou incorreto em {user}')
                func_get_insert(db, user, ga)
        else:
            print(f'O usuário {user} não consta neste db')


if __name__ == "__main__":
    pass
