from filling_the_form import good_elems_id
from filling_the_form import bad_elems_id

good_selectors_list = ['first-name','last-name','address', 'city','country', 'e-mail','phone', 'job-position','company']
bad_selectors_list = ['zip-code']   
    
def test_bad_filling_the_form():
    for i in bad_elems_id:
        assert i in bad_selectors_list and len(bad_elems_id) == 1
     
           
def test_good_filling_the_form():
    for i in good_elems_id:
        assert i in good_selectors_list and len(good_elems_id) == 9
        