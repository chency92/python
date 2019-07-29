# 1、获取秒级时间戳与毫秒级时间戳

import time
import datetime

t = time.time()

print(t)  # 原始时间数据
print(int(t))  # 秒级时间戳
print(int(round(t * 1000)))  # 毫秒级时间戳

nowTime = lambda: int(round(t * 1000))
print(nowTime())  # 毫秒级时间戳，基于lambda

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 日期格式化

# 2、将日期转为秒级时间戳

dt = '2018-01-01 10:40:30'
ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))
print(ts)

# 3、将秒级时间戳转为日期
ts = 1515774430
dt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(ts))
print(dt)
