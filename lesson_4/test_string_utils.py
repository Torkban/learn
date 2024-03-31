import pytest
from string_utils import StringUtils

@pytest.mark.positive_test
@pytest.mark.parametrize('str1, str2',[('строка','Строка'),('some string','Some string'),('4to-yo inoe','4to-yo inoe'),('','')])
def test_capitilize(str1,str2):
    s_utils = StringUtils()
    result = s_utils.capitilize(str1)
    assert result == str2
    
    
@pytest.mark.positive_test   
@pytest.mark.parametrize('str1, str2',[(' строка','строка'),('   some string','some string'),('   ',''),('some space at end   ','some space at end   ')])
def test_trim(str1,str2):
    s_utils = StringUtils()
    result = s_utils.trim(str1)
    assert result == str2
    
    
@pytest.mark.positive_test      
@pytest.mark.parametrize('str1, str2, l_chr',[('строка, с, разделителями,',',',['строка', ' с', ' разделителями','']),('here is some string','s',['here i', ' ', 'ome ', 'tring']),('','',[])])
def test_to_list(str1, str2,l_chr):
    s_utils = StringUtils()
    result = s_utils.to_list(str1, str2)
    assert result == l_chr
    
    
@pytest.mark.positive_test      
@pytest.mark.parametrize('str1, str2, bool',[('строка, c, разделителями,','c', True), ('here is some string','s',True), ('s s',' ', True), ('rrrrttt', 'a', False)])
def test_contains(str1, str2, bool):
    s_utils = StringUtils()
    result = s_utils.contains(str1, str2)
    assert result == bool


@pytest.mark.positive_test      
@pytest.mark.parametrize('str1, str2, str3',[('удали меня','у', 'дали меня'), ('delete me','ete', 'del me'), ('не удаляй','t', 'не удаляй'),('  ',' ', '')])
def test_delete_symbol(str1, str2, str3):
    s_utils = StringUtils()
    result = s_utils.delete_symbol(str1, str2)
    assert result == str3
    
    
@pytest.mark.positive_test      
@pytest.mark.parametrize('str1, str2, bool',[('удали меня','у', True), ('delete me','m', False), ('44 удаляй','4', True),('  ',' ', True), ('','', True)])
def test_starts_with(str1, str2, bool):
    s_utils = StringUtils()
    result = s_utils.starts_with(str1, str2)
    assert result == bool
    
    
@pytest.mark.positive_test      
@pytest.mark.parametrize('str1, str2, bool',[('удали меня','я', True), ('delete me','d', False), ('44 удаляй55','55', True),('  ',' ', True), ('','', True)])
def test_end_with(str1, str2, bool):
    s_utils = StringUtils()
    result = s_utils.end_with(str1, str2)
    assert result == bool
    
    
@pytest.mark.positive_test      
@pytest.mark.parametrize('str1, bool',[('удали меня', False), ('delete me', False), ('  ', True), ('', True)])
def test_is_empty(str1, bool):
    s_utils = StringUtils()
    result = s_utils.is_empty(str1)
    assert result == bool
    
    
@pytest.mark.positive_test      
@pytest.mark.parametrize('l_str, str1, str2',[([1,2,3],':', '1:2:3'), (['a','b','c'],',', 'a,b,c'), (['a','b','c'], '', 'abc'), ([' ',' '],':', ' : '), ('', '','')])
def test_list_to_string(l_str, str1, str2):
    s_utils = StringUtils()
    result = s_utils.list_to_string(l_str, str1)
    assert result == str2