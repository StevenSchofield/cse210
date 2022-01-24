import time

from balloon import Balloon

def current_time_ms():
    return round(time.time() * 1000)

print(current_time_ms)

first_balloon = Balloon("Red")
second_balloon = Balloon("Blue")

balloon_list = []
for i in range(10):
    balloon_list.append(Balloon("Green"))

print(first_balloon)
print(second_balloon)

for balloon in balloon_list:
    print(balloon)