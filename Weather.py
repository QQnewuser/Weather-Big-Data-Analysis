import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
# 读取xlsx文件到DataFrame对象
df = pd.read_excel('city/'+'武汉'+ "近5年天气数据.xlsx")

# 统计某一列数据的权重
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
               '大雨':'heavy-rain',
               '浮尘':'dust',
               '中雨':'middle-rain',
               '小到中雨':'LTM-rain',
               '阵雪':'snower',
               '大到暴雨':'BTT-rain',
               '小到中雪':'LTM-snow',
               '中度霾':'middle-haze'
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

# 输出权重信息
for key, value in weights.items():
    print(f'{key}: {value}')

# 计算总权重
total_weight = sum(weights.values())

# 计算每项的占比
proportions = {key: value / total_weight for key, value in weights.items()}

# 设置颜色映射对象
cmap = plt.get_cmap('tab20')
colors = [cmap(i) for i in range(len(proportions))]

# 绘制饼图
plt.pie(proportions.values(), labels=proportions.keys(), colors=colors,textprops={'fontsize':8})
plt.axis('equal')


# 添加每个部分的名称和占比标签
labels = [f'{key}: {value * 100:.1f}%' for key, value in proportions.items()]
plt.text(-1.6, -1.2, '\n'.join(labels), fontsize=12)

# 获取当前坐标轴对象
ax = plt.gca()

# 构建文本标签所需的英文信息
translated_labels = [f'{translation.get(key, key)}: {value * 100:.1f}%' for key, value in proportions.items()]

# 添加文本标签显示占比信息和颜色对应关系
x0, y0 = ax.transAxes.transform((1, 1))  # 将坐标从图形坐标系转换为坐标轴坐标系
x, y = ax.transAxes.inverted().transform((x0, y0))  # 将右上角的点从坐标轴坐标系转换为图形坐标系
label = '\n'.join([f'{translated_labels[i]} ({colors[i]})' for i in range(len(translated_labels))])  # 要显示的文本
ax.text(x - 220, y - 240, label, fontsize=12, ha='left', va='center')  # 添加文本标签

plt.savefig('Weather/'+'武汉'+'.png')
plt.show()
