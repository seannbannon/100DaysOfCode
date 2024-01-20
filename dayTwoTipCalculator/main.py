print("Welcome to the Tip Calulator!")
price = float(input("What was the total cost of the bill? $"))
tip = int(input("How much tip would you like to leave?"))
tip_to_percent = (tip/100)
tip_in_dollars = price * tip_to_percent
number_of_people = int(input("How many people to split the bill?"))
final_amount = (price + tip_in_dollars) / number_of_people
# weird python syntax to get format 
rounded_final_amount = "{:.2f}".format(final_amount) 
print(f"Each person should pay: ${rounded_final_amount}")
