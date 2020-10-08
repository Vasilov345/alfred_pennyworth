import unittest
import homework


class DictComprehensionTestCases(unittest.TestCase):

    def test_task_1_valid_values(self):
        given_data = [
            {'age': 43, 'name': 'denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36, 'name': 'Godzilla'},
            {'age': 47, 'name': 'spike'},
            {'age': 31, 'name': 'SuperMan'},
            {'age': 49, 'name': 'Batman'},
            {'age': 37, 'name': 'claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'homer'}
        ]
        actual_result = homework.task_1_fix_names_start_letter(given_data)
        for student in actual_result:
            self.assertTrue(student['name'][0].isupper())

    def test_task_1_empty_fields(self):
        given_data = [
            {'age': 43, 'name': 'denis'},
            {'age': 49, 'name': 'Roman'},
            {'age': 36},
            {'age': 47, 'name': 'spike'},
            {'age': 31, 'name': 'SuperMan'},
            {'age': 49},
            {'age': 37, 'name': 'claus'},
            {'age': 55, 'name': 'Frank'},
            {'age': 83, 'name': 'homer'}
        ]
        actual_result = homework.task_1_fix_names_start_letter(given_data)
        for student in actual_result:
            if student.get('name') is not None:
                self.assertTrue(student['name'][0].isupper())

    def test_task_2_valid_values(self):
        given_data = [{'age': 43, 'name': 'denis', 'sex': 'male'},
                      {'age': 49, 'name': 'Roman', 'sex': 'male'},
                      {'age': 36, 'name': 'Godzilla', 'sex': 'male'},
                      {'age': 47, 'name': 'spike', 'sex': 'female'},
                      {'age': 31, 'name': 'SuperMan', 'sex': 'female'},
                      {'age': 49, 'name': 'Batman', 'sex': 'male'},
                      {'age': 37, 'name': 'claus', 'sex': 'male'},
                      {'age': 55, 'name': 'Frank', 'sex': 'female'},
                      {'age': 83, 'name': 'homer', 'sex': 'male'}
                      ]
        redundant_keys = ['sex', 'name']
        actual_result = homework.task_2_remove_dict_fields(given_data, redundant_keys)
        for member in actual_result:
            for redundant_key in redundant_keys:
                self.assertIsNone(member.get(redundant_key))


class FilterTestCases(unittest.TestCase):

    def test_task_3_one_result(self):
        given_data = [{'age': 43, 'name': 'denis', 'sex': 'male'},
                      {'age': 49, 'name': 'Roman', 'sex': 'male'},
                      {'age': 36, 'name': 'Godzilla', 'sex': 'male'},
                      {'age': 47, 'name': 'spike', 'sex': 'female'},
                      {'age': 31, 'name': 'SuperMan', 'sex': 'female'},
                      {'age': 49, 'name': 'Batman', 'sex': 'male'},
                      {'age': 37, 'name': 'claus', 'sex': 'male'},
                      {'age': 55, 'name': 'Frank', 'sex': 'female'},
                      {'age': 83, 'name': 'homer', 'sex': 'male'}
                      ]
        value_to_search = 'SuperMan'
        expected_result = [{'age': 31, 'name': 'SuperMan', 'sex': 'female'}]
        actual_result = homework.task_3_find_item_via_value(data=given_data, value=value_to_search)
        self.assertListEqual(expected_result, actual_result)


class LambdaFunctionTestCases(unittest.TestCase):

    def test_task_4_check_sum(self):
        lambda_func = homework.task_4_return_lambda_sum_2_ints()
        self.assertEqual(lambda_func(5, 6), 11)


class MutableImmutableTestCases(unittest.TestCase):

    def test_task_5_list_not_mutated_by_func(self):
        l = ["a", "b"]
        self.assertEqual(homework.task_5_append_str_to_list_and_return(l, "c"), ["a", "b", "c"])
        self.assertEqual(l, ["a", "b"])


class StringFormattersTestCases(unittest.TestCase):

    def test_task_6_insert_callable_result_into_string(self):
        self.assertEqual(homework.task_6_insert_function_result_into_string(lambda: "play"), "start play finish")

    def test_task_7_string_shorter(self):
        self.assertEqual(
            homework.task_7_insert_2_vars_into_string(5.67, "dolls"), "I have 5.6 years and I love dolls     "
        )

    def test_task_7_string_longer(self):
        self.assertEqual(
            homework.task_7_insert_2_vars_into_string(-6.99999, "electrocardiograms"),
            "I have -6.9 years and I love electrocar"
        )


if __name__ == "__main__":
    unittest.main()
