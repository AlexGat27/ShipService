from sqlalchemy import select
from ..models.db import Session
from ..shemas import *
from ..models import *
from typing import Union

class GetShipController:
    def __init__(self):
        self.session = Session()

    async def getModels(self, table: type):
        result = self.session.query(table).all()
        return result

    async def get_ship_system_association(self):
        stmt = select(Ship.title, Ship.description, ShipSystem.title, ShipSystem.description, ShipSystem.type) \
        .join(ShipAndSystem, Ship.id == ShipAndSystem.ship_id) \
        .join(ShipSystem, ShipSystem.id == ShipAndSystem.ship_system_id)
        sendData = []
        for row in self.session.execute(stmt).fetchall():
            sendData.append({"model1": {"title": row[0], "description": row[1]}, \
                             "model2": {"title": row[2], "description": row[3], "type": row[4]}})
        return sendData
    
    async def get_system_equipment_association(self):
        stmt = select(Equipment.title, Equipment.description, Equipment.type, ShipSystem.title, ShipSystem.description, ShipSystem.type) \
        .join(SystemAndEquipment, Equipment.id == SystemAndEquipment.equipment_id) \
        .join(ShipSystem, ShipSystem.id == SystemAndEquipment.ship_system_id)
        sendData = []
        for row in self.session.execute(stmt).fetchall():
            sendData.append({"model1": {"title": row[0], "description": row[1], "type": row[2]}, \
                             "model2": {"title": row[3], "description": row[4], "type": row[5]}})
        return sendData
    
    async def get_system_security_association(self):
        stmt = select(SecurityIndicator.title, SecurityIndicator.description, ShipSystem.title, ShipSystem.description, ShipSystem.type) \
        .join(SystemAndIndicator, SecurityIndicator.id == SystemAndIndicator.security_indicator_id) \
        .join(ShipSystem, ShipSystem.id == SystemAndIndicator.ship_system_id)
        sendData = []
        for row in self.session.execute(stmt).fetchall():
            sendData.append({"model1": {"title": row[0], "description": row[1]}, \
                             "model2": {"title": row[2], "description": row[3], "type": row[4]}})
        return sendData