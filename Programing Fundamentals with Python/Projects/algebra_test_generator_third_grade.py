import random


def div(delimo, delitel):
    result = delimo // delitel
    ostatak = delimo % delitel
    print(f"{delimo} : {delitel} = ?")
    input_result = int(input(f"Скъпо момче, напиши частното: "))
    if ostatak != 0:
        input_ostatak = int(input("Скъпо момче, напиши остатъка:  "))
        while result != input_result and ostatak != input_ostatak:
            print("Пробвай отново да решиш примера :-)")
            input_result = int(input("Скъпо момче, напиши частното:  "))
            input_ostatak = int(input("Скъпо момче, напиши остатъка:  "))
        else:
            print("Верен резултат!")

    else:
        while result != input_result:
            print("Пробвай отново да решиш примера :-)")
            input_result = int(input("Скъпо момче, напиши частното:  "))
        else:
            print("Верен резултат!")


def multi(m1, m2):
    result = m1 * m2
    print(f"{m1} x {m2} = ?")
    input_result = int(input("Скъпо момче, напиши произведението:  "))
    while result != input_result:
        print("Пробвай отново да решиш примера :-)")
        input_result = int(input("Скъпо момче, напиши произведението:  "))
    else:
        print("Верен резултат!")
def circumferences(choice):
    side_one = random.randint(10, 90)
    choice_1 = random.randint(1, 3)
    if choice % 2 == 0:
        circumference = 3 * side_one
        if choice_1 == 1:
            print(f"Сами, обиколката на равностранен триъгълник е равна на {circumference}см. Намери дължината на страната му.")
            input_side = int(input("Въведи дължината на страната на триъгълника:  "))
            while side_one != input_side:
                print("Опитай отново.")
                input_side = int(input("Въведи дължината на страната на триъгълника:  "))
            else:
                print('Верен отговор!')
        else:
            print(f"Сами, страната на равностранен триъгълник е равна на {side_one}см. Намери обиколката му.")
            input_circumference = int(input("Въведи обиколката на триъгълника:  "))
            while circumference != input_circumference:
                print("Опитай отново.")
                input_circumference = int(input("Въведи обиколката на триъгълника:  "))
            else:
                print('Верен отговор!')
    elif choice % 3 == 0:
        leg = side_one + choice
        if leg % 2 != 0:
            leg += 1
        circumference = side_one + (2 * leg)
        if choice_1 == 1:
            print(f"Сами, обиколката на равнобедрен триъгълник е равна на {circumference}см, а основата {side_one}см. Намери дължината на бедрото му.")
            input_leg = int(input("Въведи дължината на бедрото на триъгълника:  "))
            while leg != input_leg:
                print("Опитай отново.")
                input_leg = int(input("Въведи дължината на бедрото на триъгълника:  "))
            else:
                print('Верен отговор!')
        elif choice_1 == 2:
            print(f"Сами, основата на равнобедрен триъгълник е равна на {side_one}см. а бедрото {leg}см. Намери обиколката му.")
            input_circumference = int(input("Въведи обиколката на триъгълника:  "))
            while circumference != input_circumference:
                print("Опитай отново.")
                input_circumference = int(input("Въведи обиколката на триъгълника:  "))
            else:
                print('Верен отговор!')
        elif choice_1 == 3:
            print(f"Сами, обиколката на равнобедрен триъгълник е равна на {circumference}см. а бедрото {leg}см. Намери основата му.")
            input_side_one = int(input("Въведи обиколката на триъгълника:  "))
            while side_one != input_side_one:
                print("Опитай отново.")
                input_side_one = int(input("Въведи дължината на основата на триъгълника:  "))
            else:
                print('Верен отговор!')
    elif choice % 5 == 0:
        circumference = 4 * side_one
        if choice_1 == 1:
            print(
                f"Сами, страната на квадрат е равна на {side_one}см. Намери обиколката му.")
            input_circumference = int(input("Въведи обиколката на квадрата:  "))
            while circumference != input_circumference:
                print("Опитай отново.")
                input_circumference = int(input("Въведи обиколката на квадрата:  "))
            else:
                print('Верен отговор!')
        else:
            print(f"Сами, обиколката на квадрат е равна на {circumference}см. Намери страната му.")
            input_side_one = int(input("Въведи страната на квадрата:  "))
            while side_one != input_side_one:
                print("Опитай отново.")
                side_one = int(input("Въведи страната на квадрата:  "))
            else:
                print('Верен отговор!')
    else:
        side_two = side_one + choice
        circumference = (side_one + side_two) * 2
        if choice_1 == 1:
            print(f"Сами, страните на правоъгълник са {side_one}см. и {side_two}см. Намери обиколката му.")
            input_circumference = int(input("Въведи обиколката на правоъгълника:  "))
            while circumference != input_circumference:
                print("Опитай отново.")
                print(circumference)
                input_circumference = int(input("Въведи обиколката на правоъгълника:  "))
            else:
                print('Верен отговор!')
        else:
            print(f"Сами, обиколката на правоъгълник е равна на {circumference}см. а едната му страна на {side_two}см. Намери дължината на дръгата му страна.")
            input_side_one = int(input("Въведи страната на правоъгълника:  "))
            while side_one != input_side_one:
                print("Опитай отново.")
                print(side_one)
                input_side_one = int(input("Въведи страната на правоъгълника:  "))
            else:
                print('Верен отговор!')


count = int(input("Въведи броя на задачите:  "))
ch = random.randint(1, 15)

for i in range(count):
    number_one = random.randint(20, 400)
    number_two = random.randint(1, 10)
    choice = random.randint(1, 15)
    if choice % 2 == 0:
        multi(number_one, number_two)
    else:
        div(number_one, number_two)
for i in range(ch, ch+3):
    circumferences(i)

print("Сами, ти се справи отлично! Не спирай да се упражняваш за да се справяш с още по-голяма лекота! :-)")
