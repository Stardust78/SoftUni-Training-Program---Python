budget = float(input())
price_for_one_kg_floor = float(input())
total_colored_eggs = 0
total_loaves = 0

price_for_a_loaf = price_for_one_kg_floor + (price_for_one_kg_floor * 0.75) + ((price_for_one_kg_floor*1.25)/4)

while budget >= price_for_a_loaf:
    budget -= price_for_a_loaf
    total_colored_eggs += 3
    total_loaves += 1
    if total_loaves % 3 == 0:
        total_colored_eggs -= (total_loaves - 2)

print(f"You made {total_loaves} loaves of Easter bread! Now you have {total_colored_eggs} eggs and {budget:.2f}BGN left.")

