data = [6,7,7,8,8,10,9,3,5,2,7,2,6]
frequency = {}

for i in data :
    frequency[i] = data.count(i) # count(i)는 리스트 안에 i가 몇 개 있는지 조사해 그 갯수를 반환

max_frequency = 0 # 가장 높은 빈도수를 저장

for i in frequency :
    print(i,'의 횟수: ',frequency[i])
    if(frequency[i] > max_frequency) :
        max_frequency = frequency[i]
        max_frequency_num = i

print('최빈수=',max_frequency_num)
