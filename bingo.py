from random import randint
Choices = [[-1 for x in range(100)] for y in range(5)]
for i in range(0, 100):
    for j in range(0, 5):
        temp = int(input("Give me a value from 0 to 80: "))
        while True:
            if 0 <= temp <= 80:
                x = 0
                while x <= 5:
                    if temp != Choices[i][x]:
                        Choices[i][j] = temp
                        break
                    else:
                        print("You have given the same value again")
                        break
            break
total_played = 0
for x in range(0, 1000):
    num_played = 0
    Played = []
    while True:
        val = randint(0, 80)
        played = False
        for y in range(0, len(Played)):
            if Played[y] == val:
                played = True
        if played:
            print("The number " + val + " has been played")
        else:
            Played.append(val)
            num_played += 1
        Correct = [0 in range(100)]
        for i in range(0, 100):
            for j in range(0, 5):
                if val == Choices[i][j]:
                    Correct[i] += 1
        for i in range(0, 100):
            if Correct[i] == 5:
                print("Bingo")
                total_played += num_played
                break
avg = total_played/1000
print("Average number of numbers displayed " + avg)
