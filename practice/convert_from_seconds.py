''' Convert seconds into hours, minutes, and remaining seconds '''

# Define how many seconds are in each time unit
secs_in_min = 60
secs_in_hour = 3600

# Get seconds to convert from user
total_seconds = int(input("Enter the total number of seconds: "))

# 1. Hours:
# Extract maximum number of hours possible via floor division. Floor division returns the maximun whole number possible.
hours = total_seconds // secs_in_hour 
print(f"Hours: {hours}")

# 2. Minutes:
# Determine maximum number of minutes possible using modulus. Modulus isolates the remaninng seconds after the maximun number of hours have been determined.
seconds_left = total_seconds % secs_in_hour
# Then use floor division to return the maximun number of minutes from the second that are left afer removing the hours
minutes = seconds_left // secs_in_min
print(f"Minutes: {minutes}")

# 3. Seconds:
# Determine seconds by isolating the remaining seconds from the original input using modulus and the number of seconds in a minute.
seconds = total_seconds % secs_in_min 
print(f"Seconds: {seconds}")
