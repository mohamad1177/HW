class Product:
    def __init__(self, type_product, name, price):
        self.type_product = type_product
        self.name = name
        self.price =price
        

    def set_commisiongroups(self,commisiongroups):
        self.commisiongroups = commisiongroups
        
    def set_markup(self, lower_cost,upper_cost, lower_count):
        self.lower_cost = lower_cost
        self.upper_cost = upper_cost
        self.lower_count = lower_count

    def set_count(self, count):
        self.count = count

    def cal_markup(self):

        if self.count == 1:
            return self.upper_cost

        elif self.count > self.lower_count:
            return self.lower_cost
        else:
            return ((self.lower_cost - self.upper_cost) / (self.lower_count - 1))*(self.count - 1) + self.upper_cost


    def price_markup(self):
        return ((self.cal_markup()*self.price)/100 + self.price)*self.count


    def get_commisiongroups(self):
        return self.commisiongroups
    
        
        
        
shirts = Product("1", "shirts", 30)
shirts.set_commisiongroups(["A", "B"])
shirts.set_markup(10,20,10)


pants = Product("2", "pants", 50)
pants.set_commisiongroups(["A","C"])
pants.set_markup(15,20,10)


shoes = Product("3", "shoes", 80)
shoes.set_commisiongroups(["B"])
shoes.set_markup(10,15,5)


hat = Product("4", "hat", 20)
hat.set_commisiongroups([])
hat.set_markup(10,30,20)





shirts.set_count(5)

print(Product.cal_markup(shirts))

print(Product.price_markup(shirts))



#######problem2



class User:
    def __init__(self,userid, firstname, lastname):
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
            
    
    def set_discount(self, groups_name,cost,unit):
        self.groups_name = groups_name
        self.cost = cost
        self.unit = unit

    def get_discount(self):
        return {"groups_name":self.groups_name, "cost":self.cost, "unit":self.unit}
        

A = User(1001, "Mohsen","Bayat")
A.set_discount(["A","B","C"],[5,3,7],["percent","Doller","percent"])
B=User(1002,"Sobhan","Taghadosi")
B.set_discount(["A","C"],[5,7],["percent","percent"])
print(A.get_discount())    
    





    

        
##class Shirt(Product):
##    def __init__(self, type_product, name, price):
##        super().__init__(type_product="1", name = "shirt", price = 30)
##
##    
##    self.type_product = "1"
##    self.name = "shirt"
##    self.price = 30
##    self.commision_list = ["A", "B"]
##    self.lower_cost = 10
##    self.upper_cost = 20
##    self.lower_count = 10
##    
##
##    def set_count(self, count):
##        self.count = count
##
##    def get_type(self):
##        return self.type
##    
##class Pants(Product):
##    self.type_product = "2"
##    self.name = "pants"
##    self.price = 50
##    self.commision_list = ["A", "C"]
##    self.lower_cost = 15
##    self.upper_cost = 15
##    self.lower_count = 10
##
##    def set_count(self, count):
##        self.count = count
##
##    def get_type(self):
##        return self.type
##
##class Shoes(Product):
##    self.type_product = "3"
##    self.name = "shoes"
##    self.price = 80
##    self.lower_cost = 10
##    self.upper_cost = 15
##    self.lower_count = 5
##    
##    self.commision_list = ["B"]
##
##    def set_count(self, count):
##        self.count = count
##
##    def get_type(self):
##        return self.type
##
##
##class Hat(Product):
##    self.type_product = "4"
##    self.name = "har"
##    self.price = 20
##    self.unit = "Doller"
##    self.commision_list = []
##    self.lower_cost = 10
##    self.upper_cost = 30
##    self.lower_count = 20
##
##    def set_count(self, count):
##        self.count = count
##
##    def get_type(self):
##        return self.type


