import unittest
from plotlog.selectlog import SelectLog
from argparse import Namespace
import os.path


class TestSelectLog(unittest.TestCase):
    def setUp(self):
        self.sl = SelectLog()
        self.put_log_dir = "log/"
        self.graph_save_dir = "graph/"
        self.log_date_type = "0"
        self.args = Namespace(after=None, all=False, copy=False, input=None,
                              new=True, noshift=False, select=None,
                              setting='user.yml', slice=None)

    def test_arg_input(self):
        self.args = Namespace(after=None, all=False, copy=False,
                              input=["log/170101000000.csv", "log/170101120000.csv"],
                              new=True, noshift=False, select=None,
                              setting='user.yml', slice=None)
        paths = self.sl.get_logfile_paths(self.args, self.put_log_dir,
                                          self.graph_save_dir, self.log_date_type)
        self.assertEqual(paths[0], "log/170101000000.csv")
        self.assertEqual(paths[1], "log/170101120000.csv")
        self.assertTrue(os.path.exists(paths[0]))
        self.assertTrue(os.path.exists(paths[1]))

    def test_args_all(self):
        self.args = Namespace(after=None, all=True, copy=False, input=None,
                              new=True, noshift=False, select=None,
                              setting='user.yml', slice=None)
        paths = self.sl.get_logfile_paths(self.args, self.put_log_dir,
                                          self.graph_save_dir, self.log_date_type)
        self.assertEqual(paths[0], "log/170101000000.csv")
        self.assertEqual(paths[1], "log/170101120000.csv")
        self.assertEqual(paths[2], "log/170102000000.csv")
        self.assertTrue(os.path.exists(paths[0]))
        self.assertTrue(os.path.exists(paths[1]))
        self.assertTrue(os.path.exists(paths[2]))


if __name__ == '__main__':
    unittest.main()
