import unittest

from src.tests.chart_tests import GoogleChartTests
from src.tests.column_tests import ColumnTests


if __name__ == '__main__':
    charts = unittest.TestLoader().loadTestsFromTestCase(GoogleChartTests)
    columns = unittest.TestLoader().loadTestsFromTestCase(ColumnTests)
    suite = unittest.TestSuite([charts, columns])
    unittest.TextTestRunner(verbosity=2).run(suite)
