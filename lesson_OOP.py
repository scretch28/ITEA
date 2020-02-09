"""
* Создайте класс, описывающий автомобиль.
* Создайте класс, описывающий салон автомобилей в котором имеется:
  * Атрибут «перечень автомобилей»
  * Атрибут «выручка»
  * Метод «продажа автомобиля»
  * Метод «услуга покраски автомобиля»
"""


class Car:

    # def __init__(self, price=0.0, color='black', model_name='Ford', vin=''):
    def __init__(self, model_name='Ford', price=0.0, color='black', vin=''):
        self.price = price
        self.color = color
        self.model_name = model_name
        self.vin = vin
        # внутренний учёт уникального идентификатора автомобиля
        global reg_id
        reg_id += 1
        self.id = reg_id

    def __str__(self):
        # return f"{self.__class__.__name__} {self.price} {self.color}"  # не работает как мы хотим
        return f"{self.id}: {self.model_name}(vin1={self.vin}) {self.__class__.__name__} {self.price} {self.color}"


reg_id = 0


car1 = Car()
#print(car1)
car1.price = 10
car1.color = 'white'

car2 = Car(model_name='Mazda', price=11, color='cyan')

car3 = Car('Toyota', 10, 'white', vin=hex(121243).upper()[2:])

print(car1, car2, car3, sep='\n')
# print('-'*60)
# print('car1', car1.price, car1.color)
# print('car2', car2.price, car2.color)
# print('car3', car3.price, car3.color)

print('=' * 60)


class AutoSalon:
    def __init__(self, name):
        self.name = name
        self.cars = []  # Перечень автомобилей в салоне
        self.profit = 0.0

    def __str__(self):
        result = []
        for car in self.cars:
            result.append(str(car))
        report_of_cars = '\n'.join(result)
        return '\n' + '='*60 + f"\n{self.name} (касса={self.profit}):\n{report_of_cars}\n" + '='*60 + '\n'

    def append(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Ожидается тип `Car`, а получен {type(car)}')
        self.cars.append(car)

    def search(self, id):
        """
            Найти автомобиль на складе

        :param id: id авто
        :return: экземпляр Car
        """
        for car in self.cars:
            if car.id == id:
                return car
        # raise IndexError

    def sale(self, car_id):
        car = self.search(car_id)
        if not car:
            raise IndexError(f'Автомобиль с индексом {car_id} не найден!')
        self.cars.remove(car)  # car = self.cars.pop(car)
        self.profit += car.price
        return car

    def paint(self, car, color):
        car.color = color
        return 0.5


salon1 = AutoSalon('АВТ Бавария')
salon1.append(car1)
salon1.append(car3)
print(salon1)

try:
    print(f"\nПродан автомобиль {str(salon1.sale(10))}\n")
except IndexError as e:
    print(str(e))
else:
    print(salon1)


print(f"Продан автомобиль {str(salon1.sale(1))}")
print(salon1)

salon1.profit += salon1.paint(car2, 'black')
print(car2)
print(salon1)

car = salon1.search(3)
salon1.paint(car, 'green')
print(salon1)


# salon2 = AutoSalon('Соломенский авторынок')
# salon2.append(car2)
# print(salon2)





