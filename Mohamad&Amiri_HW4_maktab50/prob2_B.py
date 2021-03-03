scores = {'Art':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Math':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 1},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 2},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Literature':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 3},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 1},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 2}],
          'Physics':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4}],
          'Chemistry':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 2},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 3}]}
names = []
score = []
dic = {}


def make_dic(dic, key, value):
    if key not in dic:
        dic[key] = []
        dic[key].append(value)
    else:
        dic[key].append(value)
for i in scores:
    for j in range(len(scores[i])):
        temp = scores[i][j]['first_name'] + " " + scores[i][j]['last_name']
        make_dic(dic, temp, scores[i][j]['score'])
        if temp not in names:
            names.append(temp)
        
    

print(dic)