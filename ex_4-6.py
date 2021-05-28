class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class Printer(OfficeEquipment):
    def __init__(self, name, type_p):
        super().__init__(name)
        self.type_p = type_p


class Scanner(OfficeEquipment):
    def __init__(self, name, type_s):
        super().__init__(name)
        self.type_s = type_s


class CopyMachine(OfficeEquipment):
    def __init__(self, name, type_c):
        super().__init__(name)
        self.type_c = type_c


class Storage:

    def acceptance(self):
        print(f"Объект {obj.name} принят на склад")

    def moving(self):
        print(f"Объект {obj.name} перемещен")

list_obj = []
x = "1"
while x == "1" or x == "2":
    menu_1 = input("Принять оборудвание - нажмите 1 \nПереместить оборудование - нажмите 2 \nВыход - любая клавиша\n")
    if menu_1 == '1':
        print("Создаем объект учета")
        menu_class = input("Тип оборудования:\nПринтер - нажмите 'p' \nСканер - нажмите 's' \nКопир  - нажмите 'c' \n")
        if menu_class == 'p':
            name = input("Введите полное наименование устройства: \n")
            type_p = input("Тип принтера:\nСтруйный- нажмите 1 \nЛазерный - нажмите 2 \n")
            obj = Printer(name, type_p)
            print(f"Создан объект {id(obj)}; Наименование: {obj.name}, Тип {obj.type_p}")
            obj_dict = dict(id=id(obj), Наименование=obj.name, тип=obj.type_p)
        elif menu_class == 's':
            name = input("Введите полное наименование устройства: \n")
            type_s = input("Тип сканера:\nА3- нажмите 1 \nА4 - нажмите 2 \n")
            obj = Scanner(name, type_s)
            print(f"Создан объект {id(obj)}; Наименование: {obj.name}, Тип {obj.type_s}")
            obj_dict = dict(id=id(obj), Наименование=obj.name, тип=obj.type_s)
        elif menu_class == 'c':
            name = input("Введите полное наименование устройства: \n")
            type_c = input("Тип сканера:\nЦветной- нажмите 1 \nЧерно-белый - нажмите 2 \n")
            obj = CopyMachine(name, type_c)
            print(f"Создан объект {id(obj)}; Наименование: {obj.name}, Тип {obj.type_c}")
            obj_dict = dict(id=id(obj), Наименование=obj.name, тип=obj.type_c)
        else:
            obj = None
        obj = Storage()
        print(obj)
#        Storage.acceptance(obj.name)
    elif menu_1 == '2':
        Storage.moving(obj.name)
    else:
        print("Конец")
        break


#print(obj_dict)