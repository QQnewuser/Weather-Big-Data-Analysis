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

#4种不同的情况
def split_list(list):
    list_1=[]
    list_2=[]
    list_3=[]
    list_4=[]
    for i in list:
        if i[0]>30 and i[1]<10:
            list_1.append(i)
        elif i[0]>30:
            list_2.append(i)
        elif i[1]<10:
            list_3.append(i)
        else:
            list_4.append(i)
    return list_1,list_2,list_3,list_4


def split_x(list):
    x=[]
    for i in list:
        x.append(i[3])
    return x

def split_diff(list):
    diff=[]
    for i in list:
        diff.append(i[2])
    return diff


city_list = ['呼和浩特', '武汉', '北京', '杭州', '广州', '哈尔滨', '昆明', '南京','福州','海口','合肥','济南','南昌','南宁','沈阳','太原','天津','西宁','银川','长春']
city_dict = {'呼和浩特': 'huhehaote','武汉': 'wuhan', '北京': 'beijing', '杭州': 'hangzhou', 
             '广州': 'guangzhou', '哈尔滨': 'haerbin',  
             '昆明': 'kunming', '南京': 'nanjin','福州':'fuzhou','海口':'haikou','合肥':'hefei','济南':'jinan','南昌':'nanchang','南宁':'nanning','沈阳':'shenyang','太原':'taiyuan','天津':'tianjin','西宁':'xining','银川':'yinchuan','长春':'changchun'}

for city in city_list:
    file_name =  'city/'+city + "近5年天气数据.xlsx"
    data = read_excel(file_name)
    
    # 绘制折线图
    y1 = data['MaxTemp'].values
    y2 = data['MinTemp'].values
    tempdiff=y1-y2

    #一个含三个数据的列表
    s=[]
    for i in range(len(data)):
        s.append([])
        s[i].append(y1[i])
        s[i].append(y2[i])
        s[i].append(tempdiff[i])
        s[i].append(0)
    
    #按温差排序
    s.sort(key  =  lambda  x:( int (x[ 2 ]),  int (x[ 1 ])))
    
    for i in range(len(s)):
        s[i][3]=i+1

    tempdiff_1,tempdiff_2,tempdiff_3,tempdiff_4=split_list(s)

    fig, ax = plt.subplots(figsize=(20, 10))

    #画图
    #ax.bar(split_x(tempdiff_1), split_diff(tempdiff_1), color='blue', label='ExtremeDifference')
    ax.bar(split_x(tempdiff_2), split_diff(tempdiff_2), color='red', label='Hot')
    ax.bar(split_x(tempdiff_3), split_diff(tempdiff_3), color='blue', label='Cold')
    ax.bar(split_x(tempdiff_4), split_diff(tempdiff_4), color='green', label='Normal')
   

    #画一条水平线
    plt.axhline(10,color="black")

    plt.xticks([]) # 隐藏横坐标刻度值

    # 添加图例和标题
    plt.legend(loc='upper left')
    plt.title(city_dict[city]+'2016-2020TempDif', fontsize=20)

    # 保存图像
    plt.savefig('TempDif/'+city+'.png')

    # 显示图形
    plt.show()
    
