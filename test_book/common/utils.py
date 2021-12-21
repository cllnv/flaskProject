import time,csv,os
import re
import requests

base_path = os.path.dirname(os.path.dirname(__file__))  # 项目基本路径
case_path = os.path.join(base_path, 'case')  # 测试脚本所在目录
data_path = os.path.join(base_path, 'data')  # 测试用例所在目录
report_path = os.path.join(base_path, 'report')  # 测试报告所在目录


def request(url, method, data=None, header=None):
    rq = requests.session()  # 创建session对象
    if method.upper() == 'GET':
        rr = rq.get(url, params=data, headers=header)
    elif method.upper() == 'POST':
        rr = rq.post(url, json=data, headers=header)
    return rr


def get_time():
    t = time.strftime('%Y-%m-%d %X')
    return t


def read_csv(file):
    if os.path.exists(file):
        with open(file=file,mode='r') as f:
            d = csv.reader(f)
            return list(d)
    else:
        print(f'文件{file}不存在')
        return False


def get_test_data(s):
    """
    将'accoun=admin,\npassword=123123'格式字符串转换为字典{’account‘:'admin','pasword':'123456'}'
    :param s:
    :return:
    """
    data = {}
    # print(s)
    rr = re.split(',\n', s)
    # for i,j in enumerate(r):
    #     tmp = j.split('=')
    #     data[tmp[0]] = tmp[1]
    for i in rr:
        tmp = i.split('=')
        data[tmp[0]] = tmp[1]
    return data


if __name__ == '__main__':
    s = 'account=,\npassword=123123'
    rrr = get_test_data(s)
    print(get_time())

'''
    s = '{"account":"1","password":"123123"}'
    print(type(s))
    s = eval(s) # 将字符串格式转换成字典格式 前提是 字符串本身就是字典格式
    print(type(s))
'''
