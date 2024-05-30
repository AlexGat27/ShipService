from ..models.db import Session
from ..shemas import *
from ..models import *

class CreateModelsController():

    def __init__(self):
        self.session = Session()

    async def create_ship(self, ship: ShipSchema):
        if self.session.query(Ship).filter_by(title=ship.title).first(): return False
        new_model = Ship(**ship.model_dump())
        self.session.add(new_model)
        self.session.commit()
        return True

    async def create_ship_system(self, ship_system: ShipSystemSchema):
        if self.session.query(ShipSystem).filter_by(title=ship_system.title).first(): return False
        new_model = ShipSystem(**ship_system.model_dump())
        self.session.add(new_model)
        self.session.commit()
        return True

    async def create_ship_system_association(self, ship_and_system: ShipAndSystemSchema) -> bool:
        potential_ship = self.session.query(Ship).filter_by(title=ship_and_system.ship).first()
        potential_ship_system = self.session.query(ShipSystem).filter_by(title=ship_and_system.ship_system).first()
        if potential_ship is not None and potential_ship_system is not None: 
            ship_id = potential_ship.id
            ship_system_id = potential_ship_system.id
            ship_and_system_data = {"ship_id": ship_id, "ship_system_id": ship_system_id}
            if self.session.query(ShipAndSystem).filter_by(**ship_and_system_data).first(): return False
            new_model = ShipAndSystem(**ship_and_system_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    async def create_equipment(self, equipment: EquipmentSchema) -> bool:
        if self.session.query(Equipment).filter_by(title=equipment.title).first(): return False
        new_model = Equipment(**equipment.model_dump())
        self.session.add(new_model)
        self.session.commit()
        return True

    async def create_system_equipment_association(self, system_and_equipment: SystemAndEquipmentSchema) -> bool:
        potential_equipment = self.session.query(Equipment).filter_by(title=system_and_equipment.equipment).first()
        potential_ship_system = self.session.query(ShipSystem).filter_by(title=system_and_equipment.ship_system).first()
        if potential_equipment is not None and potential_ship_system is not None: 
            equipment_id = potential_equipment.id
            ship_system_id = potential_ship_system.id
            system_and_equipment_data = {"equipment_id": equipment_id, "ship_system_id": ship_system_id}
            if self.session.query(SystemAndEquipment).filter_by(**system_and_equipment_data).first(): return False
            new_model = SystemAndEquipment(**system_and_equipment_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    async def create_vulnerability(self, vulnerability: VulnerabilitySchema) -> bool:
        if self.session.query(Vulnerability).filter_by(title=vulnerability.title).first(): return False
        potential_equipment = self.session.query(Equipment).filter_by(title=vulnerability.equipment).first()
        if potential_equipment is not None:
            equipment_id = potential_equipment.id
            vulnerability_data = {key: value for key, value in vulnerability.model_dump().items() if key != "equipment"}
            vulnerability_data["equipment_id"] = equipment_id
            new_model = Vulnerability(**vulnerability_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    async def create_protection(self, protection: ProtectionSchema) -> bool:
        if self.session.query(Protection).filter_by(title=protection.title).first(): return False
        potential_equipment = self.session.query(Equipment).filter_by(title=protection.equipment).first()
        if potential_equipment is not None:
            equipment_id = potential_equipment.id
            protection_data = {key: value for key, value in protection.model_dump().items() if key != "equipment"}
            protection_data["equipment_id"] = equipment_id
            new_model = Protection(**protection_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    async def create_security_indicator(self, security_indicator: SecurityIndicatorSchema) -> bool:
        if self.session.query(SecurityIndicator).filter_by(title=security_indicator.title).first(): return False
        new_model = SecurityIndicator(**security_indicator.model_dump())
        self.session.add(new_model)
        self.session.commit()
        return True

    async def create_system_indicator_association(self, system_and_indicator: SystemAndIndicatorSchema):
        potential_indicator = self.session.query(SecurityIndicator).filter_by(title=system_and_indicator.security_indicator).first()
        potential_ship_system = self.session.query(ShipSystem).filter_by(title=system_and_indicator.ship_system).first()
        if potential_indicator is not None and potential_ship_system is not None: 
            security_indicator_id = potential_indicator.id
            ship_system_id = potential_ship_system.id
            system_and_indicator_data = {"security_indicator_id": security_indicator_id, "ship_system_id": ship_system_id}
            if self.session.query(SystemAndIndicator).filter_by(**system_and_indicator_data).first(): 
                return False
            new_model = SystemAndIndicator(**system_and_indicator_data)
            self.session.add(new_model)
            self.session.commit()
            return True
        else: return False

    async def create_danger(self, danger: DangerSchema) -> bool:
        danger_data = {key: value for key, value in danger.model_dump().items() if key != "ship_system"}
        if self.session.query(Danger).filter_by(title=danger.title).first(): 
            return False
        new_model = Danger(**danger_data)
        self.session.add(new_model)
        if danger.ship_system is not None:
            potential_ship_system = self.session.query(ShipSystem).filter_by(title=danger.ship_system).first()
            if potential_ship_system is not None: 
                ship_system_id = potential_ship_system.id
                danger_for_system_data = { "danger_id": new_model.id, "ship_system_id": ship_system_id }
                new_model = Danger4System(**danger_for_system_data)
                self.session.add(new_model)
            else: return False
        self.session.commit()
        return True