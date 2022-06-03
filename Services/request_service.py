from Repos.request_repo import Requestrepo

class RequestService:
    def __init__(self, request_repo:Requestrepo):
        self.request_repo=request_repo
    
    def create_request(self, request):
        return self.request_repo.create_request(request)

    def get_request(self, req_id):
        return self.request_repo.get_request(req_id)
    
    def all_requests(self, emp_id):
        return self.request_repo.all_requests(emp_id)

    def update_request(self,change):
        return self.request_repo.update_request(change)
    
    def delete_request(self,req_id):
        return self.request_repo.delete_request(req_id)