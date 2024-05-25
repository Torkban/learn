from sqlalchemy import create_engine 
import psycopg2



class employee_db:
          
    def __init__(self, db_connect_string) -> None:
        self.con = psycopg2.connect(db_connect_string)
        self.con.autocommit = True
    
    def new_company_id(self, name = 'Another_testing_SQL_company'):
        '''
        Создание новой компании и получение её id
        '''
        with self.con.cursor() as c:
            c.execute('INSERT INTO company (name) VALUES (%s)', (name,))
            c.execute('''select id from company c 
                    order by id desc
                    limit 1;''')
            all_users = c.fetchall()
        return all_users[0][0]
        
        
    def get_employee_by_id(self, em_id):
        '''
        Получение сотрудника по его id 
        '''
        with self.con.cursor() as c:
            c.execute('SELECT * FROM employee WHERE id = %s',(em_id,))
            emp = c.fetchall()
        return emp
  
    
    def get_employee_by_company_id(self, cm_id):
        '''
        Получение сотрудников компании
        '''
        with self.con.cursor() as c:
            c.execute('SELECT * FROM employee WHERE company_id = %s',(cm_id,))
            emp = c.fetchall()
        return emp

    def delete_employee_by_id(self, em_id):
        '''
        Удаление сотрудника по его id 
        '''
        with self.con.cursor() as c:
            c.execute('DELETE FROM employee WHERE id = %s',(em_id,))
            
    def delete_company_by_id(self, cm_id):
        '''
        Удаление компании по её id 
        '''
        with self.con.cursor() as c:
            c.execute('DELETE FROM company WHERE id = %s',(cm_id,))        
        



