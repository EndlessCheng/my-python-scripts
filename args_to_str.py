import itertools

def args_to_str(*args, **kwargs):
    return ', '.join(itertools.chain(map(repr, args), (f'{k}={v!r}' for k, v in kwargs.items())))
