
'''
Розробити проект "Адресна книга"
Реквізити контакту:
 1. Прізвище - обов*язково
 2. Ім*я - обов*язково
 3. По батькові - обов*язково
 4. Поштова адреса
 5.Перелік e-mail, в якому 1-й - основний
 6. Перелік телефонів
 7. Перелік месенджерів: пара значень - назва (із зумовленого списка) та аккаунт
 
 Функціональність:
     1. Меню дій користувача:
         a. створити контакт
         b. вивести список контактів на екран у вигляді красивої таблиці
         c. змінити контакт
         d. видалити контакт
         e. збереження списку контактів на диск
         f. пошук контакту за пізстрокою:
             і. за прізвищем
             іі. за іменем
             ііі. за всіма реквізитами
             
    2. Прочитати перелік контактів з диску  (якщо є файл) при запуску програми
    3. Під час виходу запитувати про необхідність збереження переліку контактів у файл на диск
    4. Вивести перелік контактів у текстовий файл(звіт за усіма реквізитами)
'''    
 
class Contact:

    # def __init__(self, price=0.0, color='black', model_name='Ford', vin=''):
    def __init__(self, surname, name, midle_name):
        self.surname = surname
        self.name= name
        self.midle_name = midle_name
        self.address = ''
        self.e_mail=list()
        self.phones=list()
        self.messengers=dict()
        global reg_id
        reg_id += 1
        self.id = reg_id
    
    def __str__(self):
        return self.name        
            
        

class Address_book:
    def __init__(self):
        self.contacts=dict()
        
    def create_contact(self):
        name=input('Enter the name: ')
        surname= input('Enter the surname: ')
        midle_name=input('Enter the midle_name: ')
        address=input('Enter the address: ')
        e_mail=input('Enter the e_mail: ')
        phone_number=input('Enter the phone namber: ')
        messenger=input('Enter the messenger: ')
        account=input('Enter the account: ')
        
        contact=Contact(surname, name, midle_name)
        contact.address=address
        contact.e_mail.append(e_mail)
        contact.phones.append(phone_number)
        contact.messengers[messenger]=account
        
        self.contacts[contact.id]=contact
        
        return contact
 


reg_id=0

address_book=Address_book()
c=address_book.create_contact()

print(c)
print(address_book.contacts[1])
    
    
    
    
    
    
    print
    
    
    
    
    

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





