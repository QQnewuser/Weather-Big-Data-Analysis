import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

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
city_score = []

# 循环处理每个城市
for city in city_list:
    # 读取xlsx文件到DataFrame对象
    df = pd.read_excel('city/'+city+'近5年天气数据.xlsx'.format(city))
    weights = {}
    translation = {
        '暴雨':'big-rain',
        '小雨': 'light-rain',
        '雾': 'fog',
        '晴':'sunny',
        '霾':'haze',
        '多云':'cloudy',
        '阴':'cloudy',
        '阵雨':'shower',
        '雷阵雨':'thunder-storm',
        '雨夹雪':'sleet',
        '小雪':'light-snow',
        '中雪':'middle-snow',
        '大雪':'big-snow',
        '大雨':'heavy-rain',
        '大暴雨':'heavy-rain',
        '浮尘':'dust',
        '中雨':'middle-rain',
        '小到中雨':'LTM-rain',
        '阵雪':'snower',
        '中到大雨':'BTT-rain',
        '大到暴雨':'BTT-rain',
        '小到中雪':'LTM-snow',
        '中度霾':'middle-haze'
    }
    transcore = {
        'big-rain':10,
        'light-rain':4,
        'fog':8,
        'sunny':-1,
        'haze':20,
        'cloudy':0,
        'shower':9,
        'thunder-storm':4,
        'sleet':5,
        'light-snow':1,
        'middle-snow':5,
        'big-snow':10,
        'heavy-rain':8,
        'dust':5,
        'middle-rain':6,
        'LTM-rain':5,
        'snower':4,
        'BTT-rain':10,
        'LTM-snow':3,
        'middle-haze':10
    }
    
    for item in df['Weather']:
        if '~' in item:
            start, end = item.split('~')
            weight = 0.5
            try:
                for value in range(int(start), int(end) + 1):
                    char = chr(value)  # 将Unicode编码转换为对应的汉字字符
                    translated_char = translation.get(char, char)  # 获取中文对应的英文翻译，若无则保持原字符
                    weights[translated_char] = weights.get(translated_char, 0) + weight
            except ValueError:
                pass
        else:
            translated_item = translation.get(item, item)  # 获取中文对应的英文翻译，若无则保持原字符
            weights[translated_item] = weights.get(translated_item, 0) + 1
    
    score = 0
    for key, value in weights.items():
        score += transcore[key] * value
    
    # 将score添加到city_score列表中
    city_score.append(score)
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
with open('WeatherScore.txt', 'w') as file:
    for score in transformed_scores:
        file.write(str(score) + '\n')

