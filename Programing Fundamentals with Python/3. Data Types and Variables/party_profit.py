from math import floor

companions = int(input())
current_day = int(input())
coins = 0

for current_day in range(1, current_day + 1):
    coins += 50
    if current_day % 10 == 0:
        companions -= 2
    if current_day % 15 == 0:
        companions += 5
    coins -= (2 * companions)
    if current_day % 3 == 0:
        coins -= (3 * companions)
    if current_day % 5 == 0:
        coins += (20 * companions)
        if current_day % 3 == 0:
            coins -= (2 * companions)
coins_per_companion = floor(coins / companions)
print(f"{companions} companions received {coins_per_companion} coins each.")
