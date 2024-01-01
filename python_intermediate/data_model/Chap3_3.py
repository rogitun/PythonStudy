# Special Method (Magic method)
# 시퀀스, 반복, 함수, 클래스
# 클래스 안에 정의할 수 있는 특별한(Built in) 메서드, 더블 언더스코어 (__xxx__)
from math import sqrt

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플
from collections import namedtuple

Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)  # Point(x=1.0, y=5.0), 레이블링이 이미 되어있음.
print(pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
print(l_leng2)

# 네임드 튜플 선언

Point1 = namedtuple('Point', ['x', 'y'])  # == namedtuple('Point', 'x y')
Point2 = namedtuple('Point', 'x, y')  # 따옴표로 구분해도 된다.

temp = [12, 34]
pt5 = Point1._make(temp)
print(pt5)

numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

print(numbers)
print(ranks)

Classes = namedtuple('Classes', ['rank', 'numbers'])
stds = [Classes(rank, number)
        for rank in ranks
        for number in numbers]

print(stds)

