# 두 개의 숫자 사이에 소수 몇 개인지 출력

prime=[]
def count_prime_number(n,m,prime):
    for i in range(n,m+1):
        l=0
        for j in range(2,i):
            if i%j==0:
                l=1
        if l==0:
            prime.append(i)
    print("소수개수", len(prime))

try:
    n = int(input("첫 번째 수 입력: "))
    m = int(input("두 번째 수 입력: "))
except:
    print("\n[잘못된 입력입니다. 숫자를 입력해주세요.]\n")
    quit()

count_prime_number(n,m,prime)
