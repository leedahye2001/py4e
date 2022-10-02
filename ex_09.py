# 딕셔너리를 활용한 데이터 빈도수 측정

fname=input('Enter name: ')
if len(fname)<1 :
    fname='/Users/leedahye/Desktop/py4e/ex/clown.txt'
hand=open(fname)

# 단어 추출
di=dict()
for line in hand:
    line=line.rstrip()
    words=line.split()
    for word in words:
        di[word]=di.get(word,0)+1

# 가장 많은 단어 수 출력
largest = -1
theword=None

for key, value in di.items():
    #print(key, value)
    if value>largest:
        largest=value
        theword=key
print('Done!',"\ncount : ",largest, "\nthe word : ",theword)

    