import os
import datetime as dt
import matplotlib.pyplot as plt

x = []
y = []

with open(os.path.expanduser('~') + '/code_line_log.txt') as f:
    lines = f.readlines()
    for line in lines:
        splits = line.split('=')
        if len(splits) != 2:
            break
        time = splits[0].strip()
        code_lines = splits[1].strip()
        x.append(dt.datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))
        y.append(int(code_lines))

plt.plot(x, y)
plt.gcf().autofmt_xdate()
plt.show()
