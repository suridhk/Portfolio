# ==========================================
# TASK 1: BECKETT PIZZA PLAZA (4-FOR-3)
# ==========================================


print("Beckett Pizza Plaza 4-for-3 Offer")
print("=================================")

prices = []

# Get prices for 4 pizzas
for i in range(4):
    while True:
        user_input = input(f"Enter Price of Pizza #{i + 1}: ")

        try:
            price = float(user_input)

            if price <= 0:
                print("Please enter a valid price!")
            else:
                prices.append(price)
                break   # move to next pizza

        except ValueError:
            print("Please enter a valid price!")

# Calculate total and discount
total_price = sum(prices)
cheapest_price = min(prices)
final_total = total_price - cheapest_price

discount = int((cheapest_price / total_price) * 100)

print(f"\nOrder Total is £{final_total:.2f}, a fabulous discount of {discount}%!")