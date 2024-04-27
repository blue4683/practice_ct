from collections import defaultdict
from datetime import datetime
import sys
input = sys.stdin.readline


def convert_datetime(date, time):
    year, month, day = map(int, date.split("-"))
    hour, minute = map(int, time.split(":"))
    return datetime(year, month, day, hour, minute)


n, l, f = input().rstrip().split()
l = l.replace('/', ':')
day, hour, minute = map(int, l.split(':'))
l = (day * 24 + hour) * 60 + minute

info = [input().rstrip().split() for _ in range(int(n))]
result = defaultdict()
fee = defaultdict()

for date, time, p, m in info:
    key_data = p + " " + m
    value_data = convert_datetime(date, time)
    if m not in result:
        result[m] = {}

    if p in result[m]:
        start_datetime = result[m].pop(p)
        diff_datetime = value_data - start_datetime
        diff_min = (diff_datetime.days * 1440) + (diff_datetime.seconds // 60)
        if diff_min > l:
            fee[m] = fee.get(m, 0) + (diff_min - l) * int(f)

    else:
        result[m][p] = value_data

if fee.keys():
    for key in sorted(fee.keys()):
        print(key, fee.get(key))

else:
    print(-1)
