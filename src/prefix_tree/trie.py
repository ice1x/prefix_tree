"""
Prefix Trie
"""


class Node:  # pylint: disable=R0903
    """
    Class describes the data structure of node
    """
    __slots__ = ("char", "data", "children")

    def __init__(self, char: str, data: list):
        self.char = char
        self.data = data
        self.children = {}


class Trie(Node):
    """
    Class describes the tree hierarchy and routines to set/get data
    """

    def __init__(self, char: str = "%%", data: list | None = None):
        self.char = char
        self.data = data or []
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

    def _get_last_node_by_prefix(self, prefix: str) -> Node | None:
        """
        Args:
            prefix(str): - word/name prefix to search node where last symbol of word/name appears
        Return:
            node(Node)
        """
        if prefix == self.char:
            return self

        node = self
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node

    def _get_data_by_child(self, parent: Node, result: str) -> str:
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
            (list): list of dict"s
        """
        node = self._get_last_node_by_prefix(prefix)
        if node is None:
            return []
        return self._get_data_by_child(node, node.data)

    def get_by_prefix_sort_desc_by(self, prefix: str, key_: str) -> list:
        """
        Get sorted by key_ data where word starts with prefix
        Args:
            prefix(str): prefix to search
            key_(str): key to sort by (DESC)
        Return:
            result(list): list of dict"s
        """
        data_sorted = sorted(self._get_by_prefix(prefix), key=lambda value: value[key_])
        data_sorted.reverse()
        return data_sorted

    def get_by_prefix_and_query(self, prefix: str, query: dict) -> list:
        """
        Find all data where word starts with prefix and query pattern in data
        Args:
            prefix(str): prefix to search
            query(dict): pattern to match
        Return:
            result(list): list of dict"s
        """
        tmp_result = self._get_by_prefix(prefix)
        result = []
        for i in tmp_result:
            for j in query.items():
                if j not in i.items():
                    break
            else:
                result.append(i)
        return result

    def get_by_word_and_query(self, word: str, query: dict) -> dict | None:
        """
        Find node containing the word and return one data(dict) which is matched with query pattern

        Args:
            word(str): word to search node
            query(dict): pattern to match
        Return:
            (dict or None):
        """
        node = self._get_last_node_by_prefix(word)
        if node is None:
            return None
        for i in node.data:
            for j in query.items():
                if j not in i.items():
                    break
            else:
                return i
