quantity_of_decorations_per_day = int(input())
days_to_christmas = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
christmas_spirit = 0
total_price = 0

for current_day in range(1, days_to_christmas+1):
    if current_day % 11 == 0:
        quantity_of_decorations_per_day += 2
    if current_day % 2 == 0:
        total_price += (ornament_set_price * quantity_of_decorations_per_day)
        christmas_spirit += 5
    if current_day % 3 == 0:
        total_price += ((tree_skirt_price + tree_garland_price) * quantity_of_decorations_per_day)
        christmas_spirit += 13
    if current_day % 5 == 0:
        total_price += (tree_lights_price * quantity_of_decorations_per_day)
        christmas_spirit += 17
        if current_day % 3 == 0:
            christmas_spirit += 30
    if current_day % 10 == 0:
        total_price += (tree_lights_price + tree_garland_price + tree_skirt_price)
        christmas_spirit -= 20
if days_to_christmas % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {total_price}")
print(f"Total spirit: {christmas_spirit}")
