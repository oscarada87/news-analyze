import json
import jieba

# https://github.com/APCLab/jieba-tw

jieba.case_sensitive = True # 可控制對於詞彙中的英文部分是否為case sensitive, 預設False

with open('news.json', 'r') as f:
    data = json.load(f)

seg_list = jieba.cut(data[1]['content'])
print("/".join(seg_list))
