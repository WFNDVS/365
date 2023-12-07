import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(m, s)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

# 设置专注时长为 25 分钟
countdown(25)
