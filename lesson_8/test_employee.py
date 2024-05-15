from employee_methods import employee

api = employee('https://x-clients-be.onrender.com')

comp_id = api.get_company_id()


def test_search_employee():
    api.post_employee(comp_id)
    resp = api.get_employee(comp_id)
    bresp = resp.json()
    assert resp.status_code == 200
    assert len(bresp) == 1
    
def test_create_employee():
    count_before = len(api.get_employee(comp_id).json())
    em_id = api.post_employee(comp_id)
    needed_id = em_id.json()["id"]
    emp = api.get_employee_by_id(needed_id).json()["companyId"]
    count_after = len(api.get_employee(comp_id).json())
    assert em_id.status_code == 201
    assert count_after - count_before == 1
    assert emp == comp_id
    
    
def test_get_employee():
    em_id = api.post_employee(comp_id, 33, "great_fname", "great_lmname", "great_mname", "some@mail.com", "some_url", "5553667").json()["id"]
    resp = api.get_employee_by_id(em_id)
    bresp = resp.json()
    assert resp.status_code == 200
    assert bresp["id"] == em_id
    assert bresp["firstName"] == "great_fname"
    assert bresp["lastName"] == "great_lmname"
    assert bresp["middleName"] == "great_mname"
    assert bresp["phone"] == "5553667"
    assert bresp["avatar_url"] == "some_url"
    assert bresp["companyId"] == comp_id
    
def test_change_employee():
    em_id = api.post_employee(comp_id).json()["id"]
    resp = api.patch_employee(em_id, "strange@mail.com", "another_strange_url")
    bresp = resp.json()
    assert resp.status_code == 200
    assert bresp["id"] == em_id
    assert not bresp["isActive"] 
    assert bresp["email"] == "strange@mail.com"
    assert bresp["url"] == "another_strange_url"
    
api.delete_company(comp_id)