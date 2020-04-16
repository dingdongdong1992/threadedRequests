import json
import csv
i = 2
q = []
while i <= 200:
    try:
        file_name = 'pid_'+str(i)
        f = open(file_name,'r')
        data = json.load(f)
        q.append(data)
    except IOError:
        pass
    i+=1

new_list = []
#prod_id,prod_sku,prod_cat,prod_name
for g in q:
    new_dic = {}
    new_dic['prod_id'] = g['prod_id']
    new_dic['prod_sku'] = g['prod_sku']
    new_dic['prod_cat'] = g['prod_cat']
    new_dic['prod_name'] = g['prod_name']
    new_list.append(new_dic)


keys = new_list[0].keys()

with open('filtered_data.csv','w') as f:
    dict_writer = csv.DictWriter(f, fieldnames = keys)
    dict_writer.writeheader()
    dict_writer.writerows(new_dic)
