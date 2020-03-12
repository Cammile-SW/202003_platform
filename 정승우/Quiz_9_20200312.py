N = int(input("점수를 입력하세요.(0~100) : "))
if N > 100 or N <=0:
    N=int(input("점수를 다시 입력하세요.(0~100) : "))

if N > 80 and N <=100:
    print("A학점 입니다.")
elif N > 60 and N <=80:
    print("B학점 입니다.")
elif N > 40 and N <=60:
    print("C학점 입니다.")
elif N > 20 and N <=40:
    print("D학점 입니다.")
else:
    print("F학점 입니다.")
