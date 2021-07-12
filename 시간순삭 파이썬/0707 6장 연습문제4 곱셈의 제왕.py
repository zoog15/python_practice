import random

a = random.randint(1,10)
b = random.randint(1,10)

answer= 0

while answer != a*b :
    print(a,"*",b,"=")
    answer = int(input())

print("맞았습니다.")
