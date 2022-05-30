a = int(input())
b = int(input())
c = a+b
print('Before:')
print(f'a = {a}')
print(f'b = {b}')
a = c-a
b = c-b
print('After:')
print(f'a = {a}')
print(f'b = {b}')