import unittest
from setting import Setting


class TestSetting(unittest.TestCase):
    def test_read_default_file(self):
        setting = Setting("setting.yml")
        setting.configure()
        self.assertIsNotNone(setting.default)

    def test_read_setting_file(self):
        setting = Setting("setting.yml")
        setting.configure()
        self.assertIsNotNone(setting.setting)


if __name__ == '__main__':
    unittest.main()
