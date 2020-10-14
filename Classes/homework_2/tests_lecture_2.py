import dataclasses
import types
import unittest
import homework_lecture_2


class TestCases(unittest.TestCase):

    def test_maths(self):
        self.assertEqual(homework_lecture_2.Maths.add_num(5, 8), 5 + 8)
        self.assertTrue(isinstance(homework_lecture_2.Maths.add_num, types.FunctionType))

    def test_pizza(self):
        margherite = homework_lecture_2.Pizza.margherita()
        self.assertEqual(margherite.ingredients, ['mozzarella', 'tomatoes'])
        prosciutto = homework_lecture_2.Pizza.prosciutto()
        self.assertEqual(prosciutto.ingredients, ['mozzarella', 'tomatoes', 'ham'])

    def test_concert(self):
        homework_lecture_2.Concert.max_visitors_num = 100
        c1 = homework_lecture_2.Concert()
        c1.visitors_count = homework_lecture_2.Concert.max_visitors_num - 10
        self.assertEqual(c1.visitors_count, homework_lecture_2.Concert.max_visitors_num - 10)
        c1.visitors_count = homework_lecture_2.Concert.max_visitors_num + 10
        self.assertEqual(c1.visitors_count, homework_lecture_2.Concert.max_visitors_num)

    def test_book(self):
        book_dict = {"title": "Title", "author": "Author", "pages_num": 100}
        book_datacls_obj = homework_lecture_2.BookDataclass(**book_dict)
        assert book_datacls_obj.title == book_dict["title"]
        assert not dataclasses.is_dataclass(homework_lecture_2.Book)
        book = homework_lecture_2.Book("Title", "Author", 100)
        assert str(book) == str(book_datacls_obj)


if __name__ == "__main__":
    unittest.main()
