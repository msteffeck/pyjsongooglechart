
class Options(object):
    _special_attrs = ('_value', '_attributes')

    def __init__(self, value=None):
        super(Options, self).__init__()
        self._value = value
        self._attributes = {}

    def __getattr__(self, item):
        if item in self._attributes:
            return self._attributes[item]
        else:
            option = Options()
            self._attributes[item] = option
            return option

    def __setattr__(self, key, value):
        if key in Options._special_attrs:
            self.__dict__[key] = value
        elif key in self._attributes:
            self._attributes[key]._value = value
        else:
            self._attributes[key] = Options(value)

    def __repr__(self):
        return repr(self._value)

    def build_struct(self):
        # It's possible this Options was created without any values, exclude it
        if not self._attributes and self._value is None:
            return None
        elif self._attributes:
            struct = {}
            for attr, val in self._attributes.iteritems():
                value = val.build_struct()
                # If one of the child Options returns None, we want to skip it
                if value is not None:
                    struct[attr] = value
                else:
                    continue
        else:
            struct = self._value
        return struct
