from pyb import Timer
import time

i = 0
test_tim = [1, 2, 6, 8, 9, 10, 11, 12]

def timer_callback(t):
    global i
    print(t)
    i = i + 1

for tim in test_tim:
    try:
        tim_n = Timer(tim, freq=10)
        tim_n.callback(timer_callback)
        while i < 3:
            time.sleep(0.05)

        tim_n.deinit()
        i = 0
    except ValueError:
        print("ValueError " + str(tim))
