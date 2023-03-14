def safe_get(dct: dict, keys: list):
    for key in keys:
        try:
            dct = dct[key]
        except KeyError:
            return None
    return dct
