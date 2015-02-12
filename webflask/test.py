import unittest
from request_parsers import SafeForm


class TestSafeForm(unittest.TestCase):

    def test_no_error_on_getting_inexistent_int_value(self):
        form = SafeForm({})
        result = form.int('inexistent')
        self.assertEqual(result, None)

    def test_getting_int_parsable_string(self):
        form = SafeForm({'int': '10'})
        result = form.int('int')
        self.assertIsInstance(result, int)

    def test_no_error_on_getting_inexistent_str_value(self):
        form = SafeForm({})
        result = form.str('inexistent')
        self.assertEqual(result, None)

    def test_no_convertion_on_string(self):
        form = SafeForm({'str': 'Joe'})
        result = form.str('str')
        self.assertEqual('Joe', result)