import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"C:\Users\ZHZ\Downloads\SimHei.ttf")

plt.rcParams['font.sans-serif'] = [font.get_name()]  # 将默认字体设置为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
# 函数定义，读取文件并转换为DataFrame格式
def read_excel(file_name):
    data = pd.read_excel(file_name, sheet_name=0, header=0)

    # 处理MaxTemp和MinTemp，将其转换为数字格式
    data['zhishu'] = data['zhishu'].apply(lambda x: int(re.sub('[^-\\d]', '', str(x))))


    # 返回处理后的数据
    return data


city_list = ['武汉', '北京', '杭州', '广州', '哈尔滨', '呼和浩特', '昆明', '南京','福州','海口','合肥','济南','南昌','南宁','沈阳','太原','天津','西宁','银川','长春']
city_dict = {'武汉': 'wuhan', '北京': 'beijing', '杭州': 'hangzhou',
             '广州': 'guangzhou', '哈尔滨': 'haerbin', '呼和浩特': 'huhehaote',
             '昆明': 'kunming', '南京': 'nanjin','福州':'fuzhou','海口':'haikou','合肥':'hefei','济南':'jinan','南昌':'nanchang','南宁':'nanning','沈阳':'shenyang','太原':'taiyuan','天津':'tianjin','西宁':'xining','银川':'yinchuan','长春':'changchun'}

for city in city_list:
    file_name = "C:\\Users\\ZHZ\\Desktop\\天气 (1)\\天气\\" + city + "近5年天气数据.xlsx"
    data = read_excel(file_name)

    x = np.arange(1, len(data) + 1)
    y1 = data['zhishu'].values

    fig, ax = plt.subplots(figsize=(20, 10))

    # 生成柱形图
    colors = ['blue' if y < 50 else 'green' if y < 100 else 'yellow'if y < 200 else 'red' for y in y1]
    ax.bar(x, y1, color=colors, label='zhishu')

    # 隐藏横坐标刻度值
    plt.xticks([])

    # 添加图例和标题
    plt.legend(loc='upper right')
    plt.title(city_dict[city] + '2016-2020AQI', fontsize=20)

    # 保存图像
    plt.savefig(city_dict[city] + '.png')

    # 显示图形
    plt.show()

for city in city_list:
    # 假设data是一个pandas的DataFrame，其中包含AQI的数据
    categories = ['优', '良', '轻度污染', '中度污染','重度污染', '严重污染']
    colors = ['blue', 'green', 'yellow','orange','red', 'purple']

    # 创建一个字典，用于存储不同类别的AQI出现的次数
    counts = {}
    for i in range(len(categories)):
        counts[categories[i]] = 0

    # 计算不同类别的AQI出现的次数
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

    # 计算每个类别的占比
    total = len(data)
    percent = {}
    for i in range(len(categories)):
        percent[categories[i]] = counts[categories[i]] / total * 100

    # 创建一个饼状图，显示不同类别的AQI占比
    fig, ax = plt.subplots()
    ax.pie(percent.values(), labels=percent.keys(), colors=colors, autopct='%1.1f%%', startangle=90)
    ax.legend(loc='upper right')
    plt.axis('equal')  # 为了使饼图呈现圆形
    plt.title('Air Quality Index')
    plt.savefig(city_dict[city] + '_air_quality.png')
    plt.show()