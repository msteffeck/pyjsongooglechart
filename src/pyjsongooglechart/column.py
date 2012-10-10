
class ChartColumn(object):
    def __init__(self, label=""):
        super(ChartColumn, self).__init__()
        self.label = label
        self.values = []
        self.axis = 0

    def __iter__(self):
        return iter(self.values)

    def insert_row(self, *args):
        self.validate(args[0])
        self.values.append(args)

    def validate(self, value):
        """Validates the given value.

        This should be overridden in a child class, and it should raise
        appropriate exceptions for validation errors
        """
        pass


class BooleanColumn(ChartColumn): pass


class NumberColumn(ChartColumn): pass


class StringColumn(ChartColumn): pass


class DateColumn(ChartColumn): pass


class DatetimeColumn(ChartColumn): pass


class TimeofdayColumn(ChartColumn): pass
