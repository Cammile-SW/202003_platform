N = input("정수 N을 입력하세요.(1~9) : ")

for i in range(9):
    print("{} X {} = {}".format(N,i+1,int(N)*(i+1)))
