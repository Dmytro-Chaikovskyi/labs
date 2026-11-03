from functools import wraps

def add_exclamation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            if not result.endswith('!'):
                result += '!'
        return result
    return wrapper
