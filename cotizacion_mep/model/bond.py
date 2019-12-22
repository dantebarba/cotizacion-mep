class Bond():
    def __init__(self, code, price, currency="ARS", last_update=None):
        self.code = code
        self.currency = currency
        self.price = price
        self.last_update = last_update
        
    def to_json(self):
        return self.__dict__