year = int(input())
next_happy_year_condition = False

while not next_happy_year_condition:
    year += 1
    happy_year = set()
    for i in range(len(str(year))):
        happy_year.add(str(year)[i])
    next_happy_year_condition = len(str(year)) == len(happy_year)
print(year)

