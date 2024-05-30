from sqlalchemy import select
from ..models.db import Session
from ..shemas import *
from ..models import *

class SelectShipController:
    def __init__(self):
        self.session = Session()

    async def get_ship_model(self, ship_name: str):
        ship = self.session.query(Ship).filter_by(title=ship_name).first()

        if ship:
            ship_model = ShipModelSchema(ship=ShipSchema(title=ship.title, description=ship.description), ship_systems=[])
            ship_systems = self.session.query(ShipSystem).join(ShipAndSystem).filter_by(ship_id=ship.id).all()
            
            for sys in ship_systems:
                ship_model.ship_systems.append(ShipModelSchema.SystemShipModelSchema(
                    system_ship=ShipSystemSchema(
                        title=sys.title, 
                        description=sys.description,
                        type=sys.type,
                        category=sys.category,
                        document=sys.document
                    ), security_indicators=[], equipments=[], dangers=[]
                ))
                security_indicators = self.session.query(SecurityIndicator).join(SystemAndIndicator).filter_by(ship_system_id=sys.id).all()
                for indicator in security_indicators:
                    ship_model.ship_systems[-1].security_indicators.append(SecurityIndicatorSchema(
                        title=indicator.title,
                        description=indicator.description
                    ))

                dangers = self.session.query(Danger).join(Danger4System).filter(Danger4System.ship_system_id == sys.id).all()
                for danger in dangers:
                    ship_model.ship_systems[-1].dangers.append(DangerSchema(
                        title=danger.title,
                        description=danger.description,
                        ship_system=sys.title
                    ))

                equipments = self.session.query(Equipment).join(SystemAndEquipment).filter_by(ship_system_id=sys.id).all()
                for equipment in equipments:
                    ship_model.ship_systems[-1].equipments.append(ShipModelSchema.SystemShipModelSchema.EquipmentModelSchema(
                        equipment=EquipmentSchema(title=equipment.title, description=equipment.description, type=equipment.type),
                        protections=[],
                        vulnerabilities=[]
                    ))

                    protections = self.session.query(Protection).filter_by(equipment_id=equipment.id).all()
                    for protection in protections:
                        ship_model.ship_systems[-1].equipments[-1].protections.append(ProtectionSchema(
                            title=protection.title,
                            description=protection.description,
                            equipment=equipment.title
                        ))

                    vulnerabilities = self.session.query(Vulnerability).filter_by(equipment_id=equipment.id).all()
                    for vulnerability in vulnerabilities:
                        ship_model.ship_systems[-1].equipments[-1].vulnerabilities.append(VulnerabilitySchema(
                            title=vulnerability.title,
                            description=vulnerability.description,
                            equipment=vulnerability.title
                        ))
            return ship_model.model_dump()
        