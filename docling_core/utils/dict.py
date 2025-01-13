def dig(element, *keys):
    try:
        _element = element
        for key in keys:
            _element = _element[safe_key(key)]
        return _element
    except:
        return None


def safe_key(key: any):
    if isinstance(key, int):
        return key

    return int(key) if key.isnumeric() else key