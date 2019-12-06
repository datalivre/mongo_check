import errno
from os import path
from sys import exit


def get_args(func_get_conversor, filename):
    try:
        if path.isfile(filename):
            dict_properties = {}
            with open(filename, 'r', encoding='utf8') as f:
                for line in f:
                    if '#' not in line:
                        tmp_prop = [func_get_conversor(
                            l.strip()) for l in line.split(';')]
                        dict_properties[tmp_prop.pop(0)] = tmp_prop[1]
            return dict_properties
        else:
            print(f'Arquivo {filename} não encontrado.')
            exit(errno.EPERM)
    except IOError as e:
        print(f'{filename}\n{e}')
        exit(errno.EPERM)


if __name__ == "__main__":
    pass
