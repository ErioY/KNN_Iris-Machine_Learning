'''
@Autor: ErioY
@Date: 2019-10-11 20:23:39
@Email: 1973545559@qq.com
@Github: https://github.com/ErioY
@LastEditors: ErioY
@LastEditTime: 2019-10-12 18:11:20
'''
import csv
import random
import math

# 读取文件
with open('Iris_Data.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]
# print(data)

# 把数据集分为训练集和测试集
random.shuffle(data)  # 打乱数据集顺序
test_data = data[0:30]  # 测试集取前30个
train_data = data[30:]  # 训练集取后120个


# 欧式距离法计算距离
def distance(one, two):
    res = 0
    list = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    for key in list:
        res += (float(one[key]) - float(two[key])) ** 2  # 训练集每一行数据的特征值分别与测试集计算距离并累加
    return math.sqrt(res)


# 主要操作
sum = 0  # 准确个数
s = input("请输入K的取值：")
K = int(s)
# K = 5
for i in test_data:
    species = i['species']  # 真实种类
    predict = ""
    res = [  # 遍历训练集的每一行，得出训练集每一行种类和一行测试集的距离
        {
            "train_species": trainData_perLine['species'],
            "distance": distance(i, trainData_perLine)
        }
        for trainData_perLine in train_data
    ]

    # 将列表依据距离进行升序
    res = sorted(res, key=lambda item: item['distance'])

    # 取前 K个距离最近的数据
    kSum = res[0:K]
    weight_sum = 0
    # 遍历前 K个数据，将他们的距离累加
    for i in kSum:
        weight_sum += i['distance']
    # 鸢尾花种类和权重
    result = {
        'Iris-setosa': 0,
        'Iris-versicolor': 0,
        'Iris-virginica': 0
    }
    # 遍历前 K个数据，计算每一个数据距离所占权重，存到 result中
    for i in kSum:
        result[i['train_species']] += 1 - i['distance'] / weight_sum

    # 判断哪个种类占的权重大，即将这个测试集归为此类
    if result['Iris-setosa'] > result['Iris-versicolor'] and result['Iris-setosa'] > result['Iris-virginica']:
        predict = 'Iris-setosa'
    if result['Iris-versicolor'] > result['Iris-setosa'] and result['Iris-versicolor'] > result['Iris-virginica']:
        predict = 'Iris-versicolor'
    if result['Iris-virginica'] > result['Iris-setosa'] and result['Iris-virginica'] > result['Iris-versicolor']:
        predict = 'Iris-virginica'

    # 判断真实种类和预测是否一致
    if species == predict:
        sum += 1  # 准确个数累加

# 计算准确率，保留小数点后两位小数
test_len = len(test_data)
print("准确率：{:.2f}%".format(100 * sum / test_len))
