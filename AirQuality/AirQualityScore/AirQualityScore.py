import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# 函数定义，读取文件并转换为DataFrame格式
def read_excel(file_name):
    data = pd.read_excel(file_name, sheet_name=0, header=0)
    data['zhishu'] = data['zhishu'].apply(lambda x: int(re.sub('[^-\\d]', '', str(x))))
    return data.tail(365)


city_list = [
'武汉', 
'北京', 
'杭州', 
'广州', 
'哈尔滨', 
'呼和浩特', 
'昆明', 
'南京',
'长春',
'福州',
'海口',
'合肥',
'济南',
'南昌',
'南宁',
'沈阳',
'太原',
'天津',
'西宁',
'银川'
]
city_dict = {
'武汉': 'wuhan', 
'北京': 'beijing',
 '杭州': 'hangzhou', 
'广州': 'guangzhou', 
'哈尔滨': 'haerbin', 
'呼和浩特': 'huhehaote', 
'昆明': 'kunming', 
'南京': 'nanjin',
'长春':'changchun',
'福州':'fuzhou',
'海口':'haikou',
'合肥':'hefei',
'济南':'jinan',
'南昌':'nanchang',
'南宁':'nanning',
'沈阳':'shenyang',
'太原':'taiyuan',
'天津':'tianjin',
'西宁':'xining',
'银川':'yinchuan'
}
# 假设data是一个pandas的DataFrame，其中包含AQI的数据
categories = ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']
#colors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple']
scores = {}
city_score=[]
for city in city_list:
    data = read_excel('city/'+city+'近5年天气数据.xlsx')
    counts = {}
    for i in range(len(categories)):
        counts[categories[i]] = 0
    for aqi in data['zhishu']:
        if aqi >= 0 and aqi <= 50:
            counts['优'] += 1
        elif aqi > 50 and aqi <= 100:
            counts['良'] += 1
        elif aqi > 100 and aqi <= 150:
            counts['轻度污染'] += 1
        elif aqi > 150 and aqi <= 200:
            counts['中度污染'] += 1
        elif aqi > 200 and aqi <= 300:
            counts['重度污染'] += 1
        else:
            counts['严重污染'] += 1
    scores[city] = 0
    for category in counts:
        if category == '优':
            scores[city] += counts[category] * 5
        elif category == '良':
            scores[city] += counts[category] * 3
        elif category == '重度污染':
            scores[city] += counts[category] * -10
        elif category == '严重污染':
            scores[city] += counts[category] * -10
            # 对于其他类别，你可能想给它们一个默认的分数，例如0
        else:
            scores[city] += counts[category] * 0

    city_score.append(scores[city])
print(city_score)
# 获取最大值和最小值
min_score = min(city_score)
max_score = max(city_score)

# 定义变换函数
def transform_func(score, min_val, max_val):
    transformed_score = (score - min_val) / (max_val - min_val)*100  # 使用线性映射将score映射到[0, 1]区间
    return transformed_score

# 对每个score进行变换
transformed_scores = [transform_func(score, min_score, max_score) for score in city_score]
# 打开文件并写入数据
with open('AirQualityScore.txt', 'w') as file:
    for score in transformed_scores:
        file.write(str(score) + '\n')
