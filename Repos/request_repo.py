from abc import ABC, abstractmethod


class Requestrepo(ABC):

    @abstractmethod
    def create_request(self, request):
        pass

    @abstractmethod
    def get_request(self, req_id):
        pass
    
    @abstractmethod
    def all_requests(self, emp_id):
        pass

    @abstractmethod
    def update_request(self,change):
        pass
    
    @abstractmethod
    def delete_request(self,req_id):
        pass