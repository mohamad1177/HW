
product_list = [
       {
           "type": "1",
           "name": "shirt",
           "price": 30,
           "unit": "Dollar",
           "commission_groups": ["A", "B"]
       },
       {
           "type": "2",
           "name": "pants",
           "price": 50,
           "unit": "Dollar",
           "commission_groups": ["A", "C"]
       },
       {
           "type": "3",
           "name": "shoes",
           "price": 80,
           "unit": "Dollar",
           "commission_groups": ["B"]
       },
       {
           "type": "4",
           "name": "hat",
           "price": 20,
           "unit": "Dollar",
           "commission_groups": []
       }
]

markup_list = [
    {
        "product_type": "1",
        "lower_cost": 10,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "2",
        "lower_cost": 15,
        "upper_cost": 20,
        "unit": "percent",
        "lower_count": 10
    },
    {
        "product_type": "3",
        "lower_cost": 10,
        "upper_cost": 15,
        "unit": "percent",
        "lower_count": 5
    },
    {
        "product_type": "4",
        "lower_cost": 10,
        "upper_cost": 30,
        "unit": "percent",
        "lower_count": 20
    },
]

discount_list = [
    {
        "group_name": "A",
        "cost": 5,
        "unit": "percent",
        "users": [1001, 1002, 1003, 1005]
    },
    {
        "group_name": "B",
        "cost": 3,
        "unit": "Dollar",
        "users": [1001, 1003, 1006]
    },
    {
        "group_name": "C",
        "cost": 7,
        "unit": "percent",
        "users": [1001, 1002, 1004]
    }
]

user_list = [
    {
        "userid": 1001,
        "first_name": "Mohsen",
        "last_name": "Bayat",
    },
    {
        "userid": 1002,
        "first_name": "Sobhan",
        "last_name": "Taghadosi",
    },
    {
        "userid": 1003,
        "first_name": "Javad",
        "last_name": "Jafari",
    },
    {
        "userid": 1004,
        "first_name": "Masoud",
        "last_name": "Hosseini",
    },
    {
        "userid": 1005,
        "first_name": "Hassan",
        "last_name": "Zand",
    },
    {
        "userid": 1006,
        "first_name": "Ali",
        "last_name": "Ebadi",
    }
]


# prob1
product_type = int(input("Enter type of product"))
count = int(input("Enter number of product"))



def markup(product_type, count):
    lower_count=markup_list[product_type -1]["lower_count"]
    lower_cost=markup_list[product_type -1]["lower_cost"]
    upper_cost = markup_list[product_type - 1]["upper_cost"]
    #print(lower_count)
    #print(lower_cost)
    #print(upper_cost)

    if count == 1:
        return upper_cost

    elif count > lower_count:
        return lower_cost
    else:
        return ((lower_cost - upper_cost) / (lower_count - 1))*(count - 1) + upper_cost


print(markup(product_type, count))


# prob2

product_type=int(input("Enter product_type"))
userid_input=int(input("if you have a user id please enter else pleasr enter 0"))
count=int(input("enter number"))


def discount(commision_list, userid):
    discount_dic = dict()
    for ele in commision_list:
        for i in range(3):
            if discount_list[i]["group_name"]==ele and userid in discount_list[i]["users"]:
                discount_dic[discount_list[i]["cost"]]=discount_list[i]["unit"]

    percent_list=list()
    dollar_list=list()
    for ele in discount_dic:
        if discount_dic[ele]=='Dollar':
            dollar_list.append(ele)
        else:
            percent_list.append(ele)

    return [sum(dollar_list) , sum(percent_list)]


def name(id):
    user_dic=dict()
    for i in range(len(user_list)):
        if id==user_list[i]["userid"]:
            user_dic["first name"]=user_list[i]["first_name"]
            user_dic["last name"]=user_list[i]["last_name"]

    return user_dic


commission_groups = product_list[product_type - 1]["commission_groups"]


def calculate_product_price(product_type, count,userid=0):



    final_dict=dict()
    final_dict["product_name"]=product_list[product_type - 1]["name"]
    final_dict["total_price"]=(product_list[product_type - 1]["price"]+(markup(product_type, count)*product_list[product_type - 1]["price"])/100)*count

    if userid == 0:
        final_dict["total_with_commission"]="you arent sing up in our market and commission_groups=total_price",count*final_dict["total_price"]

        final_dict["discount"]="0"
        final_dict["user_name"]="you arent sing up in our market "

    else:
        final_dict["discount"] ={"Dollar":discount(commission_groups,userid)[0],"percent":discount(commission_groups,userid)[1]}
        final_dict["total_with_commission"] =(final_dict["total_price"]/count- max([discount(commission_groups, userid)[0],((final_dict["total_price"]/count)*(discount(commission_groups, userid)[1]))/100]))*count
        final_dict["user_name"]=name(userid)

    return final_dict


print(calculate_product_price(product_type, count, userid_input),(discount(commission_groups, userid_input)[0] ,(product_list[product_type - 1]["price"])*(discount(commission_groups, userid_input)[1])/100))






