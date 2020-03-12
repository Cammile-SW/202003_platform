N = input("주민등록번호를 입력하세요.(-제외) : ")


T = int(N[6:7])

if T == 1 or 3:
    print("당신은 남자입니다.")
elif T == 2 or 4:
    print("당신은 여자입니다.")
