import time
import random
from game.clown import Clown
from game.child import Child
from game.person import Person

def current_time_ms():
    return round(time.time() * 1000)

persons = [Clown(), Person(), Child(), Clown()]

for i in range(len(persons)):
    person:Person = persons[i]
    print(f"This one says: {person.speak()}")