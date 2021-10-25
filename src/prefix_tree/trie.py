"""
Prefix Trie
"""
from typing import List, Dict, Text


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
    __slots__ = ('char', 'data', 'children')

    def __init__(self, char: str, data: List):
        self.char = char
        self.data = data
        self.children = {}


class Trie(Node):
    """
    Class describes the tree hierarchy and routines to set/get data
    """

    def __init__(self, char='%%', data=[]):
        self.char = char
        self.data = data
        super().__init__(self.char, self.data)

    def insert(self, word: str, data: List):
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

    def _get_last_node_by_prefix(self, prefix: Text) -> Node:
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

    def _get_data_by_child(self, parent: Node, result: List) -> List:
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

    def _get_by_prefix(self, prefix: Text) -> List:
        """
        Get data where word starts with prefix
        Args:
            prefix(str): prefix to search
        Return:
            (list): list of dict's
        """
        node = self._get_last_node_by_prefix(prefix)
        return self._get_data_by_child(node, node.data)

    def get_by_prefix_sort_desc_by(self, prefix, key_) -> List:
        """
        Get sorted by key_ data where word starts with prefix
        Args:
            prefix(str): prefix to search
            key_(str): key to sort by (DESC)
        Return:
            result(list): list of dict's
        """
        data_sorted = sorted(self._get_by_prefix(prefix), key=lambda value: int(value[key_]))
        data_sorted.reverse()
        return data_sorted

    def get_by_prefix_and_query(self, prefix: Text, query: Dict) -> List:
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

    def get_by_word_and_query(self, word: Text, query: Dict) -> Dict or None:
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
