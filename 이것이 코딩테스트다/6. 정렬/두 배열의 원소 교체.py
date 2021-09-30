N, K = map(int, input().split())  # N : 각배열 원소의 개수, K : 최대 바꿔치기 횟수

# A, B 배열 리스트 입력받기
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sort_A = sorted(A)  # 오름차순 정렬
sort_B = sorted(B, reverse=True)  # 내림차순 정렬

for i in range(K):
    # A의 제일 작은 원소가 B의 가장 큰원소보다 크다면 바꿀 이유가 없음
    if sort_A[i] < sort_B[i]:
        sort_A[i], sort_B[i] = sort_B[i], sort_A[i]
    else:
        break

print(sum(sort_A))
