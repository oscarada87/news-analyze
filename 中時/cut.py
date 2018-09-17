import json
import jieba
from pprint import pprint

# https://github.com/APCLab/jieba-tw

jieba.case_sensitive = True # 可控制對於詞彙中的英文部分是否為case sensitive, 預設False

with open ('./data/raw_news.json', 'r') as f:
    olddata = json.load(f)

# with open ('./data/cut_news.json', 'r') as f:
#     data = json.load(f)
data = []

def cut(data, num):
    seg_list = jieba.cut(olddata[num]['content'])
    # olddata[num]['cut_raw'] = seg_list
    olddata[num]['cut_string'] = "/".join(seg_list)
    data.append(olddata[num])
    print("{}/{} --- 完成".format(num + 1, 300))

# cut(data, 0)

for i in range(0, 300):
    cut(data, i)

with open ('./data/cut_news.json', 'w') as f:
    json.dump(data, f)
    # pprint(json.load(f))
