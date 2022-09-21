# 연봉 계산기

monthly_payment = int(input("월급 입력: "))
yearly_payment = 12 * monthly_payment #세전 연봉

def tax(yearly_payment):
    if yearly_payment <= 1200:
        return yearly_payment * (1-0.06)
    elif yearly_payment <= 4600:
        return yearly_payment * (1-0.15)
    elif yearly_payment <= 8800:
        return yearly_payment * (1-0.24)
    elif yearly_payment <= 15000:
        return yearly_payment * (1-0.35)
    elif yearly_payment <= 30000:
        return yearly_payment * (1-0.38)
    elif yearly_payment <= 50000:
        return yearly_payment * (1-0.40)
    else:
        return yearly_payment * (1-0.42)

print("세전 연봉: ", yearly_payment, "만원")
print("세후 연봉: ", int(tax(yearly_payment)), "만원")
