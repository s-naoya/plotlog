import unittest

from plotlog.selectlog import SelectLog
import create_exlog as ce


class TestSelectLog(unittest.TestCase):
    def setUp(self):
        self.sl = SelectLog()
        ce.create_exlog(log_date_type=0)

    def tearDown(self):
        pass

    def test_get_paths_of_all(self):
        all_paths = [f[1]+f[0][2:]+".csv" for f in ce.default_files]
        get_all_paths = self.sl.get_paths_of_all("log/")

        for all_path in all_paths:
            self.assertIn(all_path, get_all_paths)
        for get_all_path in get_all_paths:
            self.assertIn(get_all_path, all_paths)

    def test_get_paths_of_after(self):
        after_date = "170102200000"
        get_after_paths = self.sl.get_paths_of_after(after_date,
                                                     "log/",
                                                     0)
        after_paths = [f[1]+f[0][2:]+".csv" for f in ce.default_files if int(f[0][2:]) >= int(after_date)]
        for after_path in after_paths:
            self.assertIn(after_path, get_after_paths)
        for get_after_path in get_after_paths:
            self.assertIn(get_after_path, after_paths)

    def test_get_paths_of_select(self):
        sel_dates = ["170102200000", "170102000000"]
        get_sel_paths = self.sl.get_paths_of_select(sel_dates, "log/")
        sel_paths = []
        for sel_date in sel_dates:
            for f in ce.default_files:
                if int(f[0][2:]) == int(sel_date):
                    sel_paths.append(f[1] + f[0][2:] + ".csv")

        for sel_path in sel_paths:
            self.assertIn(sel_path, get_sel_paths)
        for get_sel_path in get_sel_paths:
            self.assertIn(get_sel_path, sel_paths)

    def test_get_paths_of_new(self):
        if ce.isdir("./graph"):
            ce.rmtree("./graph")
        sel_dates = ["170102200000", "170101120000", "170102180000"]
        get_sel_paths = self.sl.get_paths_of_select(sel_dates, "log/")
        for path in get_sel_paths:
            self.sl.setup_save_dir(self.sl.get_fn(path), 0, "graph/")

        get_new_paths = self.sl.get_paths_of_new("log/", "graph/", 0)
        new_paths = [f[1]+f[0][2:]+".csv" for f in ce.default_files]
        for get_sel_path in get_sel_paths:
            new_paths.remove(get_sel_path)

        for new_path in new_paths:
            self.assertIn(new_path, get_new_paths)
        for get_new_path in get_new_paths:
            self.assertIn(get_new_path, new_paths)
