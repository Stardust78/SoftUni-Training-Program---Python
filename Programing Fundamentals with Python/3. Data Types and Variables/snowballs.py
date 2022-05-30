number_of_snowballs = int(input())
max_snowball_value = 0
for i in range(number_of_snowballs):
    snowball_weight = int(input())
    time_needed = int(input())
    snowball_quality = int(input())
    current_snowball_value = (snowball_weight / time_needed) ** snowball_quality
    if current_snowball_value > max_snowball_value:
        max_snowball_value = int(current_snowball_value)
        max_snowball_weight = snowball_weight
        max_time_needed = time_needed
        max_snowball_quality = snowball_quality
print(f"{max_snowball_weight} : {max_time_needed} = {max_snowball_value} ({max_snowball_quality})")
