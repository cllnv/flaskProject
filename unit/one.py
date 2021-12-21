import unittest
from parameterized import parameterized

'''
让测试驱动程序直接继承自父类TestCase
运行unittest框架的测试代码时，尽量不要直接在测试方法的地方运行，否则只会运行当前测试用例
建议使用unittest.main( )来正常地启动unittest的运行器执行该类的所有测试用例
所有的测试用例，要能够正常被运行器调用的话，必须以test关键字开头
所有的测试用例，是按照ASCII排序进行调用，而不是代码开发顺序，也不是数字比大小(从不同的字符串)
'''
class UnitTest01(unittest.TestCase):
    # def setUp(self):
    #     print("每个测试用例执行前 执行")
    #
    # def tearDown(self):
    #     print("每个测试用例执行后 执行")
    #
    # @classmethod
    # def setUpClass(cls):
    #     print("每次执行一个测试类时 调用一次")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("每次执行一个测试类后  调用一次")
    #
    # @unittest.skip  # 跳过测试用例
    def test_01(self):
        self.assertTrue(True)

    @unittest.expectedFailure  # 标记该测试用例为预期失败 如果失败 则该测试方法不算失败
    def test_11(self):
        self.fail()  # 强制失败

    @parameterized.expand([(1,1,3),(1,2,3)])
    def test_12(self, a,b,c):
        self.assertEqual(a,b,c)


if __name__ == '__main__':
    unittest.main()
