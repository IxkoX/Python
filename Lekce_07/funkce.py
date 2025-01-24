import datetime as dt
import time

# IMMUTABLE
XYZ = 100
JMENO = 'ASLKJASDKJ'
JMENO = JMENO[:4]

# MUTABLE

def work():
    data = {}
    now = dt.datetime.now()
    data[now.microsecond] = now.day
    return data

print(work())
time.sleep(0.1)
print(work())

