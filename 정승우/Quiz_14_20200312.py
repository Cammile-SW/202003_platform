N = input("문자를 입력하세요 : ")

M = N.upper()
L = N.lower()

if M == L:
    print("입력 형식이 잘못되었습니다")
else:
    if N == M:
        print("변환 결과 : ",L)
    elif N == L:
        print("변환 결과 : ",M)
