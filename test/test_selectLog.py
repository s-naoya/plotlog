import unittest
from plotlog.selectlog import SelectLog


class TestSelectLog(unittest.TestCase):
    def setUp(self):
        self.obj = SelectLog()

    def test_test(self):
        self.assertEqual(0, 0)


if __name__ == '__main__':
    unittest.main()
