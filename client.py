import json
from .trie import Trie
from starlette.responses import PlainTextResponse

GENDER_MAPPING = {'t': 'male', 'f': 'female', None: 'unknown'}
TYPE_MAPPING = {'t': 'firstname', 'f': 'middlename', '': 'lastname'}


def get_trie():
    """
    Load data to prefix trie

    Returns:
        (Trie): prefix trie with loaded data
    """
    trie = Trie()
    with open("./prefix_trie/test_dataset.txt", "r") as f:
        for line in f.readlines():
            data = line.split(',')
            trie.insert(
                data[0],
                {
                    'name': data[0],
                    'amount': data[1],
                    'gender': data[2],
                    'type': data[3].strip()
                }
            )
    return trie


TRIE = get_trie()


def replace_placeholders(source_data):
    """
    Replace placeholders by user-friendly values
    Args:
        source_data(list): list of dict's with data from Trie

    Returns:
        (starlette.responses.PlainTextResponse): list of dict's->JSON with data from Trie with replaced placeholders

    """
    output = []
    for row in source_data:
        output_row = row.copy()
        output_row['type'] = TYPE_MAPPING.get(output_row['type'])
        output_row['gender'] = GENDER_MAPPING.get(output_row['gender'])
        output.append(output_row)
    print(type(PlainTextResponse(json.dumps(output, ensure_ascii=False))))
    return PlainTextResponse(json.dumps(output, ensure_ascii=False))


def suggest(query: str, count: int):
    """
    Get suggestions by name prefix
    Args:
        query(str): name prefix
        count(int): max length of suggestion list

    Returns:
        (starlette.responses.PlainTextResponse): suggestions
    """
    if count > 100:
        count = 100
    result = TRIE.get_by_prefix_sort_desc_by(query, 'amount')[:count]
    return replace_placeholders(result)


def parse(query: str):
    """
    Parse full name by text string

    Args:
        query(str): text string which may contain full name

    Returns:
        (starlette.responses.PlainTextResponse): full name parsed
    """
    tokens = query.split()
    result = []
    for token in tokens:
        token_parse_result = TRIE.get_by_word_and_query(token, {})
        if not token_parse_result:
            continue
        result.append(token_parse_result)
    return replace_placeholders(result)
