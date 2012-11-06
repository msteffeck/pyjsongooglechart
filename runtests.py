import unittest

from src.tests.chart_tests import GoogleChartTests
from src.tests.column_tests import ColumnTests
from src.tests.options_tests import OptionsTests


if __name__ == '__main__':
    charts = unittest.TestLoader().loadTestsFromTestCase(GoogleChartTests)
    columns = unittest.TestLoader().loadTestsFromTestCase(ColumnTests)
    options = unittest.TestLoader().loadTestsFromTestCase(OptionsTests)
    suite = unittest.TestSuite([charts, columns, options])
    unittest.TextTestRunner(verbosity=2).run(suite)


# Some pull test comment
