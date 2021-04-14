class Store:
    def __init__(self , userid, product, count):
        self.name = name
        self.product_list = product
        self.userid = userid
        self.discount_list = list()
        sef.count = count
        
    def add_discount(self, discount):
        self.discount_list.append(discount)

    def set_product(self , product):
        self.product = product

    def set_user(self, userid):
        self.userid = userid

    def cal_markup(self):
        
        if self.count == 1:
            return self.product.upper_cost

        elif self.product.count > self.product.lower_count:
            return self.product.lower_cost
        else:
            return ((self.product.lower_cost - self.product.upper_cost) / (self.product.lower_count - 1))*(self.product.count - 1) + self.product.upper_cost



    def payment_info(self):
        
        discount_dic = dict()
        
        for ele in self.product.commission_list:
            for i in range(3):
                if self.discount_list[i]==ele and userid in self.discount_list[i].users:
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
        user_dic["first_name"]= self.userid.first_name
        user_dic["lasr_name"]= self.userid.last_name

        final_dict=dict()
        final_dict["product_name"]= self.product.name
        final_dict["total_price"]= self.product.price + cal_markup(self)*self.produc.price/100*self.count

        if userid == 0:
            final_dict["total_with_commission"]="you arent sing up in our market and commission_groups=total_price",self.count*final_dict["total_price"]

            final_dict["discount"]="0"
            final_dict["user_name"]="you arent sing up in our market "

        else:
            final_dict["discount"] ={"Dollar":final_list[0],"percent":final_list[1]}
            final_dict["total_with_commission"] =(final_dict["total_price"]/self.count- max([final_list[0],((final_dict["total_price"]/self.count)*(final_list[1]))/100])*self.count
            final_dict["user_name"]=user_dic

    return final_dict
        
        
