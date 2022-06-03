from abc import ABC, abstractmethod


class Employeerepo(ABC):

    @abstractmethod
    def create_employee(self, employee):
        pass

    @abstractmethod
    def get_employee(self, e_id):
        pass
    
    @abstractmethod
    def all_employees(self):
        pass

    @abstractmethod
    def update_employee(self,change):
        pass
    
    @abstractmethod
    def delete_employee(self,e_id):
        pass