# coding=utf-8


def para(d):

    temp = list(d.keys())
    s = ''
    for key in temp:
        s += str(key) + '=' + str(d[key]) + '&'

    return s[:-1]


if __name__ == "__main__":
    para({})