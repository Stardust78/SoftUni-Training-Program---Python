number_of_orders = int(input())
orders_total_price = 0

for current_order in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if (price_per_capsule < 0.01 or price_per_capsule > 100.00) or (days < 1 or days > 31) or (capsules_per_day < 1 or capsules_per_day > 2000):
        continue
    current_order_price = price_per_capsule * days * capsules_per_day
    orders_total_price += current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")
print(f"Total: ${orders_total_price:.2f}")