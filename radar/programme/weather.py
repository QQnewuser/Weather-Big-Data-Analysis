import matplotlib.pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')



cities= [
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


weather_scores=[42.67399267399267,
36.08058608058608,
51.46520146520146,
79.04761904761905,
21.53846153846154,
3.8461538461538463,
100.0,
27.83882783882784,
11.20879120879121,
42.6007326007326,
72.05128205128204,
35.42124542124542,
9.963369963369964,
29.89010989010989,
70.43956043956044,
6.84981684981685,
10.659340659340659,
14.57875457875458,
31.208791208791208,
0.0]


num_cities = len(cities)

# 创建角度列表
angles = np.linspace(0, 2 * np.pi, num_cities, endpoint=False).tolist()
angles += angles[:1]  # 闭合雷达图


# 创建雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})


weather_scores += weather_scores[:1]  # 匹配角度数量
ax.fill(angles, weather_scores, 'b', alpha=0.5, label='Weather')


# 设置 x 轴刻度标签为城市名称
ax.set_xticks(angles[:-1])
ax.set_xticklabels(cities, fontsize=10,FontProperties=font)

# 隐藏 y 轴刻度标签
ax.set_yticklabels([])

# 添加标题
plt.title('城市天气得分', size=20, y=1.1,FontProperties=font)

# 添加图例
plt.legend(loc='upper right')

# 保存图像为 PNG 文件
plt.savefig('radar/weather_radar.png', dpi=300, bbox_inches='tight')




