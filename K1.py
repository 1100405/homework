import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dye.csv")

df_group = df.groupby('class')

array = [len(group) for _, group in df_group]

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

axes[0, 0].bar(range(1, 17), array, color='white', edgecolor='black')
axes[0, 0].set_title('Barplot for n class')
axes[0, 0].set_xlabel('Class')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_xticks(range(1, 17))

axes[0, 1].hist(df['c1'], color='white', bins=30, edgecolor='black')
axes[0, 1].set_title('Histogram of dye c1')
axes[0, 1].set_xlabel('c1')
axes[0, 1].set_ylabel('Frequency')

sns.boxplot(data=df[['c1', 'c2', 'c3']], color='white', ax=axes[1, 0])
axes[1, 0].set_title('Boxplot for c1, c2, and c3')
axes[1, 0].set_xlabel('Variable')
axes[1, 0].set_ylabel('Value')

sns.boxplot(x='class', y='c3', data=df, color='white', ax=axes[1, 1])
axes[1, 1].set_title('Boxplot of c3 for each class')
axes[1, 1].set_xlabel('Class')
axes[1, 1].set_ylabel('c3')

plt.tight_layout()
plt.show()
