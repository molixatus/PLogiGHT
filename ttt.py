from datetime import datetime
import time
import random


hour = int(datetime.now().strftime('%H'))
minute = int(datetime.now().strftime('%M'))
print(hour)
print(type(hour))
print()

print(minute)
print(type(minute))
print()

randiff = random.randint(1,3)
print((40 * (randiff)))