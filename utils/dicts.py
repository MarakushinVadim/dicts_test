def get_val(collection, key, default='git'):
    if collection != {}:
        if key in collection:
            return collection[key]
        return default
    return default