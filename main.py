import json
import pprint

with open("followers_1.json") as f:
    followers = json.load(f)

fol = []

for i in range(0,len(followers)):
    fol.append(followers[i]["string_list_data"][0]["value"])


with open("following.json") as file:
    following = json.load(file)
    list = following["relationships_following"]

folb = []

for i in range(0,len(list)):
    folb.append(list[i]['string_list_data'][0]['value'])


aset = set()
aset.update(fol)
bset = set()
bset.update(folb)
pprint.pp(bset-aset)


