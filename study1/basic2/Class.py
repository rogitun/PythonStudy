class FourCal:

    def __init__(self):
        self.result = 0
        self.first = 0
        self.second = 0

    def setData(self,f,s):
        self.first = f
        self.second = s

    def add(self):
        return self.first + self.second





cal = FourCal()

cal.setData(2,3)

print(cal.add())

input_base = input()

res22 = map(int, input_base.split())

print(res22[0])

