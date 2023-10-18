import matplotlib.pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')


# cities = ['WuHan','BeiJing','HangZhou','GuangZhou','HarBin','HuheHaote','KunMing','NanJing','FuZhou',
#         'HaiKou','HeFei','JiNan','NanChang','NanNing','ShenYang','TaiYuan','TianJin','XiNing','YinChuan','ChuangChun']
cities = ['武汉', '北京', '杭州', '广州', '哈尔滨', '呼和浩特', '昆明', '南京', '福州', '海口', '合肥', '济南', '南昌', '南宁', '沈阳', '太原', '天津', '西宁', '银川', '长春']

quality_scores=[52.573932092004384,
33.51588170865279,
67.57940854326397,
74.26067907995619,
27.92990142387733,
22.562979189485212,
85.76122672508215,
53.997809419496164,
33.29682365826944,
84.44687842278204,
100.0,
49.94523548740416,
0.0,
56.51697699890471,
80.72289156626506,
32.74917853231106,
0.43811610076670315,
8.762322015334064,
37.568455640744794,
29.46330777656079]


num_cities = len(cities)

# 创建角度列表
angles = np.linspace(0, 2 * np.pi, num_cities, endpoint=False).tolist()
angles += angles[:1]  # 闭合雷达图


# 创建雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})


quality_scores += quality_scores[:1]  # 匹配角度数量
ax.fill(angles, quality_scores, 'b', alpha=0.5, label='Air Quality')


# 设置 x 轴刻度标签为城市名称
ax.set_xticks(angles[:-1])
ax.set_xticklabels(cities, fontsize=10,FontProperties=font)

# 隐藏 y 轴刻度标签
ax.set_yticklabels([])

# 添加标题
plt.title('城市空气质量得分', size=20, y=1.1,FontProperties=font)

# 添加图例
plt.legend(loc='upper right')

# 保存图像为 PNG 文件
plt.savefig('radar/quality_radar.png', dpi=300, bbox_inches='tight')




