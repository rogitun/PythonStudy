class Car:
    """
    Class Car
    Description : Class, Static, Instance method
    """

    type = "car"  # 클래스 변수 -> 모든 인스턴스가 공유함, 언더바를 붙이지 않은 변수는 '클래스 변수'로서 명시
    price_per_raise = 1.0

    def __init__(self, company, detail):  # Self가 첫번째 파라미터로 오는 것은 인스턴스 메서드, 각자 고유의 value를 가지기 때문
        self._company = company
        self._details = detail

    def __str__(self):  # 사용자 레벨에서 확인하기 위함
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 개발자 레벨에서 확인하기 위함
        return 'details : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))

    # instance method
    # Self : 객체의 고유한 속성 값을 사용.

    def get_price(self):
        return 'Car {} price {} -> {}'.format(self._company, self._details.get('price'),
                                              self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):  # cls는 클래스를 의미한다.
        cls.price_per_raise = per

    # static method
    @staticmethod
    def is_kia(inst):
        if inst._company == 'Kia':
            return 'True'
        else:
            return 'belongs to {}'.format(inst._company)


car1 = Car("Kia", {'color': 'red', 'price': 2000})
car2 = Car("Hyundai", {'color': 'black', 'price': 3000})
car3 = Car("Audi", {'color': 'blue', 'price': 6000})

# 가격 정보
# 가격 인상 이전
print(car1.get_price())

# 가격 정보 인상
# Car.price_per_raise = 1.2 권장하지 않는 방법
Car.raise_price(1.2)  # 클래스 메서드 사용.
print(car1.get_price())

# static method / 인스턴스와 클래스를 통한 호출이 가능하다.
print(car1.is_kia(car1))
print(car1.is_kia(car2))
print(Car.is_kia(car3))
