import unittest


from ..pyjsongooglechart import GoogleChart
from ..pyjsongooglechart import (StringColumn, NumberColumn)

class GoogleChartTests(unittest.TestCase):
    def test_base(self):
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

        # Verify the behavior of row insertion
        g.insert_row("hullo", (7, "7"))
        self.assertEqual(g[0].values[0], ("hullo",))
        self.assertEqual(g[1].values[0], (7, "7"))

        # Verify the data structures can be assembled correctly
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

    def test_options(self):
        g = GoogleChart("Title")
        self.assertEqual(g.options._attributes, {})

        g.options.height = 50
        g.options.width = 55
        g.options.legend.position = 'bottom'

        expected = {"height": 50,
                    "width": 55,
                    "title": "Title",
                    "legend": {"position": "bottom"}
                   }
        self.assertEqual(g.build_options_struct(), expected)

        g.options.title = "New Title"
        expected['title'] = "New Title"
        self.assertEqual(g.build_options_struct(), expected)

