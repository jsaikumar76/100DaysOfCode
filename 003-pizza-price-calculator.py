print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

price = 0
if size == "S":
    price += 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price += 20

elif size == "L":
    price += 25

else:
    print("Sorry we only serve Small, Medium and Large.")

if (size == "M" or size == "L") and pepperoni == "Y":
    price += 3
elif pepperoni == "N":
    pass
else:
    print("Please choose Yes or No")

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")
