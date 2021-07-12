PI = 3.14

def circleArea(radius) :
    print("반지름이 5인 원의 면적 : ",float(PI*radius**2))
def circleCircumference(radius) :
    print("반지름이 5인 원의 둘레 : ",float(2*PI*radius))


radius = int(input("원의 반지름의 길이는?"))
circleArea(radius)
circleCircumference(radius)
