import unittest

from src.datacut import DataCut
from src.setting import Setting


class TestDataCut(unittest.TestCase):
    def setUp(self):
        self.setting = Setting("default.yml", "../test/test.yml")
        self.setting.configure()
        self.data = DataCut("../test/log/201712251354.csv")

    def tearDown(self):
        self.setting.dispose()
        self.data.dispose()

    def test_import_logfile(self):
        self.data.import_file(self.setting.setting["header_row"],
                              self.setting.setting["log_separate_type"])
        self.assertIsNotNone(self.data.df)

    def test_import_logfile_no_use_header(self):
        self.data.import_file(None, self.setting.setting["log_separate_type"])
        self.assertEqual(self.data.df.columns[2], 2)


if __name__ == '__main__':
    unittest.main()
