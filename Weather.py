import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"SimHei.ttf")
plt.rcParams['font.sans-serif'] = [font.get_name()]  # 将默认字体设置为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

def read_excel(file_name):
    data = pd.read_excel(file_name, sheet_name=0, header=0)

    # 处理MaxTemp和MinTemp，将其转换为数字格式
    #data['Weather'] = data['Weather'].apply(lambda x: int(re.sub('[^-\\d]', '', str(x))))
    # 返回处理后的数据
    return data
city_list = ['呼和浩特', '武汉', '北京', '杭州', '广州', '哈尔滨', '昆明', '南京', '福州', '海口', '合肥', '济南',
             '南昌', '南宁', '沈阳', '太原', '天津', '西宁', '银川', '长春']
city_dict = {'武汉': 'wuhan', '北京': 'beijing', '杭州': 'hangzhou',
             '广州': 'guangzhou', '哈尔滨': 'haerbin', '呼和浩特': 'huhehaote',
             '昆明': 'kunming', '南京': 'nanjin', '福州': 'fuzhou', '海口': 'haikou', '合肥': 'hefei', '济南': 'jinan',
             '南昌': 'nanchang', '南宁': 'nanning', '沈阳': 'shenyang', '太原': 'taiyuan', '天津': 'tianjin',
             '西宁': 'xining', '银川': 'yinchuan', '长春': 'changchun'}
for city in city_list:
    # 读取xlsx文件到DataFrame对象
    file_name =  city + "近5年天气数据.xlsx"
    weights = {}
    data = read_excel(file_name)
    #df = pd.read_excel(city + '近5年天气数据.xlsx')
    #df = pd.read_excel(city + '近5年天气数据.xlsx', usecols=[4])
    translation = {
        '暴雨': 'rain',
        '小雨': 'rain',
        '雾': 'fog',
        '晴': 'sunny',
        '霾': 'haze',
        '多云': 'cloudy',
        '阴': 'cloudy',
        '阵雨': 'rain',
        '雷阵雨': 'rain',
        '雨夹雪': 'snow',
        '小雪': 'snow',
        '中雪': 'snow',
        '大雪': 'snow',
        '大雨': 'rain',
        '大暴雨': 'rain',
        '浮尘': 'haze',
        '中雨': 'rain',
        '小到中雨': 'rain',
        '阵雪': 'snow',
        '中到大雨': 'rain',
        '大到暴雨': 'rain',
        '小到中雪': 'snow',
        '中度霾': 'haze'
    }

    for item in data['Weather']:
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
    print(weights)
    categories = ['晴', '多云', '雨', '雪', '雾', '霾']
    colors = ['blue', 'green', 'yellow', 'orange', 'red', 'purple']

    fig, ax = plt.subplots()
    ax.pie(weights.values(), labels=weights.keys(), colors=colors, autopct='%1.1f%%', startangle=90)
    ax.legend(loc='upper right')
    plt.axis('equal')  # 为了使饼图呈现圆形
    plt.title(city + '天气分布')
    plt.savefig(city + '天气分布.png')
    plt.show()
