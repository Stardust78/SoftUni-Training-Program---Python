ranges = int(input())
for i in range (ranges):
    for j in range(ranges):
        for k in range(ranges):
            print(f'{chr(97+i)}{chr(97+j)}{chr(97+k)}')
