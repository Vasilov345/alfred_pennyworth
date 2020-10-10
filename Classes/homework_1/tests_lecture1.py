import unittest
import homework_lecture1


class MagicMethodsTestCases(unittest.TestCase):

    def test_custom_int(self):
        custom_int = homework_lecture1.CustomInt(5)
        self.assertEqual(custom_int, 5)
        self.assertFalse(custom_int < 10)

    def test_limited_attrs(self):
        person = homework_lecture1.PersonWithLimitedSkills()
        exc = None
        try:
            person.name
        except AttributeError as e:
            exc = e
        assert type(exc) == AttributeError
        person.sleep = "zzz"
        self.assertEqual(person.sleep, "zzz")

    def test_hidden_attrs(self):
        hidden_attrs_obj = homework_lecture1.HiddenAttrs()
        self.assertEqual(dir(hidden_attrs_obj), [])
        self.assertEqual(hidden_attrs_obj.__dict__(), {})
        hidden_attrs_obj.new_attr = 5
        self.assertEqual(hidden_attrs_obj.__dict__(), {})

    def test_callable_obj(self):
        callable_obj = homework_lecture1.CallableInstances(lambda x: x + 8)
        self.assertEqual(callable_obj(10), 18)


if __name__ == "__main__":
    unittest.main()
