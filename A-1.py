def calculate_change(paid, price):
    change = paid - price
    return change

snack_price = 30
print(" ===== Snack Vending MACHINE ===== ")
print("The Snack costs: " , snack_price , "units")
print("The accpected coins are: 1, 5, 10, 25 Units\n")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert a coin ( 1, 5 , 10 , 25 Units)"))

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid Coin inserted, Please insert a valid coin.")
        continue

    total_inserted += coin
    coins_inserted += 1
    print(f"Total inserted coins: {coins_inserted} units. Total so far: {total_inserted}\n")

    if total_inserted >= snack_price:
        print("Enough money inserted.\n")
        break

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your Snack . . .")

if change_due == 0:
    pass
else:
    print("Your change is: ", change_due , "Units")

print(" ===== VENDING Machine Summary ===== ")
print("Snack Price: ", snack_price, "Units")
print("Coins Inserted: ", coins_inserted, "Units")
print("Total paid: ", total_inserted, "Units")
print("Change given: ", change_due, "Units")
print("=" * 10)
print("Thank you for your purchase!")