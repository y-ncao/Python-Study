def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict['_end_'] = '_end_'
    return root

trie = make_trie('foo', 'bar', 'baz', 'barz')
print trie

def in_trie(word, trie):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        else:
            current_dict = current_dict[letter]
    return '_end_' in current_dict

print in_trie('ba', trie)
