def BMI(height,weight) :
    bmi =  weight / (height**2)
    return bmi

def print_result(bmi) :
    if bmi<18.5 :
        print("당신은 저체중입니다.")
    elif bmi<=22.9 :
        print("당신은 정상입니다.")
    elif bmi<=24.9 :
        print("당신은 과체중입니다.")
    elif bmi<=29.9 :
        print("당신은 경도비만입니다.")
    else :
        print("당신은 고도비만입니다.")

height = float(input("키를 m단위로 입력하세요 :"))
weight = int(input("몸무게를 kg단위로 입력하세요: "))

bmi = BMI(height,weight)
print_result(bmi)
