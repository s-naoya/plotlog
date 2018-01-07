import unittest

from src.datacut import DataCut


class TestDataCut(unittest.TestCase):
    def setUp(self):
        self.data = DataCut(["../test/log/201712251354.csv"])

    def tearDown(self):
        self.data.dispose()

    def test_import_logfile(self):
        self.data.import_file(0, ",")
        self.assertIsNotNone(self.data.df)

    def test_import_logfile_no_use_header(self):
        self.data.import_file(None, ",")
        self.assertEqual(self.data.df.columns[2], 2)

    def test_df_x_axis(self):
        self.data.import_file(0, ",")
        self.data.set_x_axis("time")
        self.assertEqual(self.data.x_axis[0], 0.005)

    def test_df_shift(self):
        self.data.import_file(0, ",")
        self.data.set_x_axis("time")
        self.data.shift("refCoM_y", 1e-5)
        self.assertEqual(self.data.x_axis[0], 0.0)
        self.assertTrue(self.data.df["refCoM_y"][0] < 0.01)
        self.assertTrue(self.data.df["refCoM_y"][50] > 0.001)

    def test_df_slice(self):
        self.data.import_file(0, ",")
        self.data.set_x_axis("time")
        self.data.slice(5.0, 10.0)
        self.assertEqual(self.data.x_axis[0], 5.0)
        self.assertEqual(self.data.x_axis.tail(1).values[0], 10.0)
        self.assertEqual(len(self.data.x_axis), len(self.data.df))


if __name__ == '__main__':
    unittest.main()
