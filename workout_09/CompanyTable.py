from sqlalchemy import create_engine
from sqlalchemy.sql import text
import allure


class CompanyTable:
    """Класс предоставляет методы для работы с БД"""
    # упакрвка запросов к базе данных в скрипты
    __scripts = {
        "select": "select * from company where deleted_at is null",
        # "deleted_at is null" проверяет, что в базе даных нет компаний, которые удалены через api
        # (т.к. при удалении через api, они временно ещё присутствуют в таблице, но со статусом удаленные
        "select by id": text("select * from company where id  = :select_id"),
        "select only active": "select * from company where is_active = true and deleted_at is null",
        "delete by id": text("delete from company where id = :id_to_delete"),
        "insert new": text("insert into company (\"name\",\"description\") values (:new_name, :new_descr)"),
        "get max id": "select max(id) from company"
    }
    # создание подключения к таблице
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)
        
    @allure.step("БД. Запросить список организаций")
    def get_companies(self):
        query = self.__db.execute(self.__scripts["select"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    @allure.step("БД. Получить организацию по {id}")
    def get_company_by_id(self, id):
        query = self.__db.execute(self.__scripts["select by id"], select_id = id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()
    
    @allure.step("БД. Запросить список ативных организаций")
    def get_active_companies(self):
        query = self.__db.execute(self.__scripts["select only active"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()
    
    @allure.step("БД. Удалить организацию по {id}")
    def delete(self, id):
        query =self.__db.execute(self.__scripts["delete by id"], id_to_delete = id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Создать организацию {name} ({descr})")
    def create(self, name, descr):
        query =self.__db.execute(self.__scripts["insert new"], new_name= name, new_descr= descr)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)

    @allure.step("БД. Получить последнюю созданную организацию")
    def get_max_id(self):
        query = self.__db.execute(self.__scripts["get max id"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]
