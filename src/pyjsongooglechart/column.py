
class ChartColumn(object):
    type = ''

    def __init__(self, label="", id="", p=""):
        super(ChartColumn, self).__init__()
        self.label = label
        self.id = id
        self.p = p
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


class BooleanColumn(ChartColumn):
    type = 'boolean'


class NumberColumn(ChartColumn):
    type = 'number'


class StringColumn(ChartColumn):
    type = 'string'


class DateColumn(ChartColumn):
    type = 'date'


class DatetimeColumn(ChartColumn):
    type = 'datetime'


class TimeofdayColumn(ChartColumn):
    type = 'timeofday'
