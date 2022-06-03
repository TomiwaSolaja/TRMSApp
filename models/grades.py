class Grades:
    def __init__(self, letter, pass_fail):
        self.letter=letter
        self.pass_fail=pass_fail
    
    def __repr__(self):
        return str({
            'letter': self.letter,
            'pass_fail':self.pass_fail
        })