import unittest
from src.setting import Setting


class TestSetting(unittest.TestCase):
    def test_read_default_file(self):
        obj = Setting("test/test.yml")
        obj.configure()
        self.assertIsNotNone(obj.default)

    def test_read_user_file(self):
        obj = Setting("test/test.yml")
        obj.configure()
        self.assertIsNotNone(obj.user)

    def test_config_setting_dic(self):
        obj = Setting("test/test.yml")
        obj.configure()
        self.assertNotEqual(obj.setting["log_extension"],
                            obj.default["log_extension"])
        self.assertNotEqual(obj.setting["footprint"]["foot_size"],
                            obj.default["footprint"]["foot_size"])
        self.assertEqual(obj.setting["footprint"]["supleg_label"],
                         obj.default["footprint"]["supleg_label"])


if __name__ == '__main__':
    unittest.main()
