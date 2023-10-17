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



city_list = ['武汉', '北京', '杭州', '广州', '哈尔滨', '呼和浩特', '昆明', '南京','福州','海口','合肥','济南','南昌','南宁','沈阳','太原','天津','西宁','银川','长春']
city_dict = {'武汉': 'wuhan', '北京': 'beijing', '杭州': 'hangzhou', 
             '广州': 'guangzhou', '哈尔滨': 'haerbin', '呼和浩特': 'huhehaote', 
             '昆明': 'kunming', '南京': 'nanjin','福州':'fuzhou','海口':'haikou','合肥':'hefei','济南':'jinan','南昌':'nanchang','南宁':'nanning','沈阳':'shenyang','太原':'taiyuan','天津':'tianjin','西宁':'xining','银川':'yinchuan','长春':'changchun'}
score=[]
tempdiff_square=[]
hightemp_ave=[]
lowtemp_ave=[]

for city in city_list:
    file_name = city + "近5年天气数据.xlsx"
    data = read_excel(file_name)
    
    # 绘制折线图
    y1 = data['MaxTemp'].values
    y2 = data['MinTemp'].values
    tempdiff=y1-y2

    #统计温差
    sum=0
    for i in tempdiff:
        sum=sum+i*i
    tempdiff_square.append(sum)

    #统计高温
    sum=0
    count=0
    for i in y1:
        if i>=30:
            sum=sum+i*i
            count=count+1
    hightemp_ave.append(sum/count)

    #统计低温
    sum=0
    count=0
    for i in y2:
        if i<=10:
            sum=sum+i
            count=count+1
    lowtemp_ave.append(sum/count)





#处理温差
tempdiff_max=max(tempdiff_square)
tempdiff_min=min(tempdiff_square)

for i in tempdiff_square:
    if i==tempdiff_max:
        score.append(0)
    elif i==tempdiff_min:
        score.append(100)
    else:
        score_count=(i-tempdiff_min)/(tempdiff_max-tempdiff_min)*100
        score.append(100-score_count)

f=open("diff.txt","w")
for line in score:
    f.write(str(line)+'\n')
f.close()

#处理高温
score=[]

hightemp_max=max(hightemp_ave)
hightemp_min=min(hightemp_ave)

for i in hightemp_ave:
    if i==hightemp_max:
        score.append(0)
    elif i==hightemp_min:
        score.append(100)
    else:
        score_count=(i-hightemp_min)/(hightemp_max-hightemp_min)*100
        score.append(100-score_count)
f=open("high.txt","w")
for line in score:
    f.write(str(line)+'\n')
f.close()

#处理低温
score=[]

lowtemp_max=max(lowtemp_ave)
lowtemp_min=min(lowtemp_ave)

for i in lowtemp_ave:
    if i==lowtemp_max:
        score.append(100)
    elif i==lowtemp_min:
        score.append(0)
    else:
        score_count=(i-lowtemp_min)/(lowtemp_max-lowtemp_min)*100
        score.append(score_count)
f=open("low.txt","w")
for line in score:
    f.write(str(line)+'\n')
f.close()



    
    








    
    
