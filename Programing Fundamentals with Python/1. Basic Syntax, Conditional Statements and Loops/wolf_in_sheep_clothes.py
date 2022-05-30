input_string = input()
word = input_string.split(", ")
queue = []
for i in range((len(word)-1), -1, -1):
    queue.append(str(word[i]))
if queue[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    for i in range ( 1, len(queue)):
        if queue[i] == "wolf":
            print(f"Oi! Sheep number {i}! You are about to be eaten by a wolf!")
