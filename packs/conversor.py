# _*_ coding:utf-8 _*_
# @author Robert Carlos                 #
# email robert.carlos@linuxmail.org     #
# 2019-Dec (CC BY 3.0 BR)               #

def get_conversor(lista):
    try:
        return int(lista)
    except ValueError:
        return lista


if __name__ == "__main__":
    print(get_conversor('123456'))
