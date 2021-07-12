temp_list = [0,10,20,30] # 기온 리스트
vapor_list = [4.8,9.4,17.3,30.4] # 포화수증기량 리스트

vapor = float(input("현재 수증기량 입력 :"))
temp = int(input("현재 온도 입력 : ")) # 기온을 입력

if temp in temp_list : # 입력받은 기온이 temp_list에 있다면
    index = temp_list.index(temp) # temp_list에서 temp의 index번호 저장
    print(index)
    print(vapor_list[index]) # 그 인덱스에 해당하는 포화수증기량 출력

humidity = vapor / vapor_list[index] * 100

print("현재 습도는 ",humidity,"% 입니다.")
print("프로그램을 종료합니다.")
