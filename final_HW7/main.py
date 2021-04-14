from Store import Store
from Product import Product
from User import User
from DiscountList import DiscountList
from pprint import pprint

if __name__ =="__main__":
    ##sorat hesab ra misazim
    store = Store(1002, "1",10)



    ##SAKHTAN USER HAYE SABT SHODE DAR YEK LIST DAR STORE
    a=User(1001, "Mohasen", "Bayat")
    b=User(1002, "Sobhan", "Taghadosi")
    c=User(1003, "Javad", "Jafari")
    d=User(1004, "Masoud", "Hosseini")
    store.add_user(a)
    store.add_user(b)
    store.add_user(c)
    store.add_user(d)
    

    ##SABT ANVA TAKHFIF DAR STORE
    A=DiscountList("A", 5, "percent", [1001, 1002, 1003, 1005])
    B=DiscountList("B", 3, "Doller", [1001, 1003, 1006])
    C=DiscountList("C", 7, "percent", [1001, 1002, 1004])
    store.add_discount(A)
    store.add_discount(B)
    store.add_discount(C)




    ##SABT MAHSOLAT KARKHANE DAR YEKLIST DAR STORE
    sh=Product("1", "shirt", 30, ["A", "B"])
    pa=Product("2", "pants", 50, ["A","C"])
    so=Product("3", "shoes", 80, ["B"])
    ha=Product("4", "hat", 20, [])
    store.add_product(sh)
    store.add_product(pa)
    store.add_product(so)
    store.add_product(ha)
    #markupinfo set
    sh.set_markupinfo(10, 20, 10)
    pa.set_markupinfo(15,20,10)
    so.set_markupinfo(10,15,5)
    ha.set_markupinfo(10,30,20)



    print(store.payment_info())
    
    


























    

    

    



    
