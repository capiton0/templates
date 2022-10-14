import json
from unittest import result
import yaml

file = "banner.json"
with open(file) as fr:
    datas = json.load(fr)

result_rules = []

for data in datas:
    flag = 0
    rule = {
        "condition":"and"
    }
    name = data['name']
    rules = data['content_list']

    for rule in rules:
        if rule['method'] in ['length','url','mmh3','md5','code','header']:
            flag = 1
        
    
    if flag ==1 :
        continue
    # new_datas['name'] = name
    # new_datas['content_list'] = rules
    words = []
    for rule in rules:
        if rule['method'] == "body":
            words.append(rule['content'])
            result_rule = {
                "type":"word",
                "condition": "and",
                "name":name,
                "words":words
            }
            result_rules.append(result_rule)
        elif rule['method'] == "title":
            pass
    
    # elif 

    # else:
    #     print(name)

    # result_rules.append(result_rule)

results_data = {
    "id": "fingerprint-other1",
    "name": "ingerprint-other1",
    "requests": [
        {
            "method":"GET",
            "matchers": result_rules
        }
    ]
}

results = yaml.safe_dump(
        json.loads(
            json.dumps(results_data)
        )
    ,sort_keys=False,allow_unicode=True)

# 保存为文件
f = open(file+".yaml","w+")
f.write(results)
f.close()


