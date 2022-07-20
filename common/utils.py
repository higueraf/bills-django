
def in_dict(key, dictionary):
    if key in dictionary:
        if dictionary[key] is not None:
            return True
    return False


def update_instance(key, dictionary):
    if key in dictionary:
        if dictionary[key] is not None:
            return True
    return False