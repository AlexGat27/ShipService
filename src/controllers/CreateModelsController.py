from src.models.db import Session
from src.shemas import *
from src.models import *

class CreateModelsController():

    def __init__(self):
        self.session = Session()

    def create_ship(self, ship: ShipSchema):
        new_model = Ship(**ship.model_dump())
        self.session.add(new_model)
        self.session.commit()

    def create_ship_system(self, ship_system: ShipSystemSchema):
        new_model = ShipSystem(**ship_system.model_dump())
        self.session.add(new_model)
        self.session.commit()

    def create_ship_system_association(self, ship_and_system: ShipAndSystemSchema) -> bool:
        potential_ship = self.session.query(Ship).filter_by(name=ship_and_system.ship).first()
        potential_ship_system = self.session.query(ShipSystem).filter_by(name=ship_and_system.ship_system).first()
        if potential_ship is not None and potential_ship_system is not None: 
            ship_id = potential_ship.id
            ship_system_id = potential_ship_system.id
            ship_and_system_data = {key: value for key, value in ship_and_system.model_dump().items() if key != "ship" and key != "ship_system"}
            ship_and_system_data["ship_id"] = ship_id
            ship_and_system_data["ship_system_id"] = ship_system_id
            new_model = ShipAndSystem(**ship_and_system_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    def create_equipment(self, equipment: EquipmentSchema) -> bool:
        potential_ship_system = self.session.query(ShipSystem).filter_by(name=equipment.ship_system).first()
        if potential_ship_system is not None: 
            ship_system_id = potential_ship_system.id
            equipment_data = {key: value for key, value in equipment.model_dump().items() if key != "ship_system"}
            equipment_data["ship_system_id"] = ship_system_id
            new_model = Equipment(**equipment_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    def create_vulnerability(self, vulnerability: VulnerabilitySchema) -> bool:
        potential_equipment = self.session.query(Equipment).filter_by(name=vulnerability.equipment).first()
        if potential_equipment is not None:
            equipment_id = potential_equipment.id
            vulnerability_data = {key: value for key, value in vulnerability.model_dump().items() if key != "equipment"}
            vulnerability_data["equipment_id"] = equipment_id
            new_model = Vulnerability(**vulnerability_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    def create_protection(self, protection: ProtectionSchema) -> bool:
        potential_equipment = self.session.query(Equipment).filter_by(name=protection.equipment).first()
        if potential_equipment is not None:
            equipment_id = potential_equipment.id
            protection_data = {key: value for key, value in protection.model_dump().items() if key != "equipment"}
            protection_data["equipment_id"] = equipment_id
            new_model = Protection(**protection_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    def create_security_indicator(self, security_indicator: SecurityIndicatorSchema) -> bool:
        potential_ship_system = self.session.query(ShipSystem).filter_by(name=security_indicator.ship_system).first()
        if potential_ship_system is not None: 
            ship_system_id = potential_ship_system.id
            security_indicator_data = {key: value for key, value in security_indicator.model_dump().items() if key != "ship_system"}
            security_indicator_data["ship_system_id"] = ship_system_id
            new_model = SecurityIndicator(**security_indicator_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    def create_danger(self, danger: DangerSchema) -> bool:
        danger_data = {key: value for key, value in danger.model_dump().items() if key != "ship_system"}
        new_model = Danger(**danger_data)
        self.session.add(new_model)
        if danger.ship_system is not None:
            potential_ship_system = self.session.query(ShipSystem).filter_by(name=danger.ship_system).first()
            if potential_ship_system is not None: 
                ship_system_id = potential_ship_system.id
                danger_for_system_data = { "danger_id": new_model.id, "ship_system_id": ship_system_id }
                new_model = Danger4System(**danger_for_system_data)
                self.session.add(new_model)
            else:
                return False
        self.session.commit()
        return True