import unittest
from src.lab6 import compute_prefix
from src.lab6 import kmp_search


class TestStringSearch(unittest.TestCase):

    def test_compute_prefix(self):
        pattern_1 = "ABABCABAB"
        prefix_1 = compute_prefix(pattern_1)
        self.assertEqual(prefix_1, [0, 0, 1, 2, 0, 1, 2, 3, 4])

        pattern_2 = "AAAAA"
        prefix_2 = compute_prefix(pattern_2)
        self.assertEqual(prefix_2, [0, 1, 2, 3, 4])


    def test_kmp_search(self):
        haystack_1 = "ABABDABACDABABCABAB"
        needle_1 = "ABABCABAB"
        result_1 = kmp_search(haystack_1, needle_1)
        self.assertEqual(result_1, [10])

        haystack_2 = "ABCABCABAB"
        needle_2 = "ABAB"
        result_2 = kmp_search(haystack_2, needle_2)
        self.assertEqual(result_2, [6])
        haystack_3 = "AAAAA"
        needle_3 = "AA"
        result_3 = kmp_search(haystack_3, needle_3)
        self.assertEqual(result_3, [0, 1, 2, 3])

        haystack_4 = "ABCDEF"
        needle_4 = "G"
        result_4 = kmp_search(haystack_4, needle_4)
        self.assertEqual(result_4, [])

        haystack_5 = "AAAAA"
        needle_5 = ""
        result_5 = kmp_search(haystack_5, needle_5)
        self.assertEqual(result_5, [])



if __name__ == '__main__':
    unittest.main()
