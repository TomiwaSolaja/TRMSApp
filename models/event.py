class Event:
    def __init__(self, event_type, percentage):
        self.event_type=event_type
        self.percentage=percentage
    
    def __repr__(self):
        return str({
            'event_type': self.event_type,
            'percentage': self.percentage
        })