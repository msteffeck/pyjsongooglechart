from .column import ChartColumn

class GoogleChart(object):

    def __init__(self, title=""):
        super(GoogleChart, self).__init__()
        self.title = title
        self.columns = []

    def add_string_column(self, label=""): pass

    def add_number_column(self, label=""): pass

    def add_boolean_column(self, label=""): pass

    def add_date_column(self, label=""): pass

    def add_datetime_column(self, label=""): pass

    def add_timeofday_column(self, label=""): pass


class ComboChart(GoogleChart):
    pass


