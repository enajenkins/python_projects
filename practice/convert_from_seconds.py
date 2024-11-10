secs_in_min = 60
secs_in_hour = 3600

#Get Input
total_seconds = int(input())

#Extract maximum number of hours possible via floor dIvision
hours = total_seconds // secs_in_hour 
print(f"Hours: {hours}")

#Determine maximum number of minutes possible using modulus
seconds_left = total_seconds % secs_in_hour
minutes = seconds_left // secs_in_min
print(f"Minutes: {minutes}")

#Determine remaining seconds by subtracting minutes from modulus remainder
seconds = seconds_left - (minutes * secs_in_min)
print(f"Seconds: {seconds}")
