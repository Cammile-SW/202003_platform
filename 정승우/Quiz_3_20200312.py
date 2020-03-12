import random

c = input("주사위를 던지시겠습니까?")

a = random.randint(1,6)
b = random.randint(1,6)

if a > b:
    print("A : %d , B : %d , A의 승리입니다." %(a,b))
elif b > a:
    print("A : %d , B : %d , B의 승리입니다." %(a,b))
else:
    print("A : %d , B : %d , 무승부입니다." %(a,b))
