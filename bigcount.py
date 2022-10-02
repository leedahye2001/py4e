# 딕셔너리 이용해서 텍스트 파일에서 데이터 읽어와 가장 많이 나온 단어 출력하기

name=input('Enter file:')
f=open(name)

counts=dict()
for line in f:
    line=f.split()
    for word in words:
        counts[word]=count.get(word,0)+1

bigword=None;
bigcount=None;
for word,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigcount, bigword)
