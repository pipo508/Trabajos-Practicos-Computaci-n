class Items:
    def __init__(self, name, str, agi, con, cons):
        self.name = name
        self.str = str
        self.agi = agi
        self.con = con
        self.cons = cons

    def get_attrib(self):
        return self.name, self.str, self.agi, self.con, self.cons
