"""
Prefix Trie
"""


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
    def __init__(self, char, data):
        self.char = char
        self.level = 0
        self.data = data
        self.children = {}
        self._SIZE = self.char.__sizeof__() + self.data.__sizeof__() + self.children.__sizeof__()


class Trie(Node, metaclass=Singleton):
    """
    Class describes the tree hierarchy and routines to set/get data
    """

    def __init__(
            self,
            char='%%',
            data=[]
    ):
        self.char = char
        self.data = data
        super().__init__(
            self.char,
            self.data
        )

    def insert(self, word, data):
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
                self._SIZE += char.__sizeof__()
                self._SIZE += [].__sizeof__()
                new_node = Node(char, [])
                new_node.level = node.level + 1
                node.children.update({char: new_node})
                self._SIZE += new_node.__sizeof__()
                node = new_node
        self._SIZE += data.__sizeof__()
        node.data.append(data)

    def _get_last_node_by_prefix(self, prefix):
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

    def _get_data_by_node(self, node):
        """
        Iterator runner
        Args:
            node(Node): - word/name prefix to search node where last symbol of word/name appears
        Return:
            result(list): - contain list of data(dict) inside
        """
        def _get_data_by_child(parent, result):
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
                _result = _get_data_by_child(parent.children[key], _result)
            return _result

        return _get_data_by_child(node, node.data)

    def _sort_desc(self, source, key_):
        """
        Descending sorting by key_
        Args:
            source(list): list of dict's should contain the key: key_
            key_(str): key to sort by
        Return:
            data_sorted(list): list sorted by key_
        """
        data_sorted = sorted(source, key=lambda value: value[key_])
        data_sorted.reverse()
        return data_sorted

    def get_by_prefix(self, prefix):
        """
        Find all data where word starts with prefix
        Args:
            prefix(str): prefix to search
        Return:
            (list): list of dict's
        """
        return self._get_data_by_node(self._get_last_node_by_prefix(prefix))

    def get_by_prefix_sort_desc_by(self, prefix, key_):
        """
        Find all data where word starts with prefix
        Args:
            prefix(str): prefix to search
            key_(str): key to sort by (DESC)
        Return:
            result(list): list of dict's
        """
        return self. _sort_desc(self._get_data_by_node(self._get_last_node_by_prefix(prefix)), key_)

    def get_by_prefix_and_query(self, prefix, query):
        """
        Find all data where word starts with prefix and query pattern in data
        Args:
            prefix(str): prefix to search
            query(dict): pattern to match
        Return:
            result(list): list of dict's
        """
        tmp_result = self.get_by_prefix(prefix)
        tmp_query = [(k, v) for k, v in query.items()]
        result = []
        for i in tmp_result:
            for j in tmp_query:
                if j not in i.items():
                    break
            else:
                result.append(i)
        return result

    def get_by_word_and_query(self, word, query):
        """
        Find node containing the word and return one data(dict) which is matched with query pattern
        #TODO There is a bug if a query pattern match with more than one data(dict) but for name's it shouldn't
        Args:
            word(str): word to search node
            query(dict): pattern to match
        Return:
            result(dict):
        """
        tmp_result = self._get_last_node_by_prefix(word).data
        tmp_query = [(k, v) for k, v in query.items()]
        for i in tmp_result:
            for j in tmp_query:
                if j not in i.items():
                    break
            else:
                return i

    def __len__(self):
        return self._SIZE
