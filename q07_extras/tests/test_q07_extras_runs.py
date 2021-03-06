import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q07_extras.build import extras_runs
class TestExtras_runs(TestCase):
    def test_extras_runs(self):
        data = read_data()
        extras = extras_runs(data)
        self.assertIsInstance(extras, int)
        self.assertTrue(6 == extras)
