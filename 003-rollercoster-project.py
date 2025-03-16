print("Welcome to the Best Roller Coaster Ride!")
height = int(input("What is your height in cms? "))
bill = 0

if height >= 120:
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("You can ride without a ticket")
    else:
        bill = 12
        print("Adults tickets are $12.")

    photo_required = input("Do you want a photo taken? Y or N ").upper()
    if photo_required == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you grow taller before you can ride.")

