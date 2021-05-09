"""
Prefix Trie
"""


def sort_desc(source: list, key_: str) -> list:
    """
    Descending sorting by key_
    Args:
        source(list): list of dict's should contain the key: key_
        key_(str): key to sort by, value should be integer
    Return:
        data_sorted(list): list sorted by key_
    """
    data_sorted = sorted(source, key=lambda value: int(value[key_]))
    data_sorted.reverse()
    return data_sorted


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Node(object):
    """
    Class describes the data structure of node
    """

    def __init__(self, char: str, data: list):
        self.char = char
        self.data = data
        self.children = {}


class Trie(Node, metaclass=Singleton):
    """
    Class describes the tree hierarchy and routines to set/get data
    """

    def __init__(self, char='%%', data=[]):
        self.char = char
        self.data = data
        super().__init__(self.char, self.data)

    def insert(self, word: str, data: list):
        """
        Inserts word with attached data in the new or existent node
        Args:
            word(str):  - word/name
            data(list): - list of dictionary
        """
        node = self
        for char in word:
            found_in_child = False

            for key, value in node.children.items():
                if key == char:
                    node = value
                    found_in_child = True
                    break

            if not found_in_child:
                new_node = Node(char, [])
                node.children.update({char: new_node})
                node = new_node
        node.data.append(data)

    def _get_last_node_by_prefix(self, prefix: str) -> Node:
        """
        Args:
            prefix(str): - word/name prefix to search node where last symbol of word/name appears
        Return:
            node(Node)
        """
        node = self
        if not node.children:
            return

        for char in prefix:
            if node.children.get(char):
                node = node.children.get(char)
            else:
                break
        return node

    def _get_data_by_child(self, parent: Node, result: list) -> list:
        """
        Iterator
        Args:
            parent:
            result:
        Returns:
             (node.data)
        """
        _result = result[:]
        for key, value in parent.children.items():
            _result += value.data
            _result = self._get_data_by_child(parent.children[key], _result)
        return _result

    def _get_by_prefix(self, prefix: str) -> list:
        """
        Get data where word starts with prefix
        Args:
            prefix(str): prefix to search
        Return:
            (list): list of dict's
        """
        node = self._get_last_node_by_prefix(prefix)
        return self._get_data_by_child(node, node.data)

    def get_by_prefix_sort_desc_by(self, prefix, key_) -> list:
        """
        Get sorted by key_ data where word starts with prefix
        Args:
            prefix(str): prefix to search
            key_(str): key to sort by (DESC)
        Return:
            result(list): list of dict's
        """
        return sort_desc(self._get_by_prefix(prefix), key_)

    def get_by_prefix_and_query(self, prefix: str, query: dict) -> list:
        """
        Find all data where word starts with prefix and query pattern in data
        Args:
            prefix(str): prefix to search
            query(dict): pattern to match
        Return:
            result(list): list of dict's
        """
        tmp_result = self._get_by_prefix(prefix)
        tmp_query = [(k, v) for k, v in query.items()]
        result = []
        for i in tmp_result:
            for j in tmp_query:
                if j not in i.items():
                    break
            else:
                result.append(i)
        return result

    def get_by_word_and_query(self, word: str, query: dict) -> dict or None:
        """
        Find node containing the word and return one data(dict) which is matched with query pattern

        Args:
            word(str): word to search node
            query(dict): pattern to match
        Return:
            (dict or None):
        """
        tmp_query = [(k, v) for k, v in query.items()]
        for i in self._get_last_node_by_prefix(word).data:
            for j in tmp_query:
                if j not in i.items():
                    break
            else:
                return i
