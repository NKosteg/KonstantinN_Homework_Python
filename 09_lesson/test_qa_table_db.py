from SubjectTable import SubjectTable
from TeacherTable import TeacherTable

db_subject = SubjectTable("postgresql://postgres:zq21/04@localhost:5432/QA training SkyPro")
db_teacher = TeacherTable("postgresql://postgres:zq21/04@localhost:5432/QA training SkyPro")


# проверка, что после удаления предмета в БД он больше не отображается в таблице subject
def test_delete_subject():
    subject_id = 16
    subject_title = 'Chemistry'
    db_subject.create_subject(subject_id, subject_title)
    new_id = db_subject.get_max_id()
    db_subject.delete_subject(new_id)
    rows = db_subject.get_subject(new_id)
    assert len(rows) == 0


# проверка записи в БД после создании нового предмета в таблице subject
def test_add_subject():
    subject_id = 16
    subject_title = 'Chemistry'
    db_subject.create_subject(subject_id, subject_title)
    new_id = db_subject.get_max_id()
    new_subject = db_subject.get_subject(new_id)
    db_subject.delete_subject(new_id)
    assert new_subject[0][1] == subject_title


# проверка записи в БД после изменения названия предмета в таблице subject
def test_update_subject():
    subject_id = 16
    subject_title = 'Chemistry'
    db_subject.create_subject(subject_id, subject_title)
    new_id = db_subject.get_max_id()
    new_subject_title = 'Biology'
    db_subject.update_subject(new_subject_title, new_id)
    new_subject = db_subject.get_subject(new_id)
    db_subject.delete_subject(new_id)
    assert new_subject[0][1] == new_subject_title


# проверка, что после удаления записи об учителе из БД, данные больше не отображаются в таблице teacher
def test_delete_teacher():
    teacher_id = 34995
    teacher_email = 'uchitel.goda@shool.net'
    group_id = 201
    db_teacher.create_teacher(teacher_id, teacher_email, group_id)
    new_id = db_teacher.get_max_id()
    db_teacher.delete_teacher(new_id)
    rows = db_teacher.get_teacher(new_id)
    assert len(rows) == 0


# проверка записи в БД после создания нового учителя в таблице teacher
def test_add_teacher():
    id_teacher = 34995
    email_teacher = 'uchitel.goda@shool.net'
    id_group = 201
    db_teacher.create_teacher(id_teacher, email_teacher, id_group)
    new_id = db_teacher.get_max_id()
    new_teacher = db_teacher.get_teacher(new_id)
    db_teacher.delete_teacher(new_id)
    assert new_teacher[0]['email'] == email_teacher
    assert new_teacher[0]['group_id'] == id_group


# проверка записи в БД после изменения группы учителя в таблице teacher
def test_update_teacher():
    id_teacher = 34995
    email_teacher = 'uchitel.goda@shool.net'
    id_group = 201
    db_teacher.create_teacher(id_teacher, email_teacher, id_group)
    new_id = db_teacher.get_max_id()
    new_id_group = 404
    db_teacher.update_teacher(new_id_group, new_id)
    new_teacher = db_teacher.get_teacher(new_id)
    db_teacher.delete_teacher(new_id)
    assert new_teacher[0]['email'] == email_teacher
    assert new_teacher[0]['group_id'] == new_id_group
