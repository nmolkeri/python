import time
import webbrowser
import random

a = "https://www.youtube.com/watch?v=Sl_JnlsZIVs"
b = "https://www.youtube.com/watch?v=QdvLj9Wr8Q0"
c = "https://www.youtube.com/watch?v=QdvLj9Wr8Q0"


Alarm = input("Enter the alarm time: ")
print(Alarm)

Time = time.strftime("%H:%M")

print(Time)

while Time != Alarm:
   print("Its not time yet")
   Time = time.strftime("%H:%M")
   time.sleep(1)

if Time == Alarm:
   print("Its time to wake up")
   randomVideo = random.choice([a,b,c])
   webbrowser.open(randomVideo)

