import random
n = random.randint(1,100) # 1에서 100사이 랜덤숫자

print("1부터 100 사이의 숫자를 맞추시오.")

a=0
count = 0

while a != n :
    a = int(input("숫자를 입력하시오"))
    count = count + 1
    if a < n :
        print("낮음")
    elif a > n :
        print("높음")

print("축하합니다. 시도횟수 =",count)
