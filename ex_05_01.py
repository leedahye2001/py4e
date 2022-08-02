#루프와 반복문 연습

num=0
tot=0.0
while True:
    sval=input('Enter a number: ')
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print('Invalid input')
        continue  # 잘못된 값을 입력했을 때 숫자를 더하지 않고 다시 위로 올라가 두번째 입력 받음
    #print(fval)

    num=num+1
    tot=tot+fval

#print('ALL DONE')
print(tot,num,tot/num)
