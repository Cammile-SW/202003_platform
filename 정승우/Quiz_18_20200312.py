file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
file2 = []

for A in file:
    j = A.find('.')
    A = A[:j]
    file2.append(A)

file = file2

print(file)
