# Special Method (Magic method)
# 시퀀스, 반복, 함수, 클래스
# 클래스 안에 정의할 수 있는 특별한(Built in) 메서드, 더블 언더스코어 (__xxx__)

class Vector(object):
    def __init__(self, *args):
        if len(args) == 0:
            self._x, self._y = 0, 0
        self._x, self._y = args

    def __repr__(self):
        '''
        return the vector informations
        '''
        return 'Vector(%r,%r)' % (self._x, self._y)

    def __add__(self, other):
        '''
        Return the vector add
        '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):  # (x,y) * y
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return (bool(max(self._x, self._y))
                or bool(min(self._x, self._y)))


vector = Vector(5, 7)
vector1 = Vector(0, 0)
vector2 = Vector(-2, 5)
vector3 = Vector(-2, -6)
vector4 = Vector(3, 0)

print(bool(vector))
print(bool(vector1))
print(bool(vector2))
print(bool(vector3))
print(bool(vector4))

print(vector * 3)
