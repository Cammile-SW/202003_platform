a = int(input("첫 번째 숫자를 입력하세요. : "))
b = int(input("두 번째 숫자를 입력하세요. : "))
c = input("연산 기호를 입력하세요.(+,-,*,/) : ")

if c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "*":
    result = a * b
elif c == "/":
    result = a / b
else:
    c = input("연산 기호를 다시 입력하세요.(+,-,*,/)")

print("계산 결과는 {} 입니다.".format(result))