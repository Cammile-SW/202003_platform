N = int(input("숫자를 입력하세요 : "))

for i in range(N):
    print(" "*(N-i-1),"★"*(i+1)," "*(N-i-1))
for i in range(N-1):
    print(" "*(i+1),"★"*(N-i-1)," "*(i+1))
