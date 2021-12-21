import re

if __name__ == '__main__':
    s = 'account=admin,\npassword=123123'
    r = re.split(',\n', s)
    print(r)