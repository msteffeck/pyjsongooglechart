import unittest


from ..pyjsongooglechart import GoogleChart
from ..pyjsongooglechart import (StringColumn, NumberColumn)

class GoogleChartTests(unittest.TestCase):
    def test_basic(self):
        # Verify we can create a new chart
        g = GoogleChart("Test")
        self.assertEqual(g.title, "Test")
        self.assertEqual(g.columns, [])

        # Verify we can add a column to it
        g.add_string_column("Column0")
        self.assertTrue(isinstance(g[0], StringColumn))
        self.assertEqual(g[0].label, "Column0")

        # Verify the behavior of column indexing
        g.add_column(NumberColumn("Column2"), index=2)
        self.assertRaises(IndexError, g.__getitem__, 2)
        self.assertTrue(isinstance(g[1], NumberColumn))

        g.insert_row("hullo", (7, "7"))
        self.assertEqual(g[0].values[0], ("hullo",))
        self.assertEqual(g[1].values[0], (7, "7"))

        rows = g._build_rows_struct()
        self.assertEqual(rows,
                         [{'c': [{'v': 'hullo'}, {'f': '7', 'v': 7}]}])

        cols = g._build_columns_struct()
        self.assertEqual(cols,
                        [{  'pattern': '',
                            'type': 'string',
                            'id': '',
                            'p': '',
                            'label': 'Column0'},
                         {  'pattern': '',
                            'type': 'number',
                            'id': '',
                            'p': '',
                            'label': 'Column2'}])

