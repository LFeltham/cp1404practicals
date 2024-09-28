num_items = -1
while num_items < 0:
    num_items_input = input("Number of items: ")
    if num_items_input.isdigit():
        num_items = int(num_items_input)
        if num_items < 0:
            print("Invalid number of items!")
    else:
        print("Please enter a valid integer.")

total_price = 0.0


for i in range(num_items):
    price = -1
    while price < 0:
        price_input = input(f"Price of item {i + 1}: ")
        if price_input.replace('.', '', 1).isdigit():
            price = float(price_input)
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
        else:
            print("Please enter a valid number.")

    total_price += price

if total_price > 100:
    total_price *= 0.9


print(f"Total price for {num_items} items is ${total_price:.2f}")
