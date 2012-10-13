import datetime
from decimal import Decimal
import unittest

from ..pyjsongooglechart import (BooleanColumn, StringColumn, NumberColumn,
                                 DateColumn, DatetimeColumn, TimeofdayColumn,
                                 ChartColumn)



class ColumnTests(unittest.TestCase):
    def test_base(self):
        c = ChartColumn("name", "id", "p")
        self.assertEqual(c.label, "name")
        self.assertEqual(c.id, "id")
        self.assertEqual(c.p, "p")

        values = [("1",), (2, "2")]
        c.insert_row(values[0][0])
        c.insert_row(*values[1])

        self.assertEqual(c.values[0], values[0])
        self.assertEqual(c.values[1], (values[1][0], values[1][1]))
        self.assertEqual(c.values, values)
        self.assertEqual(c.values, list(c))

    def test_validators(self):
        def worker(column, bad, good):
            self.assertRaises(ValueError, column.insert_row, bad)
            column.insert_row(good)

        c = BooleanColumn()
        worker(c, "non-boolean", True)

        c = StringColumn()
        worker(c, 12, "isastring")

        c = NumberColumn()
        worker(c, "12.5", 12.5)
        worker(c, Decimal("12.5"), 12)

        c = DateColumn()
        worker(c, "12-23-2012", datetime.date(2012, 12, 23))
        worker(c, datetime.timedelta(), datetime.datetime.now())

        c = DatetimeColumn()
        worker(c, "12-23-2012", datetime.datetime(2012, 12, 23))
        worker(c, datetime.date(2012, 12, 23), datetime.datetime.now())

        c = TimeofdayColumn()
        worker(c, "12-23-2012", datetime.datetime(2012, 12, 23))
        worker(c, datetime.date(2012, 12, 23), datetime.datetime.now())
