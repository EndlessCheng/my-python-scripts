# -*- coding: utf-8 -*-


def generate_odd(size, start=1):
    array = [x[:] for x in [[0] * size] * size]
    x, y = 0, size >> 1
    for i in range(start, size * size + start):
        array[x][y] = i
        tx, ty = (x - 1 + size) % size, (y + 1) % size
        if array[tx][ty] != 0:
            x = (x + 1) % size
        else:
            x, y = tx, ty
    return array


def generate_double_even(size):
    gap1 = size >> 2
    gap2 = size - gap1

    array = []
    cnt = 1
    recnt = size * size
    for i in range(size):
        tarray = []
        if i < gap1 or i >= gap2:
            for j in range(size):
                tarray.append(recnt if gap1 <= j < gap2 else cnt)
                cnt += 1
                recnt -= 1
        else:
            for j in range(size):
                tarray.append(cnt if gap1 <= j < gap2 else recnt)
                cnt += 1
                recnt -= 1
        array.append(tarray)
    return array


def generate_double_odd(size):
    half = size >> 1
    k = half >> 1

    array_a = generate_odd(half)
    array_b = generate_odd(half, 3 * half * half + 1)
    for i in range(half):
        for j in range(half >> 1):
            array_a[i][j], array_b[i][j] = array_b[i][j], array_a[i][j]
    for j in range(half - 1):
        array_a[k][j], array_b[k][j] = array_b[k][j], array_a[k][j]

    array_c = generate_odd(half, 2 * half * half + 1)
    array_d = generate_odd(half, half * half + 1)
    for i in range(half):
        for j in range(2, k + 1):
            array_c[i][j], array_d[i][j] = array_d[i][j], array_c[i][j]

    array = []
    for i in range(half):
        array_a[i].extend(array_c[i])
        array.append(array_a[i])
    for i in range(half):
        array_b[i].extend(array_d[i])
        array.append(array_b[i])
    return array


def print_array(array):
    num_len = len(str(len(array) * len(array)))
    for i in array:
        for j in i:
            print "%*d" % (num_len, j),
        print


if '__main__' == __name__:
    while True:
        size = input()
        assert isinstance(size, int) and size >= 3

        if size & 1:
            result = generate_odd(size)
        elif size & 3:
            result = generate_double_odd(size)
        else:
            result = generate_double_even(size)

        print_array(result)
