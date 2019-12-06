

def get_conversor(lista):
    try:
        return int(lista)
    except ValueError:
        return lista


if __name__ == "__main__":
    print(get_conversor('123456'))
