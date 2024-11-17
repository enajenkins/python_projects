'''
Write a program to calculate the total price for car wash services. 
A base car wash is $10. 
A dictionary with each additional service and the corresponding cost has been provided. 
Two additional services can be selected. 
A '-' signifies an additional service was not selected. 
Output all selected services, according to the input order, 
along with the corresponding costs and then the total price for all car wash services.
'''

services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()
#service_choice3 = 'Vacuum'
#service_choice4 = 'Air freshener'

selected_services = [service_choice1, service_choice2]

total_price = 0

print("ZyCar Wash")   
print(f"Base car wash -- ${base_wash}")   

for service_choice in selected_services:
    if service_choice in services:
        print(f"{service_choice} -- ${services.get(service_choice)}")
        total_price = total_price + services.get(service_choice)
    else:
        break
        
print("----")   
print(f"Total price: ${total_price + 10}")       
        