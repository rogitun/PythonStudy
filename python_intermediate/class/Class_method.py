# Dict

car_dicts = [
    {'car_company': 'Ferrai',
     'car_detail': {'color': 'White', 'price': 4000}
     },
    {'car_company': 'Hyundai',
     'car_detail': {'color': 'Black', 'price': 3500}
     },
    {'car_company': 'BMW',
     'car_detail': {'color': 'Blue', 'price': 3700}
     }
]

print(car_dicts[1])  # Hyundai
del car_dicts[1]
print(car_dicts[1])  # BMW


# Class

class Car:

    type = 'Car'
    def __init__(self, company, detail):
        self._company = company
        self._details = detail

    def __str__(self):  # 사용자 레벨에서 확인하기 위함
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):  # 개발자 레벨에서 확인하기 위함
        return 'details : {} - {}'.format(self._company, self._details)


car1 = Car("Kia", {'color': 'red', 'price': 2000})
print(car1)  # __str__이 없으면 인스턴스의 주소 값, str이 있으면 str을 활용하여 프린트함.

car2 = Car("Hyundai", {'color': 'black', 'price': 3000})
car3 = Car("Audi", {'color': 'blue', 'price': 6000})

print(car2)
print(car3)

print(car1.__dict__)  # __dict__로 해당 인스턴스의 멤버 값을 확인할 수 있음, # 클래스 변수는 안나옴
