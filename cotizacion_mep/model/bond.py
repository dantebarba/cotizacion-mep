class Bond():
    def __init__(self, code, price, currency="ARS", volume=0, cantidad_operaciones=0, puntas=[], last_update=None):
        self.code = code
        self.currency = currency
        self.price = price
        self.last_update = last_update
        self.puntas = puntas
        self.cantidad_operaciones = int(cantidad_operaciones)
        self.volume = int(volume)

    def to_json(self):
        return self.__dict__
