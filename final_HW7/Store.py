class Store:
    def __init__(self , userid, product, count):
        
        self.product = product
        self.userid = userid
        self.discount_list = list()
        self.count = count
        self.user_list = list()
        self.productlist = list()

    def add_user(self, user):
        self.user_list.append(user)

    def add_product(self,product):
        self.productlist.append(product)
        
        
    def add_discount(self, discount):
        self.discount_list.append(discount)

    def get_prod2list(self):
        for prod in self.productlist:
            if self.product == prod.type_prod:
                return prod

    def get_user2userlist(self):
        for u in self.user_list:
            if self.userid == u.userid:
                return u

    def get_productlist(self):
        return self.productlist
    def get_user_list(self):
        return self.user_list

    

    def cal_markup(self):
        
        if self.count == 1:
            return self.get_prod2list().upper_cost

        elif self.count > self.get_prod2list().lower_count:
            return self.get_prod2list().lower_cost
        else:
            return ((self.get_prod2list().lower_cost - self.get_prod2list().upper_cost) / (self.get_prod2list().lower_count - 1))*(self.count - 1) + self.get_prod2list().upper_cost



    def payment_info(self):
        
        
        discount_dic = dict()
        
        for ele in self.get_prod2list().commission_group:
            for i in range(3):
                if self.discount_list[i].group_name ==ele and self.userid in self.discount_list[i].users:
                    discount_dic[self.discount_list[i].cost] = self.discount_list[i].unit

        percent_list=list()
        dollar_list=list()
        for ele in discount_dic:
            if discount_dic[ele]=='Dollar':
                dollar_list.append(ele)
            else:
                percent_list.append(ele)

        final_list=[sum(dollar_list) , sum(percent_list)]

        
        user_dic=dict()
        user_dic["first_name"]= self.get_user2userlist().first_name
        user_dic["lasr_name"]= self.get_user2userlist().last_name

        final_dict=dict()
        final_dict["product_name"]= self.get_prod2list().name
        final_dict["total_price"]= (self.get_prod2list().price + self.cal_markup()*self.get_prod2list().price/100)*self.count

        if self.userid == 0:
            final_dict["total_with_commission"]="you arent sing up in our market and commission_groups=total_price",self.count*final_dict["total_price"]

            final_dict["discount"]="0"
            final_dict["user_name"]="you arent sing up in our market "

        else:
            final_dict["discount"] ={"Dollar":final_list[0],"percent":final_list[1]}
            final_dict["total_with_commission"] =(final_dict["total_price"]/self.count- max([final_list[0],((final_dict["total_price"]/self.count)*(final_list[1]))/100]))*self.count
            final_dict["user_name"]=user_dic

        return final_dict
        
        
