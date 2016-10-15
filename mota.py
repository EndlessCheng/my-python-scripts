# -*- coding: utf-8 -*-
import sys


def get_critical_point(hp, def_):
    hp = int(hp)
    def_ = int(def_)

    len_atk1 = len(str(hp + def_))
    len_atk2 = len(str(hp + def_ - 1))
    len_times = len(str(hp - 1))

    last_time = -1
    last_atk = 1
    for atk in range(2, hp + 1):
        if (hp - 1) / atk != last_time:
            print "your atk: %*d ~ %*d = %*d time(s)" % (
                len_atk1, last_atk + def_,
                len_atk2, atk - 1 + def_,
                len_times, (hp - 1) / last_atk
            )
            last_atk = atk
            last_time = (hp - 1) / atk
    print "your atk: %*d + %s = %*d time(s)" % (len_atk1, hp + def_, " " * len_atk2, len_times, 0)


get_critical_point(sys.argv[1], sys.argv[2])
