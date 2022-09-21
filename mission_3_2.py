# 가위바위보 심화버전

# 몇 판인지 입력받기
# 재입력 받기
# 게임종료 후, 총 전적 출력

import random

while True:
    try:
        games = int(input("몇 판을 진행하시겠습니까?: "))
        break
    except:
        print("숫자가 아닙니다. 올바르게 입력하세요")
        continue

draw=0
win=0
lose=0

#def rsp_advanced(games):
for i in range(games):
        rsp = int(input("가위 바위 보(왼쪽부터 0,1,2 - 숫자를 입력하세요): "))
        com = random.randint(0,2)

        if rsp == 0:
            my = "가위"
        elif rsp == 1:
            my = "바위"
        elif rsp == 2:
            my = "보"
        else:
            print("잘못된 입력입니다.\n")
            continue

        if com == 0:
            computer = "가위"
        elif com == 1:
            computer = "바위"
        else:
            computer = "보"

        print("나: ",my)
        print("컴퓨터: ",computer)

        try:
            if my == computer:
                print(i+1,"번째 판 비김!\n")
                draw=draw+1

            if my == "가위":
                if computer == "바위":
                    print(i+1,"번째 판 컴퓨터 승리!\n")
                    lose=lose+1
                elif computer == "보":
                    print(i+1,"번째 판 나의 승리!\n")
                    win=win+1
            elif my == "바위":
                if computer == "가위":
                    print(i+1,"번째 판 나의 승리!\n")
                    win=win+1
                elif computer == "보":
                    print(i+1,"번째 판 컴퓨터 승리!\n")
                    lose=lose+1
            elif my =="보":
                if computer == "가위":
                    print(i+1,"번째 판 컴퓨터 승리!\n")
                    lose=lose+1
                elif computer == "바위":
                    print(i+1,"번째 판 나의 승리!\n")
                    win=win+1
        except:
            print("올바르지 않은 형식\n")
        

print("[나의 전적: ",win,"승",draw,"무",lose,"패]")
print("[컴퓨터의 전적: ",lose,"승",draw,"무",win,"패]")


#rsp_advanced(games)
        
