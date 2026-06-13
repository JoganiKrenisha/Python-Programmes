import time

# Current time
current_time = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))

print("Current Time:", current_time)

if 5 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 17:
    print("Good Afternoon!")
elif 17 <= hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")