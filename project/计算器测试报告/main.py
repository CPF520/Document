
'''
    入口程序：
        用于扫描加法，减法用例
        并执行得到测试报告
    1.HTMLTestRunner

'''
import HTMLTestRunner
import unittest

# 加载8条用例
tests = unittest.defaultTestLoader.discover(r"G:\python\day12【单元测试】\day12",pattern="Test*.py")

# 创建运行器，来运行8条用例
runner = HTMLTestRunner.HTMLTestRunner(
    title = "计算器的测试报告",  #标题
    description="加法和减法的测试报告",  #详细标题，描述
    verbosity=1,   #详细程度
    stream = open(file="计算器.html",mode="wb+")
)


# 生成测试报告
runner.run(tests)

# 任务1：
    # 4.使用邮件发送测试报告
# 使用代码去发送邮件。
# 温馨提示：用户名，密码：授权码（开启smtp授权码）








