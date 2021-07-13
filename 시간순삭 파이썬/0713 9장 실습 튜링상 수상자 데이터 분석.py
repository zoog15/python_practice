awards = []
awards.append({'이름':'팀 버너스리','수상년도':2016,'국적':'영국',
               '대표업적':'월드 와이드 웹의 하이퍼텍스트 시스템을 고안하여 개발'})
awards.append({'이름':'리처드 해밍','수상년도':1968,'국적':'미국',
               '대표업적':'오류 검출 부호 및 오류 정정 부호'})
awards.append({'이름':'에츠허르 데이크스트라','수상년도':1972,'국적':'네덜란드',
               '대표업적':'프로그래밍 언어 연구, 데이크스트라 알고리즘'})
awards.append({'이름':'더글러스 엥겔바트','수상년도':1977,'국적':'미국',
               '대표업적':'마우스의 발명,대화형 컴퓨팅'})
awards.append({'이름':'데니스 리치','수상년도':1983,'국적':'미국',
               '대표업적':'유닉스 운영체제 개발,C언어 개발'})


for award in awards :
    print(award)

print("==수상자 명단==")
for award in awards :
    print(award['이름'])

print()
print("==수상자 명단과 수상년도==")
for award in awards :
    if award['수상년도'] <= 1990:
        print(award['이름'],award['수상년도'])

print()
print("==수상자 국가==")
nationality = set()
for award in awards :
    nationality.add(award['국적'])

print(nationality)
