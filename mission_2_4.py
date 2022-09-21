# 버스 요금 계산기

def bus_fare(pay_type, age):
    if pay_type == "카드":
        if age < 8:
            return "무료"
        elif age >= 8 and age < 14:
            return "450원"
        elif age >= 14 and age < 20:
            return "720원"
        elif age >= 20:
            return "450원"
        elif age >= 75:
            return "무료"
    elif pay_type == "현금":
        if age < 8:
            return "무료"
        elif age >= 8 and age < 14:
            return "450원"
        elif age >= 14 and age < 20:
            return "1000원"
        elif age >= 20:
            return "1300원"
        elif age >= 75:
            return "무료"

print("[본인의 나이와 지불 유형을 입력하세요]")
age = int(input("나이: "))
pay_type = input("지불유형: ")

print("\n[버스 요금 계산기]")
print("나이: ", age, "세")
print("지불유형: ", pay_type)
print("버스요금: ", bus_fare(pay_type, age))
