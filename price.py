import datetime
from sys import exit
import os

normal_morning = 2000
normal_afternoon = 2000
normal_night = 2500
friday_night = 3500
weekend_morning = 2500
weekend_afternoon = 3000
weekend_night = 3500
normal_whole_day = 18000
friday_whole_day = 20000
weekend_whole_day = 26000


national_holiday = [datetime.date(2019,4,1)]
booked_date = {datetime.date(2019,4,11):[8,12], datetime.date(2019,4,12):"all"}

'''
morning = [8, 9, 10, 11]
afternoon = [13, 14, 15, 16]
night = [18, 19, 20, 21]
'''

while True:
    n = input("請輸入年月日(EX:2019-1-2)").split("-")
    
    morning = []
    afternoon = []
    night = []

    reserved_time = input("請輸入欲租借之時段(EX:9-21)").split("-")
    reserved_time[0] = int(reserved_time[0])
    reserved_time[1] = int(reserved_time[1])
    real_time = []
    for i in range(reserved_time[0], reserved_time[1]):
        real_time.append(i)
        # if i >= 8 and i < 12:
        #     morning.append(i)
        # elif i >= 13 and i < 17:
        #     afternoon.append(i)
        # elif i >= 18 and i < 22:
        #     night.append(i)
        
    
    year = int(n[0])
    month = int(n[1])
    day = int(n[2])

    reserved_day = datetime.date(year, month, day)
    if reserved_day < datetime.datetime.now().date():
        print("請輸入未來之時段")
        # exit()
        continue
    if reserved_day in booked_date:
        if booked_date[reserved_day] == "all":
            print("本日已無剩餘時段")
            # exit()
            continue
        else:
            for i in range(booked_date[reserved_day][0], booked_date[reserved_day][1]):
                print(i)
                if i in real_time:
                    print("該時段已被預約")
                    # exit()
                    break
    week_day = reserved_day.weekday()
    if reserved_day in national_holiday:
        week_day = 5

    print("星期" + str(week_day+1))
    amount = 0
 
    if reserved_time[0] < 6 or reserved_time[1] > 23:
        print("可租借時間為6-23")
        # exit()
        continue

    else:
        if week_day in [0,1,2,3]:
            for session in real_time:
                if session < 12:
                    amount += normal_morning
                    if session >= 8:
                        morning.append(session)
                    if len(morning) > 3:
                        amount -= normal_morning

                elif session < 17:
                    amount += normal_afternoon
                    if session >= 13:
                        afternoon.append(session)
                    if len(afternoon) > 3:
                        amount -= normal_afternoon
                else:
                    amount += normal_night
                    if session >= 18:
                        night.append(session)
                    if len(night) == 3:
                        amount -= 500
                    elif len(night) > 3:
                        amount -= normal_night
            if len(morning) >= 3 and len(afternoon) >= 3:
                amount -= normal_afternoon
            if len(afternoon) >= 3 and len(night) >= 3:
                amount -= normal_night
            if len(morning) < 3 and len(afternoon) == 0 and len(night) == 0:
                amount += 6000
                amount -= normal_morning * len(morning)
            elif len(morning) == 0 and len(afternoon) < 3 and len(night) == 0:
                amount += 6000
                amount -= normal_afternoon * len(afternoon)
            elif len(morning) == 0 and len(afternoon) == 0 and len(night) < 3:
                amount += 7000
                amount -= normal_night * len(night)
            elif len(morning) < 3 and len(afternoon) < 3 and len(night) < 3:
                if len(night) == 0:
                    if len(morning) >= len(afternoon):
                        amount += 6000
                        amount -= normal_morning * len(morning)
                    else:
                        amount += 6000
                        amount -= normal_afternoon * len(afternoon)
                elif len(morning) == 0:
                    if len(afternoon) >= len(night):
                        amount += 6000
                        amount -= normal_afternoon * len(afternoon)
                    else:
                        amount += 7000
                        amount -= normal_night * len(night)
            if amount > normal_whole_day:
                amount = normal_whole_day




            
        elif week_day == 4:
            for session in real_time:
                if session < 12:
                    amount += normal_morning
                    if session >= 8:
                        morning.append(session)
                    if len(morning) > 3:
                        amount -= normal_morning

                elif session < 17:
                    amount += normal_afternoon
                    if session >= 13:
                        afternoon.append(session)
                    if len(afternoon) > 3:
                        amount -= normal_afternoon
                else:
                    amount += friday_night
                    if session >= 18:
                        night.append(session)
                    if len(night) == 3:
                        amount -= 500
                    elif len(night) > 3:
                        amount -= friday_night
            if len(morning) >= 3 and len(afternoon) >= 3:
                amount -= normal_afternoon
            if len(afternoon) >= 3 and len(night) >= 3:
                amount -= friday_night
            if len(morning) < 3 and len(afternoon) == 0 and len(night) == 0:
                amount += 6000
                amount -= normal_morning * len(morning)
            elif len(morning) == 0 and len(afternoon) < 3 and len(night) == 0:
                amount += 6000
                amount -= normal_afternoon * len(afternoon)
            elif len(morning) == 0 and len(afternoon) == 0 and len(night) < 3:
                amount += 10000
                amount -= friday_night * len(night)
            elif len(morning) < 3 and len(afternoon) < 3 and len(night) < 3:
                if len(night) == 0:
                    if len(morning) >= len(afternoon):
                        amount += 6000
                        amount -= normal_morning * len(morning)
                    else:
                        amount += 6000
                        amount -= normal_afternoon * len(afternoon)
                elif len(morning) == 0:
                    if len(afternoon) >= len(night):
                        amount += 6000
                        amount -= normal_afternoon * len(afternoon)
                    else:
                        amount += 10000
                        amount -= friday_night * len(night)
            if amount > friday_whole_day:
                amount = friday_whole_day

        
        else:
            for session in real_time:
                if session < 12:
                    amount += weekend_morning
                    if session >= 8:
                        morning.append(session)
                    if len(morning) > 3:
                        amount -= 2000

                elif session < 17:
                    amount += weekend_afternoon
                    if session >= 13:
                        afternoon.append(session)
                    if len(afternoon) > 3:
                        amount -= 3000
                else:
                    amount += weekend_night
                    if session >= 18:
                        night.append(session)
                    if len(night) == 3:
                        amount -= 500
                    elif len(night) > 3:
                        amount -= 3500
            if len(morning) >= 3 and len(afternoon) >= 3:
                amount -= weekend_afternoon
            if len(afternoon) >= 3 and len(night) >= 3:
                amount -= weekend_night
            if len(morning) < 3 and len(afternoon) == 0 and len(night) == 0:
                amount += 8000
                amount -= weekend_morning * len(morning)
            elif len(morning) == 0 and len(afternoon) < 3 and len(night) == 0:
                amount += 9000
                amount -= weekend_afternoon * len(afternoon)
            elif len(morning) == 0 and len(afternoon) == 0 and len(night) < 3:
                amount += 10000
                amount -= weekend_night * len(night)
            elif len(morning) < 3 and len(afternoon) < 3 and len(night) < 3:
                if len(night) == 0:
                    if len(morning) >= len(afternoon):
                        amount += 8000
                        amount -= weekend_morning * len(morning)
                    else:
                        amount += 9000
                        amount -= weekend_afternoon * len(afternoon)
                elif len(morning) == 0:
                    if len(afternoon) >= len(night):
                        amount += 9000
                        amount -= weekend_afternoon * len(afternoon)
                    else:
                        amount += 10000
                        amount -= weekend_night * len(night)
            if amount > weekend_whole_day:
                amount = weekend_whole_day
        print(amount)
        continue

