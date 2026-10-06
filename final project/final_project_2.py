

print("Welcome to the car racing game, get ready to race!")

your_score=[]
opponent_score=[]
i=0

while True:
    import random
    game_menu=input("1.play 2.exit:")
    match game_menu:
        case"1":
            print("Let's get ready")
            i+=1
            print("round",i)
            your_speed=random.randint(50,120)
            opponent_speed=random.randint(50,120)
            your_score.append(your_speed)
            opponent_score.append(opponent_speed)
            print("your speed:", your_speed)
            print("opponent_speed", opponent_speed)

        case"2":
            print("bye bye")
            break

    if i==5:
        break
print("your total score:",sum(your_score))
print("opponent's total score", sum(opponent_score))

if sum(your_score)>sum(opponent_score):
        print("bravooo, you win")
else:
        print("sorryy,you lose")