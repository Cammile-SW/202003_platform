for i in range(1,101):
    j = str(i)
    if j.find('3') != -1 or j.find('6') != -1 or j.find('9') != -1:
        print("짝",end = " ")
    elif i%5 == 0:
        print("아자" ,end = " ")
    else:
        print(i,end = " ")
