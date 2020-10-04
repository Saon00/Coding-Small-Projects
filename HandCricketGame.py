import random

print("""--------------- Welcome to Hand Cricket Game ---------------
                  Enter Number btwn 1 - 7 
""")
score = []
while True:
    player_1 = int(input("> "))
    cpu_1 = random.randint(1,7)
    print(cpu_1)
    if player_1>7:
        continue
    else:
        if player_1 != cpu_1:
            score.append(player_1)
        else:
            print("Out !!!!")
            break

total_score = sum(score)
print(f'Your total score is : {total_score}')
if (total_score>=50):
    print("Congratulation for Half Century")
elif (total_score>=100):
    print("Congratulation for Century")
elif (total_score>= 200):
    print("Congratulation for Double Century")
elif (total_score<50):
    print("You got an Average Score.")
