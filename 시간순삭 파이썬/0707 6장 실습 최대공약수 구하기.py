n = int(input("정수 1 입력:"))
m = int(input("정수 2 입력:"))

if n< m:
    n,m = m,n

while m>0 :
    r = n%m # 나머지
    n,m = m,r

if n!= 1 :
    print("두 수의 최대공약수 :",n)
else :
    print("두 수는 서로소이다.")
