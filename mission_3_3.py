# 짝수인 중앙값 출력하기

def find_even_number(n,m):
    for i in range(n, m+1):
        if i%2==0 and i<m:
            print(i, "짝수")
            if i == (m+1)/2:
                print(int((m+1)/2), "중앙값")

try:
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))
except:
    print("\n[잘못된 입력입니다. 숫자를 입력해주세요.]\n")
    quit()

find_even_number(n,m)
