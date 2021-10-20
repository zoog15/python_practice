# https://programmers.co.kr/learn/courses/30/lessons/42891
def solution(food_times, k):
    count = 0  # 현재 몇번쨰 인덱스를 가리키는지 확인용
    if sum(food_times) == k:
        return -1

    for i in range(k):
        if count == len(food_times):
            count = 0
        if i != k-1 and food_times[count] == 0:
            count += 1
        food_times[count] -= 1  # 한입 먹음
        count += 1  # 다음 음식으로 진행

        print(food_times, count, i)

    print(food_times, count)
    return count+1


food_times = [1,3,5,1,1]
k = 10

result = solution(food_times, k)

print(result)