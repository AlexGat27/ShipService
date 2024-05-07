from src.models.db import Session
from src.shemas import *
from src.models import *

class CreateModelsController():

    def __init__(self):
        self.session = Session()

    def create_ship(self, ship: ShipSchema):
        with Session() as session:
            new_model = ShipSystem(**ship)
            self.session.add(new_model)
            self.session.commit()

    def create_ship_system(self, ship_system: ShipSystemSchema):
        with Session() as session:
            ship_id = session.query(Ship).filter_by(name=ship_system.ship).first().id
            ship_system_data = {key: value for key, value in ship_system.model_dump() if key != "ship"}
            ship_system_data["ship_id"] = ship_id
            new_model = ShipSystem(**ship_system_data)
            self.session.add(new_model)
            self.session.commit()

    def create_equipment(self, equipment: EquipmentSchema):
        with Session() as session:
            ship_system_id = session.query(ShipSystem).filter_by(name=equipment.ship_system).first().id
            equipment_data = {key: value for key, value in equipment.model_dump() if key != "ship_system"}
            equipment_data["ship_system_id"] = ship_system_id
            new_model = Equipment(**equipment_data)
            self.session.add(new_model)
            self.session.commit()

    def create_vulnerability(self, vulnerability: VulnerabilitySchema):
        with Session() as session:
            equipment_id = session.query(ShipSystem).filter_by(name=vulnerability.equipment).first().id
            vulnerability_data = {key: value for key, value in vulnerability.model_dump() if key != "equipment"}
            vulnerability_data["equipment_id"] = equipment_id
            new_model = Vulnerability(**vulnerability_data)
            self.session.add(new_model)
            self.session.commit()

    def create_protection(self, protection: ProtectionSchema):
        with Session() as session:
            equipment_id = session.query(ShipSystem).filter_by(name=protection.equipment).first().id
            protection_data = {key: value for key, value in protection.model_dump() if key != "equipment"}
            protection_data["equipment_id"] = equipment_id
            new_model = Protection(**protection_data)
            self.session.add(new_model)
            self.session.commit()

    def create_security_indicator(self, security_indicator: SecurityIndicatorSchema):
        with Session() as session:
            ship_system_id = session.query(ShipSystem).filter_by(name=security_indicator.ship_system).first().id
            security_indicator_data = {key: value for key, value in security_indicator.model_dump() if key != "ship_system"}
            security_indicator_data["ship_system_id"] = ship_system_id
            new_model = SecurityIndicator(**security_indicator_data)
            self.session.add(new_model)
            self.session.commit()

    def create_danger(self, danger: DangerSchema):
        with Session() as session:
            ship_system_id = session.query(ShipSystem).filter_by(name=danger.ship_system).first().id
            danger_data = {key: value for key, value in danger.model_dump() if key != "ship_system"}
            new_model = Danger(**danger_data)
            self.session.add(new_model)
            danger_for_system_data = { "danger_id": new_model.id, "ship_system_id": ship_system_id }
            new_model = Danger4System(**danger_for_system_data)
            self.session.add(new_model)
            self.session.commit()