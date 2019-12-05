

def get_check(client, dict_users, func_get_conversor, func_get_insert):

    db = client.admin
    listing = db.command('usersInfo')
    lista_users = [document['user'] for document in listing['users']]

    try:
        try:
            custom_data = [func_get_conversor(document['customData']['ga'])
                           for document in listing['users']]
        except KeyError:
            custom_data = [func_get_conversor(document['customData']['ars'])
                           for document in listing['users']]
    except Exception:
        custom_data = 'empty'

    for user, ga in dict_users.items():
        if user in lista_users:
            if custom_data is not 'empty' and ga in custom_data:
                print(f'Nada a ser feito para o usuário {user}')
            else:
                print(f'Custom Data não encontrada no documento do {user}')
                func_get_insert(db, user, ga)
        else:
            print(f'O usuário {user} não consta neste db')


if __name__ == "__main__":
    pass
