def is_isogram(string):
    if not isinstance(string, str):
        raise Exception('input must be a string')
    string = string.replace(' ', '').lower().replace('-', '')
    duplicates = []
    for c in string:
        if c not in duplicates:
            duplicates.append(c)
        else:
            return False
    return True
