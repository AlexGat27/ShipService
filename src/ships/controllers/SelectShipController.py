from ..models.db import Session
from ..shemas import *
from ..models import *

class SelectShipController:
    def __init__(self):
        self.session = Session()

    def displayShipModel(self, ship_name: str):
        ship = self.session.query(Ship).filter_by(name=ship_name).first()

        if ship:
            print(f"Системы корабля {ship_name}:")
            print("===========================================================================")
            # Найдите все системы корабля
            ship_systems = self.session.query(ShipSystem).join(ShipAndSystem).filter_by(ship_id=ship.id).all()
            
            for system in ship_systems:
                print(f"Наименование системы: {system.name}")
                print(f"Описание системы: {system.description}")
                # Найдите все показатели защищенности для этой системы
                security_indicators = self.session.query(SecurityIndicator).filter_by(ship_system_id=system.id).all()
                print("\nПоказатели защищенности:")
                for indicator in security_indicators:
                    print(f"- {indicator.name}: {indicator.description}")

                # Найдите все опасности для этой системы
                dangers = self.session.query(Danger4System).filter_by(ship_system_id=system.id).all()
                print("\nУгрозы системы:")
                for danger in dangers:
                    print(f"- {danger.danger.name}: {danger.danger.description}")

                # Найдите все оборудование с защитой для этой системы
                equipments = self.session.query(Equipment).filter_by(ship_system_id=system.id).all()
                print("\nОборудование системы:")
                print("------------------------------------------------------------------------")
                for equipment in equipments:
                    print(f"Наименование оборудования: {equipment.name}")
                    print(f"Описание оборудования: {equipment.description}")
                
                    # Найдите все оборудование с защитой для этой системы
                    protections = self.session.query(Protection).filter_by(equipment_id=equipment.id).all()
                    print("\nМеры защиты оборудования:")
                    for protection in protections:
                        print(f"- {protection.name}: {protection.description}")

                    vulnerabilities = self.session.query(Vulnerability).filter_by(equipment_id=equipment.id).all()
                    print("\nУязвимости оборудования:")
                    for vulnerability in vulnerabilities:
                        print(f"- {vulnerability.name}: {vulnerability.description}")
                    print("------------------------------------------------------------------------")
                    
                print("===========================================================================\n")
        else:
            print(f"Корабль с именем {ship_name} не найден.")