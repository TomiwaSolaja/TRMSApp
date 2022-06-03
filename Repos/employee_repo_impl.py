from sqlite3 import Cursor
from employee_repo import Employeerepo
from util.db_connection import connection
from models.employee import Employee

class EmployeeRepoImpl(Employeerepo):
    def create_employee(self, employee):
        sql="INSERT INTO employees VALUES (%s, %s,%s, %s,%s) RETURNING *"
        cursor= connection.cursor()
        cursor.execute(sql,[employee.e_id, employee.fullname, employee.email, employee.password, employee.dep_id])
        connection.commit()
        record=cursor.fetchone()
        return Employee(e_id=record[0], fullname=record[1], email=record[2], password=record[3], dep_id=record[4])
    
    def get_employee(self, e_id):
        sql = "SELECT * FROM employees WHERE e_id= %s"
        cursor= connection.cursor()
        cursor.execute(sql, [e_id])
        record= cursor.fetchone()
        if record:
            return Employee(e_id=record[0], fullname=record[1], email=record[2], password=record[3], dep_id=record[4])
        else:
            raise print(f"client id not found {e_id}")
        return
    
    def all_employees(self):
        sql= "SELECT * FROM employees"
        cursor= connection.cursor()
        cursor.execute(sql)
        records=cursor.fetchall()
        employees=[]
        for record in records:
            employee= Employee(e_id=record[0], fullname=record[1], email=record[2], password=record[3], dep_id=record[4])
            employees.append(employee)
        return employees
    
    def update_employee(self, change):
        pass
    
    def delete_employee(self, e_id):
        sql = "DELETE FROM employees WHERE e_id=%s"

        cursor = connection.cursor()
        cursor.execute(sql, [e_id])
        connection.commit()

def test():
    x=EmployeeRepoImpl()
    la=Employee(e_id=6, fullname='Peter Quill', email='Pquill@elecmail.com', password='saavxs1', dep_id=1)
    x.create_employee(la)
    pet=x.get_employee(6)
    print(pet)
    