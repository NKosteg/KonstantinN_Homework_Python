from sqlalchemy import create_engine
from sqlalchemy.sql import text


class TeacherTable:
    __scripts = {
        "insert teacher": text("insert into teacher (teacher_id, email, group_id) values (:t_id, :email, :gr_id)"),
        "get max id": "select max(teacher_id) from teacher",
        "select by id": text("select * from teacher where teacher_id = :select_id"),
        "delete by id": text("delete from teacher where teacher_id = :select_id"),
        "update group": text("update teacher set group_id = :new_group where teacher_id = :id")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_teacher(self, teacher_id, email, group_id):
        self.__db.execute(self.__scripts["insert teacher"], t_id=teacher_id, email=email, gr_id=group_id)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get max id"]).fetchall()[0][0]

    def delete_teacher(self, teacher_id):
        self.__db.execute(self.__scripts["delete by id"], select_id=teacher_id)

    def get_teacher(self, teacher_id):
        return self.__db.execute(self.__scripts["select by id"], select_id=teacher_id).fetchall()

    def update_teacher(self, group_id, teacher_id):
        self.__db.execute(self.__scripts["update group"], new_group=group_id, id=teacher_id)
