'''
>>> from SRT import SRT
>>> srt = SRT("010-1234-xxxx", YOUR_PASSWORD)

>>> dep = '수서'
>>> arr = '부산'
>>> date = '20190930'
>>> time = '144000'
>>> trains = srt.search_train(dep, arr, date, time)
>>> trains
# [[SRT] 09월 30일, 수서~부산(15:00~17:34) 특실 예약가능, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(15:30~18:06) 특실 예약가능, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(16:00~18:24) 특실 매진, 일반실 예약가능,
# [SRT] 09월 30일, 수서~부산(16:25~18:45) 특실 예약가능, 일반실 예약가능, ...]

>>> reservation = srt.reserve(trains[1])
>>> reservation
# [SRT] 09월 30일, 수서~부산(15:30~18:06) 53700원(1석), 구입기한 09월 20일 23:38
'''
from SRT import SRT
from korail_message import *
import time as ti

PASSWORD = "happy4u#5"
srt = SRT("1692325169", PASSWORD)

dep = '동탄' 
arr = '오송'
date = '20220930'
time = '175800'

flag = True
while flag:
    ti.sleep(0.3)
    try:
        trains = srt.search_train(dep, arr, date, time)
        if trains:
            print(trains)
            for train in trains:
                if train.dep_time == time:
                    print(train)
                    if (train.special_seat_available()) & (~train.general_seat_available()):
                        seat = srt.reserve(train, special_seat=True)
                    else:
                        seat = srt.reserve(train)
                    flag = False
                    print(seat)
                    send_message(seat)
                else:
                    continue
        
    except:
        pass 