def exchange(m,c) :
    if c in country_list :
        m_code = country_list.index(c)
    else :
        print("해당 국가 정보가 없습니다.")
        return
    result = round(m/rate[m_code],2)
    print(m,"원은",result,unit[m_code],"입니다.")

country_list = ['미국','중국','유럽','일본']
unit = ['달러','위안','유로','엔']
rate = [1182.5,169.22,1286.74,1078.14]
money1 = int(input("환전 금액(원)을 입력하세요:"))
country = input("국가를 입력하세요 :")
exchange(money1,country)

