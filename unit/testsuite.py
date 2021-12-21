import unittest
from unit.one import UnitTest01
# from HTMLTestRunner import *
import HTMLTestRunner
# suite = unittest.TestSuite()
# # 这个是按照 添加测试用例的顺序执行的 不是按照ascii码的顺序
# # suite.addTest(UnitTest01('test_01'))
# # suite.addTest(UnitTest01('test_11'))
# #  直接指定测试类这一级 进行测试
# suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest01))
# # suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest02))
# r = unittest.TestResult()
# suite.run(result=r)
# print(r.__dict__)
# print(r.__dict__['testsRun'])
# print(r.testsRun)
# print(r.__dict__['failures'][0][0])


#使用 HTMLTESTRUNNER运行 生成测试报告
suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(UnitTest01))

runner = HTMLTestRunner(stream=open('./report.html','wb'), title="测试报告", description="测试报告你大爷")
runner.run(suite)

