#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:04:10 2020

@author: nia
"""

#import string as string_lib
#string = 'абракадабра'
#print(repr(string_lib.punctuation))

#import lesson_OOP
#
#car1 = lesson_OOP.Car()
##print(car1)
#car1.price = 10
#car1.color = 'white'
#
#car2 = Car(model_name='Mazda', price=11, color='cyan')
#
#car3 = Car('Toyota', 10, 'white', vin=hex(121243).upper()[2:])
#
#print(car1, car2, car3, sep='\n')
#
#print('=' * 60)
#import lesson_OOP
#
from lesson_OOP import {
        Car, Autosalon as AvtoSalon,
        }


car1 = Car()
#print(car1)
car1.price = 10
car1.color = 'white'

car2 = Car(model_name='Mazda', price=11, color='cyan')

car3 = Car('Toyota', 10, 'white', vin=hex(121243).upper()[2:])

print(car1, car2, car3, sep='\n')

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


#Інаструкція програмування!!!імпорт
#c1=oop_cars.Car(
#        type.oop(car)
        
        
import oop_cars
#нужно перезапустить

#__main__скрипт 


l=list('hjfjgfd')
print(l)
list=34
del list
l=list('hgkdf')
print(l)
