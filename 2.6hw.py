
address=input("What is your address")
days = int(input("how soon do you need the item"))
base_charge = 0
if days == 0:
    base_charge = 15
elif days == 1 or days == 2 or days == 3:
    base_charge =$10
elif days == 4 or days == 5 or days == 6:
    base_charge = $4.50
elif  days >= 7:
    base_charge = $2
else:
    print("choose a current day")
    
item_weight = 0









