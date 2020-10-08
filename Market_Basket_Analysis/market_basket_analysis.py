# -*- coding: utf-8 -*-

import pandas as pd
from apyori import apriori


df = pd.read_csv('/home/anujkhaire/Documents/ICS/Market_Basket_Optimisation.csv',header=None)
df.fillna(0,inplace=True)

transactions = []
for i in range(0,len(df)):
    transactions.append([str(df.values[i,j]) for j in range(0,20) if str(df.values[i,j])!='0'])

rules = apriori(transactions,min_support=0.003,min_confidance=0.2,min_lift=3,min_length=2)
Results = list(rules)
df_results = pd.DataFrame(Results)

support = df_results.support

first_values = []
second_values = []
third_values = []
fourth_value = []

for i in range(df_results.shape[0]):
    single_list = df_results['ordered_statistics'][i][0]
    first_values.append(list(single_list[0]))
    second_values.append(list(single_list[1]))
    third_values.append(single_list[2])
    fourth_value.append(single_list[3])

lhs = pd.DataFrame(first_values)
rhs= pd.DataFrame(second_values)
confidance=pd.DataFrame(third_values,columns=['Confidance'])
lift=pd.DataFrame(fourth_value,columns=['lift'])

df_final = pd.concat([lhs,rhs,support,confidance,lift], axis=1)
df_final.fillna(value=' ', inplace=True)
df_final.columns = ['lhs',0,'rhs',1,2,'support','confidance','lift']
df_final['lhs'] = df_final['lhs']+str(", ")+df_final[1]+str(", ")
df_final.drop(columns=[0,1,2],inplace=True)

print(df_final)

