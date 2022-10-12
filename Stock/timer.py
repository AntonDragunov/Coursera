import random

import schedule
import time

i = 0
price_done = 0
b = 0
print(i,b, price_done)
def day():
    price_done = 0
    i = 0
    print('НОВЫЙ ДЕНЬ!')


def vnutry_dny():
    for i in range(5):
        if price_done == 0:
            print("считаем пишем проверяем.", i)
            i += 1
            price_done = random.randint(0, 1)
            print(price_done)
        else:
            print("ПРАЙС ЗАГРУЖЕН!")


schedule.every(5).seconds.do(vnutry_dny)
schedule.every(10).seconds.do(day)
while True:
    schedule.run_pending()
    time.sleep(1)

# schedule.every(10).seconds.do(job)

# schedule.every(1).hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

# def job_with_argument(name):
#     print(f"I am {name}")
#
# schedule.every(10).seconds.do(job_with_argument, name="Peter")
