data = [6,7,7,8,8,10,9,3,5,2,7,2,6]
data.sort() #정렬시키기
print(data)

n = len(data)
print("원소 개수:",n)

middle = n//2

if n % 2 == 1 :
    print("중앙값은:",data[middle])
else :
    print("중앙값은:"(data[middle-1]+data[middle])/2)
