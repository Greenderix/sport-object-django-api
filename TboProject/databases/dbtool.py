import sqlite3


class Objectbase:
    __db = None
    __cursor = None

    def __init__(self) -> None:
        self.__db = sqlite3.connect('db.sqllite3', check_same_thread=False)
        self.__cursor = self.__db.cursor()

    def get_objects(self, active: bool | None = None, text: str | None = None):
        objects = []

        if active is not None:
            self.__cursor.execute(
                f"SELECT * FROM `TboProject_objectlocations` WHERE `activ` = '{'Y' if active else 'N'}' LIMIT 800")
        elif text is not None:
            self.__cursor.execute("SELECT * FROM TboProject_objectlocations WHERE addres LIKE ? LIMIT 800",
                                  (f'%{text.lower()}%',))

        for row in self.__cursor.fetchall():
            objects.append({
                "id": row[0],
                "name": row[1],
                "active": row[2],
                "desc": row[3].replace('&#40', '').replace('&#41', '').replace('&#37', '') if row[3] else row[4],
                "address": row[5],
                "oktmo": row[6],
                "fcp": row[7],
                "action": row[8].title(),
                "value": row[11],
                "curator": row[12],
                "phone": ''.join(x for x in row[13] if x.isdigit()) if row[13] else row[13],
                "workingHours": row[14],
                "email": row[15],
                "siteUrl": row[16],
                "objectType": row[17].title() if row[17] else row[17],
                "sportType": row[18].title() if row[18] else row[18],
                "coordinates": {"lat": row[22], "lng": row[19]},
                "photoUrl": row[21]
            })
        return objects

    # def get_cash_object(self, id_object: int):
    #     cash = []
    #
    #     self.__cursor.execute(
    #         f"SELECT `financing_federal`, `financing_subject`, `financing_municipal`, `financing_outside` FROM `TboProject_objectlocations` WHERE `id` = ?",
    #         (id_object,))
    #     for row in self.__cursor.fetchone():
    #         cash.append(row)
    #     return cash

    def get_search_object(self, text: str):
        objects = []
        self.__cursor.execute("SELECT * FROM TboProject_objectlocations WHERE addres LIKE ? LIMIT 800",
                              (f'%{text.lower()}%',))
        for row in self.__cursor.fetchall():
            objects.append({
                "id": row[0],
                "name": row[1],
                "active": row[2],
                "desc": row[3].replace('&#40', '').replace('&#41', '').replace('&#37', '') if row[3] else row[4],
                "address": row[5],
                "oktmo": row[6],
                "fcp": row[7],
                "action": row[8].title(),
                "value": row[11],
                "curator": row[12],
                "phone": ''.join(x for x in row[13] if x.isdigit()) if row[13] else row[13],
                "workingHours": row[14],
                "email": row[15],
                "siteUrl": row[16],
                "objectType": row[17].title() if row[17] else row[17],
                "sportType": row[18].title() if row[18] else row[18],
                "coordinates": {"lat": row[22], "lng": row[19]},
                "photoUrl": row[21]
            }
            )
        return objects
