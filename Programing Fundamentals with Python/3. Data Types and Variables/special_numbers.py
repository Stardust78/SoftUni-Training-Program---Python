n = int(input())

for i in range(1, n+1):
    is_special = False
    result = 0
    string = str(i)
    if int(len(string)) == 1:
        result = i
    else:
        for j in range(len(string)):
            num = int(string[j])
            result += num
    if result == 5 or result == 7 or result == 11:
        is_special = True
    print(f'{i} -> {is_special}')
