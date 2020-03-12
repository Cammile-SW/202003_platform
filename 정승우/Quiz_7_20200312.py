sum = 0

for i in range(100):
    sum = sum + (i+1)
    if sum > 100:
        ans = i+1
        print("답 : ",ans)
        break
