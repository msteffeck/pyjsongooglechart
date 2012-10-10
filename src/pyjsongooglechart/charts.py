import itertools

from .column import (StringColumn, NumberColumn, BooleanColumn,
                     DateColumn, DatetimeColumn, TimeofdayColumn)

class GoogleChart(object):

    def __init__(self, title=""):
        super(GoogleChart, self).__init__()
        self.title = title
        self.columns = []

    def __getitem__(self, item):
        return self.columns[item]

    def _add_column(self, column, index=None):
        if index is not None:
            self.columns.insert(index, column)
        else:
            self.columns.append(column)

    def add_string_column(self, label="", index=None):
        self._add_column(StringColumn(label), index)

    def add_number_column(self, label="", index=None):
        self._add_column(NumberColumn(label), index)

    def add_boolean_column(self, label="", index=None):
        self._add_column(BooleanColumn(label), index)

    def add_date_column(self, label="", index=None):
        self._add_column(DateColumn(label), index)

    def add_datetime_column(self, label="", index=None):
        self._add_column(DatetimeColumn(label), index)

    def add_timeofday_column(self, label="", index=None):
        self._add_column(TimeofdayColumn(label), index)

    def insert_row(self, *args):
        for i, arg in enumerate(args):
            try:
                if isinstance(arg, (list, tuple)):
                    self.columns[i].insert_row(*arg)
                else:
                    self.columns[i].insert_row(arg)
            except IndexError:
                raise ValueError("There are more values than columns")

    def _build_json_structure(self):
        """Builds the json structure from the attached columns

        The following code may look a little complicated, so I think it's
        prudent that I explain what's happening:

        Step 1)
        Each column contains its associated values for the entire chart. The
        first thing we want to do is iterate over all of the columns and combine
        each row into a single tuple. That's what izip_longest does. The
        "longest" part is necessary in case one column has more values than the
        others.
        E.g. We have two columns with the following values:
        A = [("Row1",), ("Row2",), ("Row3",)]
        B = [(1, "1"), (2,)]
        What we will end up with is an iterator that spits out the following
        [ ( ("Row1",), (1, "1") ), ( ("Row2",), (2,) ), ( ("Row3",), ("",) ) ]

        Step 2)
        We then assign each column of each row to the corresponding vfp values,
        and wrap the whole row into a list
        E.g. Row1 will be as follows:
        [ {"v": "Row1"}, {"v": 1, "f": "1"} ]

        Step 3)
        Each row is then put into a dict and attached to the greater structure.
        The whole thing should look like the following:
        [
          {"c": [ {"v": "Row1"}, {"v": 1, "f": "1"} ] },
          {"c": [ {"v": "Row2"}, {"v": 2} ] },
          {"c": [ {"v": "Row3"}, {"v": ""} ] },
        ]

        """
        struct = []
        # Step 1 - See docstring for details
        for row in itertools.izip_longest(*self.columns, fillvalue=("",)):
            # Step 2
            row_list = [dict(itertools.izip(("v","f","p"), item))
                        for item in row]
            # Step 3
            struct.append({
                "c": row_list
            })
        return struct

    def render(self):
        struct = self._build_json_structure()


class ComboChart(GoogleChart):
    pass


