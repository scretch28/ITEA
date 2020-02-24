

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


import pickle 
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
        self.id = 0
    
    def __str__(self):
#        result='\n'+'name: ' % name, 'surname: ' % surname, 
        result=f"id={self.id} {self.name} {self.surname} {self.midle_name}:\n\tадреса: {self.address} \n\te_mail: {str.join(', ', self.e_mail)} \n\tтелефони: {str.join(', ', self.phones)} \n\tmessengers: {self.messengers}"
        return result        
            
        

class Address_book:
    def __init__(self):
        self.contacts=dict()
#        self.contacts=list()
        self.reg_id=0
    
    
    
    
        
    def create_contact(self):
        name=input('Enter the name: ')
        while name=='':
            name=input('Enter the name: ')
    
        
        surname= input('Enter the surname: ')
        while surname=='':
            surname= input('Enter the surname: ')
        
        midle_name=input('Enter the midle_name: ')
        while name=='':   
            midle_name=input('Enter the midle_name: ')
            
        contact=Contact(surname, name, midle_name)
        
        address=input('Enter the address: ')
        contact.address=address 
        
        e_mail=input('Enter the e_mail: ')
        while e_mail!='':
            contact.e_mail.append(e_mail)
            e_mail=input('Enter the e_mail or empty str: ')
         
        phone_number=input('Enter the phone namber: ')
        while phone_number!='':
            contact.phones.append(phone_number)
            phone_number=input('Enter the phone number or empty str: ')
        
        messenger=input('Enter the messenger: ')
        while messenger!='':
            account=input('Enter the account: ')
            contact.messengers[messenger]=account     
            messenger=input('Enter the messenger number or empty str: ')
        
        
             
        
#        self.contacts[contact.id]=contact
        
        return contact
    
    def append_contact(self, contact):
        if not isinstance(contact, Contact):
            raise TypeError(f'Ожидается тип `Contact`, а получен {type(contact)}')
#        self.contacts.append(contact)
#        global reg_id
        
        self.reg_id += 1
        contact.id=self.reg_id
        self.contacts[contact.id]=contact
        
        
        
    def __str__(self):
          l_max_name=len(max(self.contacts.values(),key=lambda x:len(x.name)).name)
          l_max_surname=len(max(self.contacts.values(),key=lambda x:len(x.surname)).surname)
          l_max_midle_name=len(max(self.contacts.values(),key=lambda x:len(x.midle_name)).midle_name)
          l_max_phone=15
          l_max_e_mail=20
          
                  
          
          
          result=''
          
          for c in self.contacts.values():
    
              l_name=l_max_name -len(c.name)
              l_surname=l_max_surname -len(c.surname)
              l_midle_name=l_max_midle_name -len(c.midle_name)
              l_phone=l_max_phone
              phone=''
              if len(c.phones)>0:
                  phone=c.phones[0]
                  l_phone=l_max_phone-len(phone)
              e_mail=''
              if len(c.e_mail)>0:
                  e_mail=c.e_mail[0]
                  l_e_mail=l_max_e_mail-len(e_mail)
              
           
                  
                  
              
              result+='| %s | %s %s | %s %s | %s %s | %s %s | %s %s |\n'%(c.id, c.name, ' '*l_name, c.surname, ' '*l_surname, c.midle_name, ' '*l_midle_name, phone, ' '*l_phone, e_mail, ' '*l_e_mail)
        
          return result
      
    def update_contact (self, id):
          contact=self.contacts[id]
          print('Дані контакту будуть змінені')
          
          value=contact.name
          print('Поточні данні контакту: name %s ' % value )
          value=input('У разі необхідності введіть нове значення name, або підтвердіть їх правельність - натисніть \'Enter\': ')
          if value!="":
              contact.name=value
          

          value=contact.surname
          print('Поточні данні контакту: surname %s ' %  value )
          value=input('У разі необхідності введіть нове значення surname, або підтвердіть їх правельність - натисніть \'Enter\': ')
          if value!="":
              contact.surname=value
              
              
          value=contact.midle_name
          print('Поточні данні контакту: midle_name %s ' %  value )
          value=input('У разі необхідності введіть нове значення midle_name, або підтвердіть їх правельність - натисніть \'Enter\': ')
          if value!="":
              contact.midle_name=value


          value=contact.address
          print('Поточні данні контакту: address %s ' %  value )
          value=input('У разі необхідності введіть нове значення address, або підтвердіть їх правельність - натисніть \'Enter\': ')
          if value!="":
              contact.address=value  
              
          value=str.join(', ', contact.e_mail)
          print('Поточні данні контакту: e_mail %s ' %  value )
          value=input('У разі необхідності введіть нове значення e_mail, або підтвердіть їх правельність - натисніть \'Enter\': ')
          if value !='':
              contact.e_mail.clear()
              while value!='':
                contact.e_mail.append(value)
                value=input('Enter the e_mail or empty str: ')
         
         
          value=str.join(', ', contact.phones)
          print('Поточні данні контакту: phone_number %s ' %  value )
          value=input('У разі необхідності введіть нове значення phone_number, або підтвердіть їх правельність - натисніть \'Enter\': ')
          if value !='':
              contact.phones.clear()
              while value!='':
                contact.phones.append(value)
                value=input('Enter the phone_number or empty str: ')        
            
            
          print('Поточні данні контакту: messenger %s ' % contact.messengers ) 
          messenger=input('Enter the messenger: ')
          while messenger!='':
               account=input('Enter the account: ')
               contact.messengers[messenger]=account     
               messenger=input('Enter the messenger number or empty str: ')


    def del_contact(self, id):
        contact=self.contacts[id]
        print('Дані контакту будуть видалені: ', contact)
        del self.contacts[id]
       
    def save_to_file(self, file_name="adress_book"):
       
        filehandler = open(file_name, 'bw') 
        pickle.dump(self, filehandler)
        
        
    def load_from_file (self, file_name="adress_book"):
        filehandler = open(file_name, 'br') 
        saved_book = pickle.load(filehandler)
        self.reg_id=saved_book.reg_id
        self.contacts=saved_book.contacts
        
    def get_contact_by_id (self, id):
        return self.contacts[id]
    
    def report_to_file (self):
         filehandler = open('report.txt', 'a') 
         for c in self.contacts.values():
             print(c, file=filehandler)
         filehandler.close()

    def search_by_name (self, name):
        result_search=list(filter(lambda x: name in x.name, self.contacts.values()))
        return result_search


#reg_id=0





#address_book=Address_book()
#c1=address_book.create_contact()
##c2=address_book.create_contact()
#c3=address_book.create_contact()
#
#address_book.append_contact(c1)
#address_book.append_contact(c2)
#address_book.append_contact(c3)
##print(c)
#print(address_book)
#address_book.save_to_file()

#address_book=Address_book()
#address_book.load_from_file()
#print(address_book)
#
##address_book.del_contact(2)
##print(address_book)
#
#z=address_book.search_by_name('bkv')
#print(z)
#print (c1)
address_book=Address_book()
comand=''
while comand!='e':
    print("Hello, can I help you? - yours Address book :Р)")
    print("Whould you choose your action?")
    print("Press \"l\" to load  contacts from file")
    print("Press \"t\" to show  contacts table")
    print("Press \"c\" to create new contact")
    print("Press \"u\" to update  contact")
    print("Press \"d\" to delete contact")
    print("Press \"v\" to view  contact info")
    print("Press \"r\" to create text report")
    print("Press \"f\" to find a contact")
    print("Press \"s\" to save contacts to file")
    print("Press \"e\" to exit")
    command=input('Make your choise: ')
    
  
    
    if command=='l':
        address_book.load_from_file()
    elif command=='t':
        print(address_book)
    elif command=='c':
        c=address_book.create_contact()
        address_book.append_contact(c)
    elif command=='u':
        contact_id=''
        while not contact_id.isdigit():
            contact_id=input("Enter contact id or \"0\" for return  to previous menu: " )
        contact_id=int(contact_id)
        if contact_id != 0:
            try:
                address_book.update_contact(contact_id)
            except KeyError:
                print ('Contact with this id didn\'t find')
    elif command=='d':
        contact_id=''
        while not contact_id.isdigit():
            contact_id=input("Enter contact id or \"0\" for return  to previous menu: " )
        contact_id=int(contact_id)
        if contact_id != 0:
            try:
                address_book.del_contact(contact_id)
            except KeyError:
                print ('Contact with this id didn\'t find')
    elif command=='v':
        contact_id=''
        while not contact_id.isdigit():
            contact_id=input("Enter contact id or \"0\" for return  to previous menu: " )
        contact_id=int(contact_id)
        if contact_id != 0:
            try:
                c=address_book.get_contact_by_id(contact_id)
                print(c)                
            except KeyError:
                print ('Contact with this id didn\'t find')
    elif command=='f':
        f=input('enter the name: ')
        if f != '':
            search_res=address_book.search_by_name(f)
            for sr in search_res:
                print (sr)
                
    elif command=='s':
        address_book.save_to_file()
        
    elif command=='r':
        address_book.report_to_file()
        
    elif command=='e':
        break
        
    
            
        
        
    









#address_book.update_contact()
#address_book.update_contact(2)

    
    

#a={1:'A', 2:'B', 3:'C'}

#a.update({2:'T'}) 
#print(a) 
#c=a.get(10)
#print (c)
#b=a[10]
#print(b)
###    
#    
#    print
#    
#    
#    
#    
#    
#
#    def __str__(self):
#        # return f"{self.__class__.__name__} {self.price} {self.color}"  # не работает как мы хотим
#        return f"{self.id}: {self.model_name}(vin1={self.vin}) {self.__class__.__name__} {self.price} {self.color}"
#
#
#reg_id = 0
#
#
#car1 = Car()
##print(car1)
#car1.price = 10
#car1.color = 'white'
#
#car2 = Car(model_name='Mazda', price=11, color='cyan')
#
#car3 = Car('Toyota', 10, 'white', vin=hex(121243).upper()[2:])
#
#print(car1, car2, car3, sep='\n')
## print('-'*60)
## print('car1', car1.price, car1.color)
## print('car2', car2.price, car2.color)
## print('car3', car3.price, car3.color)
#
#print('=' * 60)
#
#
#class AutoSalon:
#    def __init__(self, name):
#        self.name = name
#        self.cars = []  # Перечень автомобилей в салоне
#        self.profit = 0.0
#
#    def __str__(self):
#        result = []
#        for car in self.cars:
#            result.append(str(car))
#        report_of_cars = '\n'.join(result)
#        return '\n' + '='*60 + f"\n{self.name} (касса={self.profit}):\n{report_of_cars}\n" + '='*60 + '\n'
#
#    def append(self, car):
#        if not isinstance(car, Car):
#            raise TypeError(f'Ожидается тип `Car`, а получен {type(car)}')
#        self.cars.append(car)
#
#    def search(self, id):
#        """
#            Найти автомобиль на складе
#
#        :param id: id авто
#        :return: экземпляр Car
#        """
#        for car in self.cars:
#            if car.id == id:
#                return car
#        # raise IndexError
#
#    def sale(self, car_id):
#        car = self.search(car_id)
#        if not car:
#            raise IndexError(f'Автомобиль с индексом {car_id} не найден!')
#        self.cars.remove(car)  # car = self.cars.pop(car)
#        self.profit += car.price
#        return car
#
#    def paint(self, car, color):
#        car.color = color
#        return 0.5
#
#
#salon1 = AutoSalon('АВТ Бавария')
#salon1.append(car1)
#salon1.append(car3)
#print(salon1)
#
#try:
#    print(f"\nПродан автомобиль {str(salon1.sale(10))}\n")
#except IndexError as e:
#    print(str(e))
#else:
#    print(salon1)
#
#
#print(f"Продан автомобиль {str(salon1.sale(1))}")
#print(salon1)
#
#salon1.profit += salon1.paint(car2, 'black')
#print(car2)
#print(salon1)
#
#car = salon1.search(3)
#salon1.paint(car, 'green')
#print(salon1)
#
#
## salon2 = AutoSalon('Соломенский авторынок')
## salon2.append(car2)
## print(salon2)
#
#



