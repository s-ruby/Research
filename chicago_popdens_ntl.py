# -*- coding: utf-8 -*-
"""chicago_popDens_ntl.ipynb

Author: Serena Killion

Original file is located at
    https://colab.research.google.com/drive/1lzrwlD3Wl84XV8spmzZ8N-dKBGt5O_lk

#Comparing Mean Absolute Error of GWR and EBK as Predictors for Population Density in Chicago with NTL as Explanatory Variable (2017)

**Key:** 
*   Example: df1 represents January EBK Table
*   Example: dfg5 represents May GWR Table
"""

import pandas as pd
import numpy as np
ebk_mae = []
gwr_mae = []
#R2 values taken from ArcGIS GWR reports per month
gwr_r2 = [.6474, .6523, .6744, .6725, .6750, .6697, .6691, .6723, .6658, 0.6648, .6653, .6718]
difs = []

pop_count = [
0.4645,
0.4615,
0.4622,
0.4293,
0.4639,
0.4715,
0.4782,
0.4676,
0.4676,
0.4690,
0.4745,
0.4680]

d = []
total = 0
for x in range(len(gwr_r2)):
  y = gwr_r2[x] - pop_count[x]
  total += y
  d.append(y)

print(total/12)

def make_absolute(x):
  return abs(x)

"""#January"""

df1 = pd.read_excel('jan_ebk_d.xlsx')
total = df1['Error'].apply(make_absolute).sum()
ebk1_mae = total/len(df1)
#ebk_mae.append(ebk1_mae)
t = df1['StdError'].sum() / len(df1)
t2 = df1['Stdd_Error'].apply(make_absolute).sum() / len(df1)
print(t2)
print(ebk1_mae)
#df1.sort_values(by = 'Predicted')

df1_emp = pd.read_excel('01_ebk_emp.xlsx')
total = df1_emp['Error'].apply(make_absolute).sum()
ebk1_mae = total/len(df1_emp)
ebk_mae.append(ebk1_mae)
t = df1_emp['StdError'].sum() / len(df1_emp)
t2 = df1_emp['Stdd_Error'].apply(make_absolute).sum() / len(df1_emp)
print(t2)
print(ebk1_mae)
#df1.sort_values(by = 'Predicted')

df1_b = pd.read_excel('nugget.xlsx')
total = df1_b['Error'].apply(make_absolute).sum()
test = total/len(df1_b)
d = df1_b['Stdd_Error'].apply(make_absolute).sum() / len(df1_b)
print(d)
print(test)

dfg1 = pd.read_excel('jan_gwr.xlsx')
total = dfg1['RESIDUAL'].apply(make_absolute).sum()
gwr1_mae = total/len(dfg1)
gwr_mae.append(gwr1_mae)
print(gwr1_mae)
t3 = dfg1['STDRESID'].apply(make_absolute).sum() / len(dfg1)
print(t3)
dfg1.head()

dif1 = ebk1_mae-gwr1_mae
difs.append(dif1)
print(dif1)

"""#Feburary"""

df2 = pd.read_excel('ebk_feb.xlsx')
total = df2['Error'].apply(make_absolute).sum()
ebk2_mae = (total/len(df2))
#ebk_mae.append(ebk2_mae)
print(ebk2_mae)

df2_emp = pd.read_excel('02_ebk_emp.xlsx')
total = df2_emp['Error'].apply(make_absolute).sum()
ebk2_mae = (total/len(df2_emp))
ebk_mae.append(ebk2_mae)
print(ebk2_mae)

dfg2 = pd.read_excel('feb_gwr.xlsx')
total = dfg2['RESIDUAL'].apply(make_absolute).sum()
gwr2_mae = (total/len(dfg2))
gwr_mae.append(gwr2_mae)
print(gwr2_mae)

dif2 = ebk2_mae-gwr2_mae
difs.append(dif2)
print(dif2)

"""#March"""

df3 = pd.read_excel('ebk_mar.xlsx')
total = df3['Error'].apply(make_absolute).sum()
ebk3_mae = (total/len(df3))
#ebk_mae.append(ebk3_mae)
print(ebk3_mae)

df3_emp = pd.read_excel('03_ebk_emp.xlsx')
total = df3_emp['Error'].apply(make_absolute).sum()
ebk3_mae = (total/len(df3_emp))
ebk_mae.append(ebk3_mae)
print(ebk3_mae)

dfg3 = pd.read_excel('mar_gwr.xlsx')
total = dfg3['RESIDUAL'].apply(make_absolute).sum()
gwr3_mae = (total/len(dfg3))
gwr_mae.append(gwr3_mae)
print(gwr3_mae)

dif3 = ebk3_mae-gwr3_mae
difs.append(dif3)
print(dif3)

"""#April"""

df4 = pd.read_excel('ebk_apr.xlsx')
total = df4['Error'].apply(make_absolute).sum()
ebk4_mae = (total/len(df4))
#ebk_mae.append(ebk4_mae)
print(ebk4_mae)

df4_emp = pd.read_excel('03_ebk_emp.xlsx')
total = df4_emp['Error'].apply(make_absolute).sum()
ebk4_mae = (total/len(df4_emp))
ebk_mae.append(ebk4_mae)
print(ebk4_mae)

dfg4 = pd.read_excel('apr_gwr.xlsx')
total = dfg4['RESIDUAL'].apply(make_absolute).sum()
gwr4_mae = (total/len(dfg4))
gwr_mae.append(gwr4_mae)
print(gwr4_mae)

dif4 = ebk4_mae-gwr4_mae
difs.append(dif4)
print(dif4)

"""#May

Compute mean error after taking absolute value
"""

df5 = pd.read_excel('ebk_may.xlsx')
total = df5['Error'].apply(make_absolute).sum()
ebk5_mae = total/len(df5)
#ebk_mae.append(ebk5_mae)
print(ebk5_mae)

df5_emp = pd.read_excel('05_ebk_emp.xlsx')
total = df5_emp['Error'].apply(make_absolute).sum()
ebk5_mae = total/len(df5_emp)
ebk_mae.append(ebk5_mae)
print(ebk5_mae)

df5g = pd.read_excel('may_gwr.xlsx')
t = df5g['RESIDUAL'].apply(make_absolute).sum()
gwr5_mae = t/len(df5g)
gwr_mae.append(gwr5_mae)
print(gwr5_mae)

dif5 = ebk5_mae - gwr5_mae
difs.append(dif5)
print(dif5)

"""#June"""

df6 = pd.read_excel('ebk_jun.xlsx')
total = df6['Error'].apply(make_absolute).sum()
ebk6_mae = total/len(df6)
#ebk_mae.append(ebk6_mae)
print(ebk6_mae)

df6_emp = pd.read_excel('06_ebk_emp.xlsx')
total = df6_emp['Error'].apply(make_absolute).sum()
ebk6_mae = total/len(df6_emp)
ebk_mae.append(ebk6_mae)
print(ebk6_mae)

df6g = pd.read_excel('jun_gwr.xlsx')
t = df6g['RESIDUAL'].apply(make_absolute).sum()
gwr6_mae = t/len(df6g)
gwr_mae.append(gwr6_mae)
print(gwr6_mae)

dif6 = ebk6_mae - gwr6_mae
difs.append(dif6)
print(dif6)

"""#July"""

df7 = pd.read_excel('ebk_jul.xlsx')
ebk7_mae = (df7['Error'].apply(make_absolute).sum())/len(df7)
#ebk_mae.append(ebk7_mae)
print(ebk7_mae)

df7_emp = pd.read_excel('07_ebk_emp.xlsx')
ebk7_mae = (df7_emp['Error'].apply(make_absolute).sum())/len(df7_emp)
ebk_mae.append(ebk7_mae)
print(ebk7_mae)

df7g = pd.read_excel('jul_gwr.xlsx')
t = df7g['RESIDUAL'].apply(make_absolute).sum()
gwr7_mae = t/len(df7g)
gwr_mae.append(gwr7_mae)
print(gwr7_mae)

dif7 = ebk7_mae - gwr7_mae
difs.append(dif7)
print(dif7)

"""#August"""

df8 = pd.read_excel('ebk_aug.xlsx')
ebk8_mae = (df8['Error'].apply(make_absolute).sum())/len(df8)
#ebk_mae.append(ebk8_mae)
print(ebk8_mae)

df8_emp = pd.read_excel('08_ebk_emp.xlsx')
ebk8_mae = (df8_emp['Error'].apply(make_absolute).sum())/len(df8_emp)
ebk_mae.append(ebk8_mae)
print(ebk8_mae)

df8g = pd.read_excel('aug_gwr.xlsx')
t = df8g['RESIDUAL'].apply(make_absolute).sum()
gwr8_mae = t/len(df8g)
gwr_mae.append(gwr8_mae)
print(gwr8_mae)

dif8 = ebk8_mae - gwr8_mae
difs.append(dif8)
print(dif8)

"""#September"""

df9 = pd.read_excel('ebk_sep.xlsx')
ebk9_mae = (df9['Error'].apply(make_absolute).sum())/len(df9)
#ebk_mae.append(ebk9_mae)
print(ebk9_mae)
d = df9['Stdd_Error'].apply(make_absolute).sum() / len(df9)
print(d)

df9_emp = pd.read_excel('09_ebk_emp.xlsx')
ebk9_mae = (df9_emp['Error'].apply(make_absolute).sum())/len(df9_emp)
ebk_mae.append(ebk9_mae)
print(ebk9_mae)
d = df9_emp['Stdd_Error'].apply(make_absolute).sum() / len(df9_emp)
print(d)

df9g = pd.read_excel('sep_gwr.xlsx')
t = df9g['RESIDUAL'].apply(make_absolute).sum()
t3 = df9g['STDRESID'].apply(make_absolute).sum() / len(df9g)
print(t3)
gwr9_mae = t/len(df9g)
gwr_mae.append(gwr9_mae)
print(gwr9_mae)

#emp transformation with 500 simulations --> tendency toward mean
df1_ek = pd.read_excel('emp_cross_validation.xlsx')
total = df1_ek['Error'].apply(make_absolute).sum()
test = total/len(df1_ek)
d = df1_ek['Stdd_Error'].apply(make_absolute).sum() / len(df1_ek)
print(d)
print(test)

#emp transformation with 100 simulations 
df = pd.read_excel('emp_100_ebk.xlsx')
total = df['Error'].apply(make_absolute).sum()
test = total/len(df)
d = df['Stdd_Error'].apply(make_absolute).sum() / len(df)
print(d)
print(test)

dif9 = ebk9_mae - gwr9_mae
difs.append(dif9)
print(dif9)

"""#October"""

df10 = pd.read_excel('ebk_oct.xlsx')
ebk10_mae = (df9['Error'].apply(make_absolute).sum())/len(df10)
#ebk_mae.append(ebk10_mae)
print(ebk10_mae)

df10_emp = pd.read_excel('10_ebk_emp.xlsx')
ebk10_mae = (df10_emp['Error'].apply(make_absolute).sum())/len(df10_emp)
ebk_mae.append(ebk10_mae)
print(ebk10_mae)

df10g = pd.read_excel('oct_gwr.xlsx')
t = df10g['RESIDUAL'].apply(make_absolute).sum()
gwr10_mae = t/len(df10g)
gwr_mae.append(gwr10_mae)
print(gwr10_mae)

dif10 = ebk10_mae - gwr10_mae
difs.append(dif10)
print(dif10)

"""#November"""

df11 = pd.read_excel('ebk_nov.xlsx')
ebk11_mae = (df11['Error'].apply(make_absolute).sum())/len(df11)
#ebk_mae.append(ebk11_mae)
print(ebk11_mae)

df11_emp = pd.read_excel('11_ebk_emp.xlsx')
ebk11_mae = (df11_emp['Error'].apply(make_absolute).sum())/len(df11_emp)
ebk_mae.append(ebk11_mae)
print(ebk11_mae)

df11g = pd.read_excel('nov_gwr.xlsx')
t = df11g['RESIDUAL'].apply(make_absolute).sum()
gwr11_mae = t/len(df11g)
gwr_mae.append(gwr11_mae)
print(gwr11_mae)

dif11 = ebk11_mae - gwr11_mae
difs.append(dif11)
print(dif11)

"""#December"""

df12 = pd.read_excel('ebk_dec.xlsx')
ebk12_mae = (df12['Error'].apply(make_absolute).sum())/len(df12)
#ebk_mae.append(ebk12_mae)
print(ebk12_mae)

df12_emp = pd.read_excel('12_ebk_emp.xlsx')
ebk12_mae = (df12_emp['Error'].apply(make_absolute).sum())/len(df12_emp)
ebk_mae.append(ebk12_mae)
print(ebk12_mae)

df12g = pd.read_excel('dec_gwr.xlsx')
t = df12g['RESIDUAL'].apply(make_absolute).sum()
gwr12_mae = t/len(df11g)
gwr_mae.append(gwr12_mae)
print(gwr12_mae)

dif12 = ebk12_mae - gwr12_mae
difs.append(dif12)
print(dif12)

df12_p = pd.read_excel('pred_test2.xlsx')
df12_p.head()
gwr12_p_mae = (df12_p['Residual'].apply(make_absolute).sum())/len(df12_p)
ebk_mae.append(gwr12_p_mae)
print(gwr12_p_mae)

#dif_p_12 = gwr12_p_mae - gwr12_mae
#print(dif_p_12)

"""#Plot of EBK and GWR Predicted and Measured"""

#df12_p[['PREDICTED', 'MAX_17']].plot(figsize=(20,5))



df5[['Predicted', 'Measured']].plot(figsize=(20,5))

df5g[['PREDICTED', 'MAX_17']].plot(figsize=(20,5))

s = 0
for x in difs:
  s += x
print(s/12)

min_dif = np.argmin(difs)
min_ebk_mae = np.argmin(ebk_mae)
min_gwr_mae = np.argmin(gwr_mae)
max_gwr_r2 = np.argmax(gwr_r2)

def make_dict(d, sort):
  my_dict = {}
  month = 1
  for i in d:
    my_dict[month] = i
    month += 1
  if sort:
    my_dict = sorted(my_dict.items(), key=lambda kv: kv[1])
  else:
    my_dict = sorted(my_dict.items(), key=lambda kv: kv[1], reverse = True)
  return my_dict

dif_dict = make_dict(difs, True)
ebk_mae_dict = make_dict(ebk_mae, True)
gwr_mae_dict = make_dict(gwr_mae, True)
gwr_r2_dict = make_dict(gwr_r2, False)
print(dif_dict)
print(ebk_mae_dict)
print(gwr_mae_dict)
print(gwr_r2_dict)
pd.DataFrame.from_dict(dif_dict)

import statistics 
pop_count = [
0.4645,
0.4615,
0.4622,
0.4293,
0.4639,
0.4715,
0.4782,
0.4676,
0.4676,
0.4690,
0.4745,
0.4680
]

w = [.4680, .4645, .4615]

def season_avg(x, y, data):
  total  = 0
  for i in range(x, y):
    total += data[i]
  return total/3.0

spring = round(season_avg(2, 5, pop_count), 4)
summer = round(season_avg(5, 8, pop_count), 4)
fall = round(season_avg(8, 11, pop_count), 4)
winter = round(season_avg(0 ,3, w), 4)
print(spring, summer, fall, winter)
print(statistics.stdev(pop_count))

w2 = []
w2.append(gwr_r2[11])
w2.append(gwr_r2[0])
w2.append(gwr_r2[1])
spring = round(season_avg(2, 5, gwr_r2), 4)
summer = round(season_avg(5, 8, gwr_r2), 4)
fall = round(season_avg(8, 11, gwr_r2), 4)
winter = round(season_avg(0 ,3, w2), 4)
print(spring, summer, fall, winter)
print(statistics.stdev(gwr_r2))
