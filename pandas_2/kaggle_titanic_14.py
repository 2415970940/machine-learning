import numpy as np
import pandas as pd

titanic_survival = pd.read_csv('train.csv')
# print(titanic_survival.head())
print(titanic_survival.shape)
age = titanic_survival['Age']
# print(age.loc[:10])
age_is_null = pd.isnull(age)
age_null_true = age[age_is_null]
# print(age_null_true)
age_null_count = len(age_null_true)
print(age_null_count)
# 平均年龄
good_ages = titanic_survival['Age'][age_is_null == False]
avg_age = sum(good_ages)/len(good_ages)
print(avg_age)
avg_age = titanic_survival['Age'].mean()
print(avg_age)

# 船舱等级，平均价格
pclasses = [1,2,3]
fare_by_class = {}
for pclass in pclasses:
    row_class = titanic_survival[titanic_survival["Pclass"]==pclass]
    class_avg = row_class["Fare"].mean()
    fare_by_class[pclass]=class_avg
print(fare_by_class)

fare_by_class = titanic_survival.pivot_table(index="Pclass",values="Fare",aggfunc=np.mean)
print(fare_by_class)

passenger_age = titanic_survival.pivot_table(index="Pclass",values="Age")
print(passenger_age)

# dropna去掉NAN
titanic_survival.dropna(axis=0,subset=['Age','Sex'])

#     df.loc[行标签,列标签]
#     df.loc['a':'b']#选取ab两行数据
#     df.loc[:,'one']#选取one列的数据
new_titanic_survival = titanic_survival.sort_values('Age',ascending=False)
print(new_titanic_survival.loc[:,['Age','Survived']])

#重新设计序列号
# new_titanic_survival.reset_index(drop=True)

# 调用函数
def not_null_count(column):
    column_null = pd.isnull(column)
    null_rows = column[column_null]
    return len(null_rows)

column_null_row = titanic_survival.apply(not_null_count)
# print(column_null_row)

def which_class(row):
    pclass = row['Pclass']
    if pd.isnull(pclass):
        return "UNKNOWN"
    elif pclass == 1:
        return "The First Class"
    elif pclass == 2:
        return "The Second Class"
    elif pclass == 3:
        return "The Third Class"

classes = titanic_survival.apply(which_class,axis=1)
# print(classes)

def age_classes(row):
    age_all = row['Age']
    if pd.isnull(age_all):
        return 'Unkown'
    elif age_all<18:
        return 'minor'
    else:
        return 'adult'

age_group_class = titanic_survival.apply(age_classes,axis=1)
# print(age_group_class)

titanic_survival['age_labels']=age_group_class
age_group_survival = titanic_survival.pivot_table(index='age_labels',values='Survived')
print(age_group_survival)