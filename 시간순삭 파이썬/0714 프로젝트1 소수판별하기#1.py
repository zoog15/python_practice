import time
start = time.time()

n = int(input("n값을 입력하세요: "))

count = 1
b=(n+1)//2 # 입력된 수의 중간수를 확인

for a in range(2,b+1) : # 2~n까지 나머지없이 나누어떨어지는 a가 있는지 확인
    if n%2 == 0 :
        count += 3
        break
    elif n%a == 0 :
        count+=1

if(count == 1) : 
    print("소수입니다.")
else :
    print("소수가 아닙니다.")

print("time :",time.time() - start) # 코드가 실행되는 시간을 현재 컴퓨터 시간이용해 측
