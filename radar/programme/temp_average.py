import matplotlib.pyplot as plt
import numpy as np

from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc')


# cities = ['WuHan','BeiJing','HangZhou','GuangZhou','HarBin','HuheHaote','KunMing','NanJing','FuZhou',
#         'HaiKou','HeFei','JiNan','NanChang','NanNing','ShenYang','TaiYuan','TianJin','XiNing','YinChuan','ChuangChun']
cities = ['武汉', '北京', '杭州', '广州', '哈尔滨', '呼和浩特', '昆明', '南京', '福州', '海口', '合肥', '济南', '南昌', '南宁', '沈阳', '太原', '天津', '西宁', '银川', '长春']


scores_high = [17.24576416984938, 41.896084151703164, 0, 30.36815829482076, 74.91817424322544, 82.39461236633191, 100, 27.39125348073263, 5.29540058896896, 28.039026097229907, 25.514176623393084, 32.217975114829684, 6.751535055907297, 23.681573702432573, 63.16240570908229, 56.31878766346933, 38.88018074384215, 90.76035346272022, 53.595717308026245, 77.07658142900777]
scores_diff = [74.86678781532018, 54.18322193817312, 85.68495189987783, 90.98024318709938, 56.22871770652594, 33.9585835874375, 53.7797353209926, 83.85403298391871, 89.29477110091273, 100, 76.01804225144848, 73.91642111819522, 94.56679089537069, 87.60040109102233, 38.16319476528304, 6.738123838564277, 76.80379736005449, 0, 33.364476066296376, 59.97303244662101]
scores_low = [69.50968871893642, 43.920826990253616, 77.15896391505929, 95.69188142209288, 0, 23.673277798049575, 82.71894321008834, 70.43817213642997, 95.22771176949547, 100, 68.31649289830922, 55.818276826498014, 81.94407950036125, 97.10725972012398, 17.826189558847307, 36.82169531338813, 53.689326029229754, 36.62406660777776, 36.6457343638023, 11.542717434668875]

#三个温度指标的比例，及相应平均分数的计算。默认等比例，可设置成用户自定义
r_high = 1
r_diff = 1
r_low = 1
average_scores = [(r_high*high + r_diff*diff + r_low*low) / (r_high+r_diff+r_low) for high, diff, low in zip(scores_high, scores_diff, scores_low)]




num_cities = len(cities)

# 创建角度列表
angles = np.linspace(0, 2 * np.pi, num_cities, endpoint=False).tolist()
angles += angles[:1]  # 闭合雷达图


# 创建雷达图
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'polar': True})


average_scores += average_scores[:1]  # 匹配角度数量
ax.fill(angles, average_scores, 'b', alpha=0.5, label='average score')


# 设置 x 轴刻度标签为城市名称
ax.set_xticks(angles[:-1])
ax.set_xticklabels(cities, fontsize=10,FontProperties=font)

# 隐藏 y 轴刻度标签
ax.set_yticklabels([])

# 添加标题
plt.title('城市气温平均得分', size=20, y=1.1,FontProperties=font)

# 添加图例
plt.legend(loc='upper right')

# 保存图像为 PNG 文件
plt.savefig('radar/temperature_average_radar.png', dpi=300, bbox_inches='tight')




