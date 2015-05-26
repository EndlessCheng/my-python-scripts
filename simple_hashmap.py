class LinearArray():
    def __init__(self):
        self.items = []

    def put(self, k, v):
        self.items.append((k, v))

    def get(self, k):
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError

    def delete(self, k):
        self.items.remove((k, self.get(k)))

    def is_exist(self, k):
        for key, val in self.items:
            if key == k:
                return True
        return False


class LinearTable():
    def __init__(self, size=10):
        self.arrays = []
        for i in range(size):
            self.arrays.append(LinearArray())

    def find_array(self, k):
        index = hash(k) % len(self.arrays)
        return self.arrays[index]

    def put(self, k, v):
        m = self.find_array(k)
        m.put(k, v)

    def get(self, k):
        m = self.find_array(k)
        return m.get(k)

    def delete(self, k):
        m = self.find_array(k)
        m.delete(k)

    def is_exist(self, k):
        m = self.find_array(k)
        return m.is_exist(k)


class HashMap():
    def __init__(self):
        self.table = LinearTable()
        self.count = 0

    def resize(self, size):
        new_table = LinearTable(size)

        for m in self.table.arrays:
            for k, v in m.items:
                new_table.put(k, v)

        self.table = new_table

    def map_put(self, k, v):
        if self.count == len(self.table.arrays):
            self.resize(self.count << 1)

        self.table.put(k, v)
        self.count += 1

    def map_get(self, k):
        return self.table.get(k)

    def map_delete(self, k):
        self.table.delete(k)

        self.count -= 1
        if self.count << 1 == len(self.table.arrays):
            self.resize(self.count)

    def is_exist(self, k):
        return self.table.is_exist(k)


import string

m = HashMap()
s = string.ascii_lowercase

for k, v in enumerate(s):
    m.map_put(k, v)

for k in range(20):
    m.map_delete(k)

for k in range(len(s)):
    if m.is_exist(k):
        print k, m.map_get(k)
