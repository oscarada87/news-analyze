from pprint import pprint
import json

with open ('./data/cut_news.json', 'r') as f:
    data = json.load(f)

with open ('./data/statistics.json', 'r') as f:
    stat = json.load(f)

def count(data, num, stat):
    cut_string = data[num]['cut_string'].split('/')
    length = len(cut_string)
    for i in cut_string:
        if i in stat:
            stat[i] = stat[i] + 1
        else:
            stat[i] = 1
    print("{}/{} --- 完成".format(num+1, 300))

for i in range(0, 300):
    count(data, i, stat)

with open ('./data/statistics.json', 'w') as f:
    json.dump(stat, f)

# pprint(stat)
