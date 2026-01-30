prices = {
    "AAPL": 180,
    "TSLA": 250,
}
print("Stock Portfolio Tracker")
total_investment = 0
records = []
n = int(input("How many stocks do you want to add? "))
for i in range(n):
    print("Stock", i + 1)
    name = input("Enter stock name (AAPL/TSLA): ").upper()
    quantity = int(input("Enter quantity: "))
    if name in prices:
        price = prices[name]
        value = price * quantity
        total_investment += value
        records.append("{name}  {quantity}  {value}")
        print("Investment value:", value)
    else:
        print("Stock not found in price list")

print("Total Investment Value =", total_investment)
# Save result to file
with open("portfolio.txt", "w") as file:
    file.write("Stock  Quantity  Value")
    for r in records:
        file.write(r + "\n")
    file.write("Total Investment = {total_investment}")

print("Data saved to portfolio.txt")
