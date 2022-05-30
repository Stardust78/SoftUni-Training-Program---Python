checked_digit = int(input())
is_natural = True
for current_digit in range(2, checked_digit):
    flag = checked_digit % current_digit
    if flag == 0:
        is_natural = False
        break
print(is_natural)
