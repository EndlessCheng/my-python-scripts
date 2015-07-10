def generate_next(digits):
    now = digits[0]
    count = 1
    for c in digits[1:]:
        if c == now:
            count += 1
        else:
            yield str(count) + str(now)
            now = c
            count = 1
    yield str(count) + str(now)


digits = raw_input()
with open('digits_result.txt', 'w') as f:
    for i in range(1, 15):
        write = '%2d ' % i + digits
        f.write(write + '\n')
        print write
        digits = ''.join(generate_next(digits))
