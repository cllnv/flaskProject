import pytest
from test_book.common.utils import *

data = read_csv(data_path + '/test.csv')  # 读取csv文件中的测试用例


# @pytest.mark.skip()  #  直接跳过测试用例 可以加在整个类上
# @pytest.mark.skip(reason='该用例存在bug，请跳过！') 可以加在整个类上

# @pytest.mark.xfail 标记预期测试用例为fail 用例成功则显示Xpassed，失败则显示xfailed。xfail标记并不会影响用例的运行 看清了 多个X啊

# data1 = [1, 2]
# data2 = ["python", "java"]
# data3 = ["软", "件", "测", "试", "君"]
#
#
# @pytest.mark.parametrize("a", data1)
# @pytest.mark.parametrize("b", data2)
# @pytest.mark.parametrize("c", data3)

# @pytest.mark.parametrize("user,pwd",
#                          [("xiaoqiang", "123456"), ("rose", "123456"),
#                           pytest.param("jone", "123456", marks=pytest.mark.xfail),
#                           pytest.param("Alex", "123456", marks=pytest.mark.skip)])

@pytest.mark.skipif(data[5][1] != 'N', reason='此版本不持支测试')  # 必须带上reason  可以加在整个类上
@pytest.mark.parametrize('case', data[7:])  # 参数化
def test_login(case):
    url = data[1][1]
    print("url:"+url)
    method = data[2][1]
    print("method:"+method)
    print("case[1]:" + case[1])
    d = get_test_data(case[1])
    print(d)
    r = request(url=url, method=method, data=d)
    print(type(r))
    assert int(case[2]) == r.json()['code']
    assert case[3] == r.json()['message']


# @pytest.mark.xfail
def test_login1():
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(['-v', __file__])
    # pytest.main(['-rs', 'test01.py'])


