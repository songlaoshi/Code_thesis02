#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time  : 18-12-11 下午9:52
#@Author: zhaohui li
#@File  : Code_spain_dataproce.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcs_lzh
from scipy.stats.stats import pearsonr
import math

filepath = r"D:\Thesis2\data\spain_grassland"
savepath=r"D:\Thesis2\data_processed\spain"
data = pd.read_csv(filepath + "//Majadas2017-Eddy_and_Flox.csv", encoding='utf-8')
# 剔除SIF<0的值
idx=data['SIF_A_ifld_mean']<0
idx1=data['SIF_A_ifld_mean']>2
data.loc[idx.values | idx1.values,'SIF_A_ifld_mean']=None
idx=data['SIF_A_sfm_mean']<0
idx1=data['SIF_A_sfm_mean']>2
data.loc[idx.values | idx1.values,'SIF_A_sfm_mean']=None
# 剔除GPP<0的值
data.loc[data['GPP_MR_f_Subcanopy']<0,'GPP_MR_f_Subcanopy']=None
# 时间筛选+剔除有雨的数据
doy=data['new_DOY']
for i in range(len(data.index)): # 
    # doy 小数部分
    t=math.modf(doy[i])[0]
    rain=data.loc[i]['Rain_North']
    # print(rain)
    if t<8/24 or t>18/24 or rain>0:
        data.drop([i],inplace=True)
# print(data.shape)
#修改删除行之后的index
data.index=range(len(data.index))

# # 去掉含有date格式数据的列，否则不能计算日平均
data=data.drop(['datetime_mean','rDate_Subcanopy','rDate_North',
    'rDate_Subcanopy_15','datetime_sd'],axis=1)
# print(data.shape)
# # 保存剔除的结果
data.to_csv(savepath+"/"+"Majadas2017-Eddy_and_Flox_droptime_sifclean_8-18_norain.csv",
    header=True,index=False)

# # 求日平均
DOYnew=data['new_DOY']
all1=[]
daymean=[]
for i in range(len(data.index)-1):
    doy=np.fix(DOYnew[i])
    doy1=np.fix(DOYnew[i+1])
    if doy==doy1:
        all1.append(data.loc[i].values)
    else:
        all1.append(data.loc[i].values)
        daymean.append(np.nanmean(all1,axis=0))
        all1=[]
    if i==len(data.index)-2:
        all1.append(data.loc[i+1].values)
        daymean.append(np.nanmean(all1,axis=0))
        # print(all1)
        # print(type(all1))

daymean=pd.DataFrame(daymean,columns=data.columns)
daymean['DOY']=[int(x) for x in daymean['new_DOY']]
daymean.to_csv(savepath+"\\"+"Majadas2017-Eddy_and_Flox_daymean_8-18_norain.csv",
    header=True,index=False)
print('writing ok')