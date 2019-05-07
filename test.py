import datetime
import unittest

from trie import Trie


GENDER = {
    True: 'Male',
    False: 'Female',
    None: 'Unknown'
}
TYPE = {
    True: 'name',
    False: 'patronymic',
    None: 'surname'
}
TYPE_REVERSED = {v: k for k, v in TYPE.items()}
GENDER_REVERSED = {v: k for k, v in GENDER.items()}
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
    SETUP_DONE = False

    def setUp(self):
        self.trie = Trie()
        if TestSmallTrieMethods.SETUP_DONE:
            return
        print("\nSETUP\n", datetime.datetime.now())
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
            TestSmallTrieMethods.SETUP_DONE = True

    def test_no_output_increment(self):
        """
        Regression
        """
        res1 = self.trie.get_by_prefix('иван')[:]
        res2 = self.trie.get_by_prefix('иван')[:]
        print("test_no_output_increment")
        print(res1)
        print(res2)
        print(datetime.datetime.now())
        self.assertEqual(res1, res2)

    def test_get_by_prefix_sort_desc_by(self):
        """
        Regression
        """
        res = self.trie.get_by_prefix_sort_desc_by('ив', 'age')
        print("test_get_by_prefix_sort_by")
        print(res)
        print(datetime.datetime.now())
        self.assertEqual(res, [IVANOVICH_51_TN, IVAN_31_TT])

    def test_len(self):
        """
        Regression
        """
        res = self.trie.get_by_prefix('%%')
        print("test_len")
        print(res)
        print(datetime.datetime.now())
        self.assertEqual(len(res), len(TEST_DATA_SMALL))

    def test_get_by_prefix_and_query(self):
        """
        Regression
        """
        res = self.trie.get_by_prefix_and_query("и", {"type": True, "gender": False})
        print("test_get_by_prefix_and_query")
        print(res)
        print(datetime.datetime.now())
        self.assertEqual(res, [IRINA_23_FT])


if __name__ == '__main__':
    unittest.main()

