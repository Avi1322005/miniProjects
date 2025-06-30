import datetime
import time
from playsound import playsound

# Get alarm time from user
alarm_time = input("Set alarm (HH:MM in 24-hour format): ")
alarm_hour, alarm_minute = map(int, alarm_time.split(":"))

print(f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("⏰ Wake up!")
        playsound(r"C:\Users\HP\Downloads\alarm.mp3")
        break

    time.sleep(1)
