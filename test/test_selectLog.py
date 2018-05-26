import unittest

from plotlog.selectlog import SelectLog
import create_exlog as ce


class TestSelectLog(unittest.TestCase):
    def setUp(self):
        self.sl = SelectLog()

    def tearDown(self):
        pass

    def test_get_paths_of_all(self):
        ce.create_exlog(log_date_type=0)
        all_paths = [f[1]+f[0][2:]+".csv" for f in ce.default_files]
        get_all_paths = self.sl.get_paths_of_all("log/")

        for all_path in all_paths:
            self.assertIn(all_path, get_all_paths)
        for get_all_path in get_all_paths:
            self.assertIn(get_all_path, all_paths)

