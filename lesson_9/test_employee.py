from employee_methods import employee_api
from db_methods import employee_db
from sqlalchemy import create_engine
from faker import Faker
import psycopg2


api = employee_api('https://x-clients-be.onrender.com')

db_connect_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
edb = employee_db(db_connect_string)

comp_db_id = edb.new_company_id()
test_em_id = 2
fake = Faker("ru_RU")
a = fake.first_name()
test_dict = {"fn1": a, "fn2": a,  "ln1":a, "ln2":a, "mn1":a, "mn2":a, "e-mail1": fake.ascii_free_email(), "e-mail2": fake.ascii_free_email(), "e-mail3": fake.ascii_free_email(), "url1":a, "url2":a, "url3":a,"t1": fake.phone_number(),"t2": fake.phone_number()}


def test_search_employee():
    api.post_employee(comp_db_id)
    resp = api.get_employee(comp_db_id)
    api_resp = resp.json()
    db_resp = edb.get_employee_by_company_id(comp_db_id)
    assert resp.status_code == 200
    assert len(api_resp) == 1 and len(db_resp) == 1


def test_create_employee():
    count_before = len(edb.get_employee_by_company_id(comp_db_id))
    em_resp = api.post_employee(comp_db_id, test_em_id, test_dict["fn1"], test_dict["ln1"], test_dict["mn1"], test_dict["e-mail1"], test_dict["url1"], test_dict["t1"])
    em_id = em_resp.json()["id"]
    emp = api.get_employee_by_id(em_id).json()["companyId"]
    count_after_api = len(api.get_employee(comp_db_id).json())
    count_after_db = len(edb.get_employee_by_company_id(comp_db_id))
    assert em_resp.status_code == 201
    assert count_after_db - count_before == 1
    assert emp == comp_db_id
    assert count_after_db == count_after_api
    
test_em_id += 1
 
def test_get_employee():
    em_id = api.post_employee(comp_db_id, test_em_id, test_dict["fn2"], test_dict["ln2"], test_dict["mn2"], test_dict["e-mail2"], test_dict["url2"], test_dict["t2"]).json()["id"]
    resp = api.get_employee_by_id(em_id)
    apiresp = resp.json()
    dbresp=edb.get_employee_by_id(em_id)
    assert resp.status_code == 200
    assert apiresp["id"] == em_id and apiresp["id"] == dbresp[0][0]
    assert apiresp["firstName"] == test_dict["fn2"] and apiresp["firstName"] == dbresp[0][4]
    assert apiresp["lastName"] == test_dict["ln2"] and apiresp["lastName"] == dbresp[0][5]
    assert apiresp["middleName"] == test_dict["mn2"] and apiresp["middleName"] == dbresp[0][6]
    assert apiresp["phone"] == test_dict["t2"] and apiresp["phone"] == dbresp[0][7]
    assert apiresp["avatar_url"] == test_dict["url2"] and apiresp["avatar_url"] == dbresp[0][10]
    assert apiresp["companyId"] == comp_db_id and apiresp["companyId"] == dbresp[0][11]
    
def test_change_employee():
    em_id = api.post_employee(comp_db_id).json()["id"]
    resp = api.patch_employee(em_id, test_dict["e-mail3"], test_dict["url3"])
    api_resp = resp.json()
    dbresp=edb.get_employee_by_id(em_id)
    assert resp.status_code == 200
    assert api_resp["id"] == em_id and api_resp["id"] == dbresp[0][0]
    assert not api_resp["isActive"]  and not dbresp[0][1]
    assert api_resp["email"] == test_dict["e-mail3"] and api_resp["email"] == dbresp[0][8]
    assert api_resp["url"] == test_dict["url3"] and api_resp["url"] == dbresp[0][10]
    
    # удаление тестовых данных
    del_id = edb.get_employee_by_company_id(comp_db_id)
    for i in del_id:
        edb.delete_employee_by_id(i[0])
    edb.delete_company_by_id(comp_db_id)    

