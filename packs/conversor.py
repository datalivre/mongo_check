

def get_conversor(lista):
    try:
        return int(lista)
    except Exception:
        return lista


if __name__ == "__main__":
    print(get_conversor([1, 2, 3, 'a', 5]))
