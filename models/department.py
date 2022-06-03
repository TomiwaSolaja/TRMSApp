class Department:
    def __init__(self, d_id, dep_name, dep_head):
        self.d_id= d_id
        self.dep_name=dep_name
        self.dep_head=dep_head
    
    def __repr__(self):
        return str({
            'd_id': self.d_id,
            'dep_name': self.dep_name,
            'dep_head': self.dep_head
        })