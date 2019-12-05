import errno
from os import path
from sys import exit


def get_args(filename):
    try:
        if path.isfile(filename):
            dict_properties = {}
            with open(filename, 'r', encoding='utf8') as f:
                for line in f:
                    tmp_prop = [l.strip() for l in line.split(';')]
                    dict_properties[tmp_prop.pop(0)] = ''.join(tmp_prop[1])
            return dict_properties
        else:
            print(f'Arquivo {filename} não encontrado.')

    except IOError as e:
        print(f'{filename}\n{e}')
        exit(errno.EPERM)


if __name__ == "__main__":
    filename = "confiles/mongocheck.properties"
    print(get_args(filename))
