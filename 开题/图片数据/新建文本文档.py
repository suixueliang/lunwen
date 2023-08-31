import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#按街道名分类
# 读取CSV文件
data = pd.read_csv('F:/哈工大/硕士毕设/开题/图片数据/Parking_Violations_Issued_-_Fiscal_Year_2023.csv')
# 获取街道和门牌号的列数据
street_column = data['Street Name']
category_counts = street_column.value_counts()
top_50_categories = category_counts.head(50)
print(top_50_categories)
plt.bar(top_50_categories.index, top_50_categories.values)
# 设置图表标题和轴标签
plt.title('Category Counts')
plt.xlabel('Street Name')
plt.ylabel('Count')
# 自动调整X轴标签显示
plt.xticks(rotation=90)
# 显示图表
plt.show()