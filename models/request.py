class Request:
    def __init__(self, req_id,req_type, cost, amount, grade, status, event_date, location, emp_id):
        self.req_id = req_id
        self.req_type = req_type
        self.cost = cost
        self.amount = amount
        self.grade = grade
        self.status = status
        self.event_date= event_date
        self.location= location
        self.emp_id = emp_id
    
    def __repr__(self):
        return str({
            'req_id' : self.req_id,
            'req_type': self.req_type,
            'cost': self.cost,
            'amount':self.amount,
            'grade':self.grade,
            'status':self.status,
            'event_date':self.event_date,
            'location':self.location,
            'emp_id':self.emp_id
        })