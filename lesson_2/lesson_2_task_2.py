def is_year_leap(year):
    if year % 4 == 0:
        return True
    else: return False
    
my_int_year = 1345   
is_year = is_year_leap(my_int_year)
print("год " + str(my_int_year) + ": " + str(is_year))