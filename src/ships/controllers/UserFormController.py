from .CreateModelsController import CreateModelsController
from .SelectShipController import SelectShipController
from ..shemas import *

class UserFormController():

    def __init__(self) -> None:
        self.createController = CreateModelsController()
        self.selectController = SelectShipController()

    def startMenu(self):
        while True:
            print("\nВыберите действие:")
            print("1. Добавить корабль")
            print("2. Добавить систему корабля")
            print("3. Добавить ассоциацию корабля и системы")
            print("4. Добавить оборудование")
            print("5. Добавить уязвимость")
            print("6. Добавить меру защиты")
            print("7. Добавить показатель защищенности")
            print("8. Добавить ассоциацию показателя защищенности и системы")
            print("9. Добавить угрозу")
            print("10. Вывести характеристики корабля")
            print("11. Выйти из программы")

            choice = input("Ваш выбор: ")

            if choice == "1":
                self.shipForm()
            elif choice == "2":
                self.shipSystemForm()
            elif choice == "3":
                self.shipSystemAssociationForm()
            elif choice == "4":
                self.equipmentForm()
            elif choice == "5":
                self.vulnerabilityForm()
            elif choice == "6":
                self.protectionForm()
            elif choice == "7":
                self.securityIndicatorForm()
            elif choice == "8":
                self.securityIndicatorForm()
            elif choice == "9":
                self.dangerForm()
            elif choice == "10":
                self.infoShipAll()
            elif choice == "11":
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

    def shipForm(self):
        new_model = ShipSchema(
            name = input("Введите наименование корабля: "),
            description = input("Введите описание корабля: ")
        )
        self.createController.create_ship(new_model)
        print("Успешно добавлен корабль")

    def shipSystemForm(self):
        new_model = ShipSystemSchema(
            name = input("Введите наименование системы корабля: "),
            description = input("Введите описание системы корабля: "),
            type = input("Введите тип системы корабля: ")
        )
        self.createController.create_ship_system(new_model)
        print("Успешно добавлена система корабля")

    def shipSystemAssociationForm(self):
        new_model = ShipAndSystemSchema(
            ship = input("Введите наименование корабля: "),
            ship_system = input("Введите наименование системы: ")
        )
        if self.createController.create_ship_system_association(new_model):
            print("Успешно добавлена ассоциация корабля и системы")
        else: print("Не найден корабль или система")

    def equipmentForm(self):
        new_model = EquipmentSchema(
            name = input("Введите наименование оборудования: "),
            description = input("Введите описание оборудования: "),
            type = input("Введите тип оборудования корабля: "),
            ship_system = input("Введите наименование системы корабля: ")
        )
        if self.createController.create_equipment(new_model):
            print("Успешно добавлено оборудование")
        else: print("Не найдена система")

    def vulnerabilityForm(self):
        new_model = VulnerabilitySchema(
            name = input("Введите наименование уязвимости: "),
            description = input("Введите описание уязвимости: "),
            equipment = input("Введите наименование оборудования: ")
        )
        if self.createController.create_vulnerability(new_model):
            print("Успешно добавлена уязвимость")
        else: print("Не найдено оборудование")

    def protectionForm(self):
        new_model = ProtectionSchema(
            name = input("Введите наименование меры защиты: "),
            description = input("Введите описание меры защиты: "),
            equipment = input("Введите наименование или id оборудования: ")
        )
        if self.createController.create_protection(new_model):
            print("Успешно добавлена мера защиты")
        else: print("Не найдено оборудование")

    def securityIndicatorForm(self):
        new_model = SecurityIndicatorSchema(
            name = input("Введите наименование показателей защищенности: "),
            description = input("Введите описание показателей защищенности: "),
        )
        if self.createController.create_security_indicator(new_model): 
            print("Успешно добавлен показатель защищенности")
        else: print("Не найдена система")

    def systemIndicatorAssociationForm(self):
        new_model = ShipAndSystemSchema(
            ship_system = input("Введите наименование системы: "),
            security_indicator = input("Введите показатель защищенности: "),
        )
        if self.createController.create_system_indicator_association(new_model):
            print("Успешно добавлена ассоциация показателя защищенности и системы")
        else: print("Не найден показатель защищенности или система")

    def dangerForm(self):
        new_model = DangerSchema(
            name = input("Введите наименование угрозы: "),
            description = input("Введите описание угрозы: "),
            ship_system = input("Введите наименование системы корабля (опционально): ")
        )
        if self.createController.create_danger(new_model):
            print("Успешно добавлена угроза")
        else: print("Не найдена система")

    def infoShipAll(self):
        ship_name = input("Введите наименование корабля: ")
        self.selectController.displayShipModel(ship_name)