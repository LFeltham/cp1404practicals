# 1. Tax
"""
START
    DEFINE constants for tax rates and thresholds
    PRINT welcome message

    GET user input for income
    CONVERT income to a float

    IF income < TAX_THRESHOLD_LOW THEN
        total_tax = 0
    ELSE IF income <= TAX_THRESHOLD_HIGH THEN
        total_tax = income * TAX_RATE_LOW
    ELSE
        total_tax = income * TAX_RATE_HIGH
    ENDIF

    take_home_pay = income - total_tax

    PRINT total tax and take home pay
END
"""
TAX_RATE_LOW = 0.05
TAX_RATE_MEDIUM = 0.02
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_MEDIUM = 500
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))

if income < TAX_THRESHOLD_LOW:
    total_tax = 0
elif income <= TAX_THRESHOLD_MEDIUM:
    total_tax = income * TAX_RATE_MEDIUM
elif income <= TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
else:
    total_tax = income * TAX_RATE_HIGH

take_home_pay = income - total_tax
print("Total tax is: $", total_tax, sep="")
print("Take home pay is: $", take_home_pay, sep="")

# 2. Car Insurance
print("Welcome to Painz Car Rental")
age = int(input("Please enter your age: "))

if age < 18:
    print("Hire refused")
elif age < 25:
    print("Insurance required")
else:
    print("Insurance not required")
# # 0, 17, 18, 20, 24 25, 30, 50

# 3. Simple Password Checker
SECRET_PASSWORD = "123"
user_password = input("Please enter the password: ")
if user_password == SECRET_PASSWORD:
    print("Access granted")
else:
    print("Access denied")

# 4. Basketball
number_of_shots_attempted = int(input("Number of shots attempted: "))
number_of_shots_made = int(input("Number of shots made: "))

if number_of_shots_attempted > 0:
    shooting_percentage = (number_of_shots_made / number_of_shots_attempted) * 100
    print(f"Your shooting percentage is {shooting_percentage:.1f}%")

    if shooting_percentage >= 50:
        print("That's great!")

# 5. Rock of Ages
age = int(input("Please enter your age: "))
if age < 0 or age > 120:
    print("Invalid age")
else:
    if age <= 12:
        print("You're a child.")
    elif age <= 19:
        print("You're a teenager.")
    elif age <= 65:
        print("You're an adult.")
    else:
        print("You're a senior.")

# 6. Speeding Fines
speed = float(input("Enter your speed (km/h): "))
speed_limit = float(input("Enter the speed limit (km/h): "))

speed_over_limit = speed - speed_limit
penalty_amount = 0

if speed_over_limit < 0:
    print("You are within the speed limit.")
elif speed_over_limit < 11:
    penalty_amount = 309
elif speed_over_limit <= 20:
    penalty_amount = 464
elif speed_over_limit <= 30:
    penalty_amount = 696
elif speed_over_limit <= 40:
    penalty_amount = 1161
else:
    penalty_amount = 1780

if penalty_amount > 0:
    print(f"Your penalty amount is: ${penalty_amount}")
