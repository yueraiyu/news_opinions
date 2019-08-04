import unittest


class DemoTest(unittest.TestCase):
    # 初始测试资源
    def setUp(self):
        print("demo test start")

    # 释放测试资源
    def tearDown(self):
        print("demo test end")

    def test_demo(self):
        print("test demo")
