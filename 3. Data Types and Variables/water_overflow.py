num = int(input())
litres_added = 0
max_capacity_ltr = 255
for litres in range(num):
    add_litres = int(input())
    if (max_capacity_ltr - add_litres) >= litres_added:
        litres_added += add_litres
    else:
        print('Insufficient capacity!')
print(litres_added)