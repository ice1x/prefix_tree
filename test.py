import unittest

from trie import Trie


IVAN_31_TT = {
        'name': 'иван',
        'age': 31,
        'gender': True,
        'type': True
    }
IRINA_23_FT = {
        'name': 'ирина',
        'age': 23,
        'gender': False,
        'type': True
    }
IO_3_TT = {
        'name': 'ио',
        'age': 3,
        'gender': True,
        'type': True
    }
IVANOVICH_51_TN = {
        'name': 'иванович',
        'age': 51,
        'gender': True,
        'type': None
    }
TEST_DATA_SMALL = [
    IVAN_31_TT,
    IRINA_23_FT,
    IO_3_TT,
    IVANOVICH_51_TN
]


class TestSmallTrieMethods(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        for person in TEST_DATA_SMALL:
            self.trie.insert(
                person['name'],
                {
                    'name': person['name'],
                    'age': person['age'],
                    'gender': person['gender'],
                    'type': person['type']
                }
            )

    def test_no_output_increment(self):
        """
        Regression
        """
        res1 = self.trie.get_by_prefix('иван')[:]
        res2 = self.trie.get_by_prefix('иван')[:]
        self.assertEqual(res1, res2)

    def test_get_by_prefix_sort_by(self):
        """
        Regression
        """
        res = self.trie.get_by_prefix_sort_desc_by('ив', 'age')
        self.assertEqual(res, [IVANOVICH_51_TN, IVAN_31_TT])

        # print(len(res))
        # print(self.trie.get_by_prefix_and_query("и", {"type": True, "gender": False}))


if __name__ == '__main__':
    unittest.main()

