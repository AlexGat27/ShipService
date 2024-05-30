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
        stmt = select(ShipAndSystem.id, Ship.title, Ship.description,\
                      ShipSystem.title, ShipSystem.description, ShipSystem.type, ShipSystem.category, ShipSystem.document) \
        .join(ShipAndSystem, Ship.id == ShipAndSystem.ship_id) \
        .join(ShipSystem, ShipSystem.id == ShipAndSystem.ship_system_id)
        sendData = []
        for row in self.session.execute(stmt).fetchall():
            sendData.append({"id": row[0],
                            "model1": {"title": row[1], "description": row[2]}, \
                             "model2": {"title": row[3], "description": row[4], "type": row[5], "category": row[6], "document": row[7]}})
        return sendData
    
    async def get_system_equipment_association(self):
        stmt = select(SystemAndEquipment.id, Equipment.title, Equipment.description, Equipment.type, \
                      ShipSystem.title, ShipSystem.description, ShipSystem.type, ShipSystem.category, ShipSystem.document) \
        .join(SystemAndEquipment, Equipment.id == SystemAndEquipment.equipment_id) \
        .join(ShipSystem, ShipSystem.id == SystemAndEquipment.ship_system_id)
        sendData = []
        for row in self.session.execute(stmt).fetchall():
            sendData.append({"id": row[0],
                            "model1": {"title": row[1], "description": row[2], "type": row[3]}, \
                            "model2": {"title": row[4], "description": row[5], "type": row[6], "category": row[7], "document": row[8]}})
        return sendData
    
    async def get_system_security_association(self):
        stmt = select(SystemAndIndicator.id, SecurityIndicator.title, SecurityIndicator.description, \
                      ShipSystem.title, ShipSystem.description, ShipSystem.type, ShipSystem.category, ShipSystem.document) \
        .join(SystemAndIndicator, SecurityIndicator.id == SystemAndIndicator.security_indicator_id) \
        .join(ShipSystem, ShipSystem.id == SystemAndIndicator.ship_system_id)
        sendData = []
        for row in self.session.execute(stmt).fetchall():
            sendData.append({"id": row[0],
                            "model1": {"title": row[1], "description": row[2]}, \
                             "model2": {"title": row[3], "description": row[4], "type": row[5], "category": row[6], "document": row[7]}})
        return sendData