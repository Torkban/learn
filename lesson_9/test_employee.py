from employee_methods import employee_api
from db_methods import employee_db
from sqlalchemy import create_engine
import psycopg2


api = employee_api('https://x-clients-be.onrender.com')

db_connect_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
edb = employee_db(db_connect_string)

comp_db_id = edb.new_company_id()


def test_search_employee():
    api.post_employee(comp_db_id)
    resp = api.get_employee(comp_db_id)
    api_resp = resp.json()
    db_resp = edb.get_employee_by_company_id(comp_db_id)
    assert resp.status_code == 200
    assert len(api_resp) == 1 and len(db_resp) == 1


def test_create_employee():
    count_before = len(edb.get_employee_by_company_id(comp_db_id))
    em_resp = api.post_employee(comp_db_id, 33, "great_fname", "great_lmname", "great_mname", "some@mail.com", "some_url", "5553667")
    em_id = em_resp.json()["id"]
    emp = api.get_employee_by_id(em_id).json()["companyId"]
    count_after_api = len(api.get_employee(comp_db_id).json())
    count_after_db = len(edb.get_employee_by_company_id(comp_db_id))
    assert em_resp.status_code == 201
    assert count_after_db - count_before == 1
    assert emp == comp_db_id
    assert count_after_db == count_after_api
    
    
 
def test_get_employee():
    em_id = api.post_employee(comp_db_id, 33, "great_fname", "great_lmname", "great_mname", "some@mail.com", "some_url", "5553667").json()["id"]
    resp = api.get_employee_by_id(em_id)
    apiresp = resp.json()
    dbresp=edb.get_employee_by_id(em_id)
    assert resp.status_code == 200
    assert apiresp["id"] == em_id and apiresp["id"] == dbresp[0][0]
    assert apiresp["firstName"] == "great_fname" and apiresp["firstName"] == dbresp[0][4]
    assert apiresp["lastName"] == "great_lmname" and apiresp["lastName"] == dbresp[0][5]
    assert apiresp["middleName"] == "great_mname"and apiresp["middleName"] == dbresp[0][6]
    assert apiresp["phone"] == "5553667" and apiresp["phone"] == dbresp[0][7]
    assert apiresp["avatar_url"] == "some_url" and apiresp["avatar_url"] == dbresp[0][10]
    assert apiresp["companyId"] == comp_db_id and apiresp["companyId"] == dbresp[0][11]
    
def test_change_employee():
    em_id = api.post_employee(comp_db_id).json()["id"]
    resp = api.patch_employee(em_id, "strange@mail.com", "another_strange_url")
    api_resp = resp.json()
    dbresp=edb.get_employee_by_id(em_id)
    assert resp.status_code == 200
    assert api_resp["id"] == em_id and api_resp["id"] == dbresp[0][0]
    assert not api_resp["isActive"]  and not dbresp[0][1]
    assert api_resp["email"] == "strange@mail.com" and api_resp["email"] == dbresp[0][8]
    assert api_resp["url"] == "another_strange_url" and api_resp["url"] == dbresp[0][10]
    
    # удаление тестовых данных
    del_id = edb.get_employee_by_company_id(comp_db_id)
    for i in del_id:
        edb.delete_employee_by_id(i[0])
    edb.delete_company_by_id(comp_db_id)    

