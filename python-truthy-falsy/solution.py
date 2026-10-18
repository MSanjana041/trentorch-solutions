def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    #handle None
    if value is None:
        return False
    elif isinstance(value,int) and value == 0:
        return False
    elif isinstance(value,float) and value == 0.0:
        return False
    elif isinstance(value,str) and value == "":
        return False
    elif isinstance(value,list) and len(value) == 0:
        return False
    elif isinstance(value,tuple) and len(value) == 0:
        return False
    elif isinstance(value,dict) and len(value) == 0:
        return False
    elif isinstance(value,set) and len(value) == 0:
        return False
    else:
        return True


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    
    for i in values:
        if is_truthy(i):
            return i
    return None
