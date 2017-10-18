import json


class Foo:
    def __init__(self):
        self.x = 1
        self.y = 2


if __name__ == '__main__':
    mp = {'a': 1, 'b': Foo()}
    print json.dumps(mp, default=lambda obj: obj.__dict__)
