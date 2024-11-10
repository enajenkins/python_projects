#Get Hours
input_hours = int(input())
#print(input_hours)
input_hours_in_seconds = input_hours * 3600

#Get Minutes
input_minutes = int(input())
#print(input_minutes)
input_minutes_in_seconds = input_minutes * 60

#Get Seconds
input_seconds = int(input())
#print(input_seconds)

#Total Seconds
print(f"Seconds: {input_hours_in_seconds + input_minutes_in_seconds + input_seconds}")
