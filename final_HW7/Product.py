class Product:
    def __init__(self, type_prod, name, price, commission_group):
        self.type_prod = type_prod
        self.name = name
        self.price = price
        self.commission_group = commission_group

    def set_markupinfo(self, lower_cost, upper_cost, lower_count):
        self.lower_cost = lower_cost
        self.upper_cost = upper_cost
        self.lower_count = lower_count

    
    
        
