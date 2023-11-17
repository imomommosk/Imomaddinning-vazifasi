# import json
#
# x=10
# x_json=json.dumps(x)
#
# ism='imomaddin'
# ism_json = json.dumps(ism)
#
# sonlar=[45,98,25,10]
# sonlar_json=json.dumps(sonlar)
# print(sonlar_json)
# print(ism_json)
# print(x_json)
import json

# import json
#
# bemor={
#     "ism":"alijon Valiyev",
#     "yosh":30,
#     "oila":True,
#     "farzandlari":("axmad","bonu"),
#     "allegiya":None,
#     "dorilar":[
#         {'nomi':'Analgin','miqdori':0.5},
#         {'nomi':'panadol','miqdori':1.2},
#     ]
# }
# bemor_json=json.dumps(bemor, indent=4)
# print(bemor_json)

# import json
#
# bemor={
#     "ism":"alijon Valiyev",
#     "yosh":30,
#     "oila":True,
#     "farzandlari":("axmad","bonu"),
#     "allegiya":None,
#     "dorilar":[
#         {'nomi':'Analgin','miqdori':0.5},
#         {'nomi':'panadol','miqdori':1.2},
#     ]
# }
# with open('bemor.json','w') as f:
#     json.dump(bemor,f)
# import json
# fil = 'data.json'
# with open(fil) as f:
#     data=json.load(f)
#
# kenglik=data['geometry']['location']['lat']
# uzunlik=data['geometry']['location']['lat']
# print(f"{kenglik},{uzunlik}")


import json

data = {
    "Model" : "Malibu",
    "Rang" : "Qora",
    "Yil":2020,
    "Narh":40000
    }

data_json=json.dumps(data)
print(data_json)