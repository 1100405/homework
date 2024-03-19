import pandas as pd

df = pd.read_csv('data_with_classes.csv')
# print(df)

matclass1 = df[df['Class'] == 1]
del matclass1['Class']
matclass1 = matclass1.values
# matclass1 = matclass1.transpose()

matclass2 = df[df['Class'] == 2]
del matclass2['Class']
matclass2 = matclass2.values
# matclass2 = matclass2.transpose()

matclass3 = df[df['Class'] == 3]
del matclass3['Class']
matclass3 = matclass3.values
# matclass3 = matclass3.transpose()

print(matclass1)
print(matclass1.shape)
print()
print(matclass2)
print(matclass2.shape)
print()
print(matclass3)
print(matclass3.shape)