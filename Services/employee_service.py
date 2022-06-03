from Repos.employee_repo import Employeerepo

class EmployeeService:
    def __init__(self,employee_repo:Employeerepo):
        self.employee_repo=employee_repo
    
    def create_employee(self, employee):
        return self.employee_repo.create_employee(employee)

    def get_employee(self, e_id):
        return self.employee_repo.get_employee(e_id)
    
    def all_employees(self):
        return self.employee_repo.all_employees()

    def update_employee(self,change):
        return self.employee_repo.update_employee(change)
    
    def delete_employee(self,e_id):
        return self.employee_repo.delete_employee(e_id)