import unittest
from setting import Setting


class TestSetting(unittest.TestCase):
    def test_read_default_file(self):
        setting = Setting()
        setting.configure()
        self.assertIsNotNone(setting.default)


if __name__ == '__main__':
    unittest.main()
