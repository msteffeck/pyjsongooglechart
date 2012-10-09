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



class ComboChart(GoogleChart):
    pass


