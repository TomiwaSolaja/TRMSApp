import email


class Employee:
    def __init__(self, e_id, fullname, email, password, dep_id):
        self.e_id= e_id
        self.fullname= fullname
        self.email=email
        self.password=password
        self.dep_id=dep_id
    
    def __repr__(self):
        return str({
            'e_id':self.e_id,
            'fullname': self.fullname,
            'email': self.email,
            'password': self.password,
            'dep_id': self.dep_id

        })