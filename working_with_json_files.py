import json

# req_file="myjson.json"
#
# fo=open(req_file,'r')
#
# print(fo.read())
# fo.close()

my_dict={'Name':'narendra','skills':['Python','shell','yaml','AWS']}

req_file="myInfo.json"

fo=open(req_file,'w')
json.dump(my_dict,fo)



fo.close()