# 가위바위보 게임
import random

#컴퓨터
computer = random.randint(0,2)
def com(computer):
    if computer == 0:
        return "바위"
    elif computer == 1:
        return "가위"
    else:
        return "보"


#가위바위보
def rsp(my, computer):
    if my == "가위":
        print("컴퓨터: ", com(computer))

        if com(computer) == "보":
            print("나 승리!")
        elif com(computer) == "바위":
            print("컴퓨터 승리!")
        else:
            print("비김!")

    elif my == "바위":
        print("컴퓨터: ", com(computer))

        if com(computer) == "가위":
            print("나 승리!")
        elif com(computer) == "보":
            print("컴퓨터 승리!")
        else:
            print("비김!")

    else:
        print("컴퓨터: ", com(computer))

        if com(computer) == "바위":
            print("나 승리!")
        elif com(computer) == "가위":
            print("컴퓨터 승리!")
        else:
            print("비김!")


#나
my = input("나: ")

rsp(my, com(computer))
print("게임이 끝났습니다.")
