def r1.show():
    print(f"좌측 상단 꼭지점이 {Rectangle[1]}, {Rectangle[2]}이고 우측 하단 꼭지점이 {Rectangle[3]}, {Rectangle[4]}인 사각형입니다.")

def r1.getArea():
    Area = (Rectangle[3] - Rectangle[1]) * (Rectangle[4] - Rectangle[2])
    return Area

def r1.getPerimeter():
    Perimeter = 2 * (Rectangle[3] - Rectangle[1] + Rectangle[4] - Rectangle[2])
    return Perimeter

Rectangle = []
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
