import time
import random
from clown import Clown

def current_time_ms():
    return round(time.time() * 1000)


print(current_time_ms)

clown = Clown()

balloon_list = []

for i in range(10):
    balloon_list.append(clown.buy_balloon(random.randint(1,12)))

for balloon in balloon_list:
    print(balloon)