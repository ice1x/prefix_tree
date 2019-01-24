"""
SQL-like query with prefix-tree:
"""
from datetime import datetime

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


class Node(object):
    def __init__(self, char, data):
        self.char = char
        self.level = 0
        self.data = data
        self.children = []


class Trie(Node):
    def insert(self, word, data):
        node = self
        for char in word:
            found_in_child = False

            for child in node.children:
                if child.char == char:
                    node = child
                    found_in_child = True
                    break

            if not found_in_child:
                new_node = Node(char, [])
                new_node.level = node.level + 1
                node.children.append(new_node)
                node = new_node
        node.data.append(data)

    def _find_last_node_by_prefix(self, prefix):
        node = self
        if not node.children:
            return

        for char in prefix:
            for child in node.children:
                if char in child.char:
                    node = child
                    break
        return node

    def _get_data_by_node(self, node):
        def _get_data_by_child(parent, result):
            for child in range(len(parent.children)):
                result += parent.children[child].data
                result = _get_data_by_child(parent.children[child], result)
            return result

        return _get_data_by_child(node, node.data)

    def _sort(self, data_dict, key_):
        data_sorted = sorted(data_dict, key=lambda value: value[key_])
        data_sorted.reverse()
        return data_sorted

    def get_by_prefix(self, prefix):
        return self._get_data_by_node(self._find_last_node_by_prefix(prefix))

    def get_by_prefix_sort_by(self, prefix, key_):
        return self._sort(self._get_data_by_node(self._find_last_node_by_prefix(prefix)), key_)


if __name__ == "__main__":
    trie = Trie('%%', [])
    for person in [
        {
            'name': 'иван',
            'age': 31,
            'gender': True,
            'type': True
        },
        {
            'name': 'ирина',
            'age': 23,
            'gender': False,
            'type': True
        },
        {
            'name': 'ио',
            'age': 3,
            'gender': True,
            'type': True
        },
        {
            'name': 'иванович',
            'age': 51,
            'gender': True,
            'type': None
        }

    ]:
        trie.insert(
            person['name'],
            {
                'age': person['age'],
                'gender': person['gender'],
                'type': person['type']}
        )

s = datetime.now()
# res = trie.get_by_prefix('иван')
res = trie.get_by_prefix_sort_by('и', 'age')
time_ = datetime.now() - s
for i in res:
    print(i)
print(len(res))
print(time_)
