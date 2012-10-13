import datetime
import numbers


class ChartColumn(object):
    type = ''
    validation_error = "Values stored in a {0} column must be type {1}"

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

    def validate(self, value):
        """Validates the value as a bool type

        Note: we could just cast value into a bool, but the common theme of all
        validators is that we will not make assumptions about what the user
        really wants. Instead, we are strict and leave it to them to decide
        """
        if not isinstance(value, bool):
            raise ValueError(self.validation_error.format("boolean", "'bool'"))


class NumberColumn(ChartColumn):
    type = 'number'

    def validate(self, value):
        """Validates the value as a Number type

        Note: This doesn't accept Decimal types because Decimal types do not
        have a direct translation to a native numeric value. The user may want
        to cast the decimal to a float or an int, so we disallow Decimal, and
        allow the user to choose the best route for their data.
        The same is true for numbers inside a string. It is better if we force
        the user to cast the string to the appropriate type.
        """
        if not isinstance(value, numbers.Number):
            raise ValueError(self.validation_error.format("number", "'Number'"))


class StringColumn(ChartColumn):
    type = 'string'

    def validate(self, value):
        """Validates the value as a basestring type

        Note: Instead of validating the value of the string as a string type, we
        could have just cast all values to string. However, this may not be what
        the user wants; maybe they want a raw string, or a unicode string.
        Instead of making assumptions, we will just require the value already
        be a string.
        """
        if not isinstance(value, basestring):
            raise ValueError(self.validation_error.format("string",
                                                          "'basestring'"))


class DateColumn(ChartColumn):
    type = 'date'

    def validate(self, value):
        if not isinstance(value, datetime.date) \
                and not isinstance(value, datetime.datetime):
            raise ValueError(self.validation_error.format(
                                               "date",  "'date' or 'datetime'"))


class DatetimeColumn(ChartColumn):
    type = 'datetime'

    def validate(self, value):
        if not isinstance(value, datetime.datetime):
            raise ValueError(self.validation_error.format("datetime",
                                                          "'datetime'"))


class TimeofdayColumn(DatetimeColumn):
    type = 'timeofday'
