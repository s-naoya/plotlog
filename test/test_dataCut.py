import unittest

from src.setting import Setting


class TestDataCut(unittest.TestCase):
    def setUp(self):
        self.setting = Setting("test/test.yml")
        self.setting.configure()

    def tearDown(self):
        self.setting.dispose()


if __name__ == '__main__':
    unittest.main()
