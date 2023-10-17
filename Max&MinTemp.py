import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re

# 函数定义，读取文件并转换为DataFrame格式
def read_excel(file_name):
    data = pd.read_excel(file_name, sheet_name=0, header=0)

    # 处理MaxTemp和MinTemp，将其转换为数字格式
    data['MaxTemp'] = data['MaxTemp'].apply(lambda x: int(re.sub('[^-\d]', '', str(x))))
    data['MinTemp'] = data['MinTemp'].apply(lambda x: int(re.sub('[^-\d]', '',str(x))))

    # 返回处理后的数据
    return data

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

for city in city_list:
    file_name = 'city/'+city + "近5年天气数据.xlsx"
    data = read_excel(file_name)

    # 绘制折线图
    x = np.arange(1, len(data)+1)
    y1 = data['MaxTemp'].values
    y2 = data['MinTemp'].values

    fig, ax = plt.subplots(figsize=(20, 10))

    ax.plot(x, y1, color='r', label='MaxTemp')
    ax.plot(x, y2, color='b', label='MinTemp')

    plt.xticks([]) # 隐藏横坐标刻度值

    # 添加图例和标题
    plt.legend(loc='upper right')
    plt.title(city_dict[city]+'2016-2020Max&MinTemp', fontsize=20)

    # 保存图像
    plt.savefig('Max&MinTemp/'+city+'.png')

    # 显示图形
    plt.show()
