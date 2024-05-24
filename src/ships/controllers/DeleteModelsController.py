from ..models.db import Session
from ..shemas import *
from ..models import *

class DeleteModelsController():

    def __init__(self):
        self.session = Session()

    async def delete_model(self, id: int, tablename: str):
        print(id, tablename)
        for table in Base.metadata.tables.values():
            if table.name == tablename:
                delete_query = table.delete().where(table.c.id == id)
                result = self.session.execute(delete_query)
                if result.rowcount > 0:
                    self.session.commit()
                    return 200  # Успешно удалено
                else:
                    return 404  # Объект не найден
                break
        return 404
        