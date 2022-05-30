number_of_persons = int(input())
elevator_capacity = int(input())
number_of_courses = 0
while number_of_persons > 0:
    if number_of_persons >= elevator_capacity:
        number_of_courses += (number_of_persons // elevator_capacity)
        number_of_persons = number_of_persons % elevator_capacity
    else:
        number_of_courses += 1
        break
print(number_of_courses)
