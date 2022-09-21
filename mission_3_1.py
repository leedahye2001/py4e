# 구구단 출력 함수
# 홀 수 번째만 출력하기
# 값 50이하만 출력하기

n = 1

def gugudan(num,n):
    while n <= 9:
        mul = num * n
        if mul <= 50:
            print(num,"X",n,"=",mul)
            n = n + 2
        else:
            break
try:
    num = int(input("몇 단?: "))
    print(num,"단")
except:
    print("\n[잘못된 입력입니다. 숫자를 입력해주세요.]\n")
    quit()

gugudan(num,n)
