import pytest
import requests
from gaoji.function import Function


func = Function()


def test_driver():
    with open('./data.csv') as file:
        list1 = file.readlines()

    for item in list1:
        print("item:"+item)
        number = item.strip().split(",")[0]
        print(number)
        expect = item.strip().split(",")[1]
        print(expect)
        result = func.check_number(number)
        if result == expect:
            print('success')  # 有返回值根据返回值判断 抛出异常 可以捕获异常 如果没有返回值呢
        else:
            print('fail,数字为:%s' % number)


if __name__ == '__main__':
    pytest.main(['-vs'])
    # try:
    #     x=5
    # except Exception as e:
    #     print(e)

    # with Function() as f:
    #     f.check_number(2)
    # 需要配合__enter__