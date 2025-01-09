from sqlalchemy import create_engine, text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)



def test_db_connection():
    names = db.table_names()
    assert names[1] == 'app_users'

def test_select():
    rows = db.execute("select * from company").fetchall()
    print(rows)
    row1 = rows[-1]

    assert row1['id'] == 657
    assert row1["name"] == 'My company 8'

def test_select_1_row():
    sql_statement = text("select * from company where id = :company_id")
    rows = db.execute(sql_statement, company_id = 2).fetchall()

    assert len(rows) == 1
    assert rows[0]["name"] == 'Автоматизация тестирования'

def test_select_1_row_with_two_filters():
    sql_statement = text("select * from company where is_active = :is_active and id >= :id")
    my_param = {
        'id': 601,
        'is_active': True
    }
    rows = db.execute(sql_statement, my_param).fetchall()

    assert len(rows) == 19
    assert rows[-1]["name"] == 'My company 8'

def test_insert():
    sql = text("insert into company (\"name\") values (:new_name)")
    rows = db.execute(sql, new_name = 'Kosta SQL School')

def test_update():
    sql = text("update company set description = :descr where id = :id")
    rows = db.execute(sql, {"descr": 'new descr', "id": 659})

def test_delete():
    sql = text("delete from company where id = :id")
    rows = db.execute(sql, id = 659)