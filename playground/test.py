import unittest


class TestGetTopK(unittest.TestCase):
    def test_get_top_k(self):
        nums = [1, 2, 2, 3, 3, 3]
        k = 2
        expected_output = [3, 2]
        self.assertEqual(get_top_k(nums, k), expected_output)

        nums = [4, 4, 4, 4, 4, 4, 4, 4]
        k = 1
        expected_output = [4]
        self.assertEqual(get_top_k(nums, k), expected_output)

        nums = [1, 2, 3, 4, 5]
        k = 5
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(get_top_k(nums, k), expected_output)


if __name__ == "__main__":
    unittest.main()
