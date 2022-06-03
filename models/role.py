class Role:
    def __init__(self, role_id, role):
        self.role_id = role_id
        self.role = role
    
    def __repr__(self):
        return str({
            'role_id': self.role_id,
            'role': self.role
        })