# Special Method (Magic method)
# 시퀀스, 반복, 함수, 클래스
# 클래스 안에 정의할 수 있는 특별한(Built in) 메서드, 더블 언더스코어 (__xxx__)
import math

# 기본형

print(int)  # Data 타입은 class

print(dir(int))

n = 10
print(n + 100)
print(n.__add__(100))

# print(n.__doc__)
print(n.__bool__())

print(n * 100, n.__mul__(100))


# 클래스 예제 1

class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit class Info : {} , {} '.format(self._name, self._price)

    def __add__(self, x):
        print('called __add__')
        return self._price + x._price

    def __sub__(self, other):
        return abs(self._price - other._price)

    def __ge__(self, other):
        if self._price >= other._price:
            return True
        else:
            return False


s1 = Fruit('ORagne', 7500)
s2 = Fruit('Apple', 8400)

print(s1.__add__(s2))  # == __add__ => +
print(s1 + s2)

print(s1 - s2)

print(s1 >= s2)
