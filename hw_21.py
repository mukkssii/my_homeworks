def return_only_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return str(result)

    return wrapper
