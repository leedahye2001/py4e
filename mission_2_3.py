# 학점 변환기

def grader(name, score):
    if score>=95 or score==100:
        return "A+"
    elif score>=90 and score<=94:
        return "A"
    elif score>=85 and score<=89:
        return "B+"
    elif score>=80 and score<=84:
        return "B"
    elif score>=75 and score<=79:
        return "C+"
    elif score>=70 and score<=74:
        return "C"
    elif score>=65 and score<=69:
        return "D+"
    elif score>=60 and score<=64:
        return "D"
    else:
        return "F"

print("[학생 이름과 점수를 입력하세요]")
name = input("학생 이름: ")
score = int(input("점수: "))

print("\n[학점 변환기]")
print("학생이름: ", name)
print("점수: ", score, "점")
print("학점: ", grader(name, score))
