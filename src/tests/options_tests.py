import unittest

from ..pyjsongooglechart.options import Options

class OptionsTests(unittest.TestCase):
    def test_base(self):
        o = Options()
        self.assertEqual(o._value, None)

        ## Verify setattr
        # Change a special attribute
        o._value = 5
        self.assertEqual(o._value, 5)
        self.assertFalse("value" in o._attributes)

        # Create a new option
        o.height = 50
        self.assertTrue("height" in o._attributes)
        self.assertEqual(o.height._value, 50)
        self.assertEqual(repr(o.height), '50')
        self.assertTrue(isinstance(o._attributes['height'], Options))
        self.assertEqual(o._attributes['height']._value, 50)

        # Create a multi-level option
        o.hAxis.title = "test"
        self.assertEqual(o.hAxis._value, None)
        self.assertTrue("title" in o._attributes['hAxis']._attributes)
        self.assertEqual(o._attributes['hAxis']._value, None)
        self.assertEqual(o.hAxis.title._value, "test")

        # Change an existing option
        o.height = 55
        self.assertEqual(o.height._value, 55)

        ## Verify getattr
        getattr(o, "height")

    def test_build_struct(self):
        o = Options("test")
        o.height = 50
        o.width = 65
        o.legend.position = "bottom"
        o.legend.textStyle.color = 'gray'
        o.legend.textStyle.fontName = "Open Sans"
        setattr(o.legend.textStyle, "fontSize", 14)

        struct = o.build_struct()
        expected = \
          {'height': 50,
           'width': 65,
           'legend': {'position': 'bottom',
                      'textStyle': {'color': 'gray',
                                    'fontName': 'Open Sans',
                                    'fontSize': 14}},
           }
        self.assertEqual(struct, expected)


