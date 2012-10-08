
class ChartColumn(object):
    def __init__(self, label=""):
        super(ChartColumn, self).__init__()
        self.label = label
        self.values = []
        self.axis = 0


class BooleanColumn(ChartColumn): pass

class NumberColumn(ChartColumn): pass

class StringColumn(ChartColumn): pass

class DateColumn(ChartColumn): pass

class DatetimeColumn(ChartColumn): pass

class TimeofdayColumn(ChartColumn): pass
