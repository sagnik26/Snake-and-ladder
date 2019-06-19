from PIL import Image
import random
end=100
def show():
    img=Image.open("ludo.jpg")
    img.show()


def check_ladder(point):
    if point==8:
        print("Here is a Ladder :) :) :)")
        return 26
    elif point==21:
        print("Here is a Ladder :) :) :)")
        return 82
    elif point==43:
        print("Here is a Ladder :) :) :)")
        return 77
    elif point==50:
        print("Here is a Ladder :) :) :)")
        return 91

    elif point==54:
        print("Here is a Ladder :) :) :)")
        return 93

    elif point==62:
        print("Here is a Ladder :) :) :)")
        return 96

    elif point==66:
        print("Here is a Ladder :) :) :)")
        return 87

    elif point==80:
        print("Here is a Ladder :) :) :)")
        return 100
    else:
        return point

def check_snake(point):
    if point == 44:
        print("oh shit! it's a Snake :( :( :(")
        return 22
    elif point == 46:
        print("oh shit! it's a Snake :( :( :(")
        return 5
    elif point == 48:
        print("oh shit! it's a Snake :( :( :(")
        return 9
    elif point == 52:
        print("oh shit! it's a Snake :( :( :(")
        return 11

    elif point == 55:
        print("oh shit! it's a Snake :( :( :(")
        return 7

    elif point == 59:
        print("oh shit! it's a Snake :( :( :(")
        return 17

    elif point == 64:
        print("oh shit! it's a Snake :( :( :(")
        return 36

    elif point == 69:
        print("oh shit! it's a Snake :( :( :(")
        return 33

    elif point == 73:
        print("oh shit! it's a Snake :( :( :(")
        return 1

    elif point == 83:
        print("oh shit! it's a Snake :( :( :(")
        return 19

    elif point == 92:
        print("oh shit! it's a Snake :( :( :(")
        return 51

    elif point == 95:
        print("oh shit! it's a Snake :( :( :(")
        return 24

    elif point == 98:
        print("oh shit! it's a Snake :( :( :(")
        return 28

    else:
        return point

def reached_end(point):
    if point==end:
        return True
    else:
        return False



def play():
    p1_name=input("Player 1, enter player.1 name : ")
    p2_name =input("Player 2, enter player.2 name : ")

    pp1=0

    pp2=0

    turn=0

    while(1):
        if turn%2==0:
            print(p1_name," your turn..")
            c=int(input("Press 1 to continue , 0 to quit"))

            if c==0:
                print(p1_name, " scored " ,pp1)
                print(p2_name, " scored ", pp2)
                print("Quitting the game....")
                break

            dice=random.randint(1,6)
            print("Dice showed : ",dice)
            pp1=pp1+dice

            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)

            if pp1>end:
                pp1=end

            print(p1_name," your score : ",pp1)

            if reached_end(pp1):
                print(p1_name,"won")
                break
        else:
            print(p2_name, " your turn..")
            c = int(input("Press 1 to continue , 0 to quit"))

            if c == 0:
                print(p1_name, " scored ", pp1)
                print(p2_name, " scored ", pp2)
                print("Quitting the game....")
                break

            dice = random.randint(1, 6)
            print("Dice showed : ", dice)
            pp2 = pp2 + dice

            pp2 = check_ladder(pp2)
            pp2 = check_snake(pp2)

            if pp2 > end:
                pp2 = end

            print(p2_name, " your score : ", pp2)

            if reached_end(pp2):
                print(p2_name, "won")
                break

        turn=turn+1




show()
play()
