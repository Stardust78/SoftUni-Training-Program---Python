divisor = int(input())
boundary = int(input())
for max_number in range(boundary, 0, -1):
    if max_number % divisor == 0:
        print(max_number)
        break
