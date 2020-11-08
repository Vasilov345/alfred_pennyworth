import unittest
import homework
<<<<<<< HEAD
=======
from LoggingAndExceptions.homework import homework
>>>>>>> bcdbe039ca591bcd6801c62ac89c9a83db0710f2


class TestCases(unittest.TestCase):

    def test_exceptions(self):
        err = homework.TooManyVisitors()
        assert isinstance(err, homework.Error)
        concert_made = homework.make_concert(1000)
        self.assertFalse(concert_made)
        self.assertRaises(homework.TooManyVisitors, homework.Concert, 1000)

    def test_logging(self):
        homework.log_message("this is info", 20)
        homework.log_message("this is warning", 30)
        with open("test.log", "r") as f:
            logs = f.readlines()
            self.assertEqual(logs, ['this is info\n', 'this is warning\n'])


if __name__ == "__main__":
<<<<<<< HEAD
    unittest.main()
=======
    unittest.main()
>>>>>>> bcdbe039ca591bcd6801c62ac89c9a83db0710f2
