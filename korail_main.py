from korail2 import *
from korail_message import *
import time as ti
korail = Korail("1571795012", "happy4u#5") # with membership number

dep = '서울'
arr = '오송'
date = '20220708'
time = '173800'
psgrs = [AdultPassenger()]

flag = True
while flag:
    ti.sleep(0.5)
    try:
        trains = korail.search_train(dep, arr, date, time)
        print(trains)
        for train in trains:
            if train.dep_time == time:
                seat = korail.reserve(train, passengers=psgrs)
                flag = False
                send_message(seat)
            else:
                continue
        
    except:
        pass 