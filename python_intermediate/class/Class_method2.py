class Car:
    """
    Class Car

    """

    type = "car"  # 클래스 변수 -> 모든 인스턴스가 공유함, 언더바를 붙이지 않은 변수는 '클래스 변수'로서 명시
    count = 0

    def __init__(self, company, detail):  # Self가 첫번째 파라미터로 오는 것은 인스턴스 메서드, 각자 고유의 value를 가지기 때문
        self._company = company
        self._details = detail
        Car.count += 1

    def __del__(self):
        Car.count -= 1

    def __str__(self):  # 사용자 레벨에서 확인하기 위함
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 개발자 레벨에서 확인하기 위함
        return 'details : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))


car1 = Car("Kia", {'color': 'red', 'price': 2000})
car2 = Car("Hyundai", {'color': 'black', 'price': 3000})
car3 = Car("Audi", {'color': 'blue', 'price': 6000})

print(id(car1))
car1.detail_info()
print(id(car2))
print(id(car3))

print(car1.__doc__)

# Car.detail_info() 불가. 인스턴스 메서드를 호출하기 때문에 인스턴스에서 호출하거나 파라미터로 인스턴스를 넘겨야함

print('car Count = {} '.format(Car.count))  # 3
del car2
print('car Count = {} '.format(Car.count))  # 2
