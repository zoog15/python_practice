alist = []
sum=0

for i in range(5) :
    num = int(input("정수를 입력하시오. :"))
    sum += num
    alist.append(num)

length = len(alist) # 리스트의 길이 저장

avg  = float(sum/length)

print("평균 = ",avg)
