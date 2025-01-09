from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CompanyTable:
    # упакрвка запросов к базе данных в скрипты
    __scripts = {
        "select": "select * from company where deleted_at is null",
        "select by id": text("select * from company where id  = :select_id"),
        "select only active": "select * from company where is_active = true and deleted_at is null",
        "delete by id": text("delete from company where id = :id_to_delete"),
        "insert new": text("insert into company (\"name\",\"description\") values (:new_name, :new_descr)"),
        "get max id": "select max(id) from company"
    }
    # создание подключения к таблице
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        
    # получение списка всех компаний из таблицы
    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()
    # "deleted_at is null" проверяет, что в базе даных нет компаний, которые удалены через api
    # (т.к. при удалении через api, они временно ещё присутствуют в таблице, но со статусом удаленные

    # получение компании по id
    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id = id).fetchall()
    
    # получение списка всех активных компаний из таблицы
    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select only active"]).fetchall()
    
    # удаление компании серез БД по id
    def delete(self, id):
        self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)

    # создание новой компании в БД
    def create(self, name, descr):
        self.__db.execute(self.__scripts["insert new"], new_name= name, new_descr= descr)

    # получение компании из таблицы по последнему/максимальному id
    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

