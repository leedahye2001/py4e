# from 으로 시작하는 문장을 찾고, 분할하고, 세번째 단어를 출력,


# han = open('mbox-short.txt')
# for line in han:
#     line = line.rstrip()
#     wds = line.split()

#     if len(wds) < 3 or wds[0] != 'From' :
#         continue
#     print(wds[2])


han=open('mbox-short.txt')

for line in han:
    line=line.rstrip()
    wds=line.split()

    if wds[0] != from
        continue
    print(wds[2])