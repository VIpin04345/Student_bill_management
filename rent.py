rent = int(input("enter your hostle flat rent:-"))
food = int(input("enter the ammount of ordered food:-"))
electicity_spend = float(input("enter the total of electricity spend:-"))
charge_per_unit = float(input("enter the charge per unit:-"))
# other = int(input("enter the other ammount whatever you spent:-"))
persons = int(input("enter the number of persons living in flat:-"))
bill = charge_per_unit * electicity_spend
all = (rent + food + bill) // persons
print(f"each person will pay rs.", all)
