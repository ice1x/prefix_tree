![PyPI - Downloads](https://img.shields.io/pypi/dm/prefix-tree)
![PyPI](https://img.shields.io/pypi/v/prefix-tree)
![License](https://img.shields.io/pypi/l/prefix-tree)

# 📦 prefix\_tree

A lightweight, pure-Python prefix tree (trie) implementation for fast in-memory prefix search, autocomplete, and filtering based on metadata. Useful for building autocomplete engines, suggestion systems, and efficient word lookups.

---

## ✨ Features

* In-memory key-value storage using a prefix tree (trie)
* Fast search by prefix
* Sortable results by dictionary key
* Query filtering by field values (exact match)
* Pure Python, no dependencies
* Compatible with Python 3.10+

---

## 📅 Installation

```bash
pip install prefix-tree
```

---

## 🚀 Usage Example

```python
from prefix_tree import Trie

# Create a new trie
trie = Trie()

# Insert words with associated metadata
trie.insert("hello", {"name": "hello", "amount": 10, "gender": "t", "type": "t"})
trie.insert("help", {"name": "help", "amount": 5, "gender": "f", "type": "f"})
trie.insert("hell", {"name": "hell", "amount": 7, "gender": "t", "type": "f"})

# Search by prefix and sort by amount (descending)
results = trie.get_by_prefix_sort_desc_by("hel", "amount")
print(results)
# Output:
# [{'name': 'hello', 'amount': 10, ...}, {'name': 'hell', 'amount': 7, ...}, {'name': 'help', 'amount': 5, ...}]

# Search by prefix and filter by query
filtered = trie.get_by_prefix_and_query("hel", {"gender": "t"})
print(filtered)
# Output:
# [{'name': 'hello', 'amount': 10, ...}, {'name': 'hell', 'amount': 7, ...}]
```

---

## 🔧 Build & Upload to PyPI

```bash
python3 -m build
twine upload dist/*
```

---

## 🧠 Use Cases

* Autocomplete and typeahead suggestions
* Named entity lookup with filters
* Efficient in-memory keyword searches
* Building simple text-based databases

---

## 🔗 Related Projects

* [autocomplete-full-name (GitHub)](https://github.com/ice1x/autocomplete-full-name)

---

## 📚 Keywords

`autocomplete`, `trie`, `prefix search`, `in-memory database`, `suggestions`, `python trie`, `word search`, `autocompletion`, `fast lookup`, `filtering`

---

## 📝 License

MIT License (see [LICENSE](./LICENSE) for details)

---

## ✨ Author

Created by ilia iakhin