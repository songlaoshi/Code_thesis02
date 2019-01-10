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

savepath=r"D:\Thesis2\data_processed\avignon"
filepath=r"D:\Thesis2\data\Avignon\Database db1\1 - SIF-EC"
# # -------------------------------------------------
# data=pd.read_table(filepath+"//AV2010db1.txt",encoding='utf-8')
# # 补全时间
# hour=np.arange(8,16,0.5)/24
# datestart=int(data.loc[0]['DOY'])
# dateend=int(data.loc[data.shape[0]-1]['DOY'])
# day=range(datestart,dateend+1)
# newdoy=np.ones((dateend-datestart+1)*len(hour))
# for i in range(0,len(newdoy),len(hour)):
#     newdoy[i:i+len(hour)]=day[int(i/len(hour))]+hour

# temp=pd.DataFrame(newdoy,columns=['newdoy'])
# new=pd.DataFrame(np.empty((temp.shape[0],data.shape[1])),columns=data.columns)
# new['DOY']=temp
# # print(new.index)
# count=0
# for i in range(temp.shape[0]):
#     if (abs(new.loc[i]['DOY']-data.loc[count]['DOY']))<1e-5:
#         print(i,count)
#         new.iloc[i,1:]=data.iloc[count,1:]
#         count=count+1
#     else:
#         new.iloc[i,1:]=np.nan
#     if count>data.shape[0]-1:
#         break
# #
# data=new
# print(data.shape)
# # 剔除SIF<0的值
# idx=data['SIF687']<0
# idx1=data['SIF687']>3
# data.loc[idx.values | idx1.values,'SIF687']=None
# idx=data['SIF760']<0
# idx1=data['SIF760']>3
# data.loc[idx.values | idx1.values,'SIF760']=None
# # 剔除GPP<0的值
# data.loc[data['GPP']<0,'GPP']=None
# print(data.shape)
# # # 时间筛选//剔除有雨的数据
# doy=data['DOY']
# for i in range(len(data.index)): # 
#     # doy 小数部分
#     t=math.modf(doy[i])[0]
#     #rain=data.loc[i]['Rain_North']
#     # print(rain)
#     if t<7.5/24 or t>18/24:
#         data.drop([i],inplace=True)
# print(data.shape)
# #修改删除行之后的index
# data.index=range(len(data.index))
# # 替换值NAN
# data.replace('NAN',np.nan,inplace=True)
# data.replace(-9999,np.nan,inplace=True)
# data.replace(0,np.nan,inplace=True)
# data['clear_index']=data['PAR2diff']/data['PAR2']
# # 保存剔除的结果
# data.to_csv(savepath+"/"+"AV2010db1_sifclean_8-18.csv",
#     header=True,index=False)

# # # # 求日平均
# data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_8-18.csv",encoding='utf-8')
# DOYnew=data['DOY']
# all1=[]
# daymean=[]
# for i in range(len(data.index)-1):
#     doy=np.fix(DOYnew[i])
#     doy1=np.fix(DOYnew[i+1])
#     if doy==doy1:
#         all1.append(data.loc[i].values)
#     else:
#         all1.append(data.loc[i].values)
#         # print(all1)
#         daymean.append(np.nanmean(all1,axis=0))
#         all1=[]
#     if i==len(data.index)-2:
#         all1.append(data.loc[i+1].values)
#         daymean.append(np.nanmean(all1,axis=0))

# daymean=pd.DataFrame(daymean,columns=data.columns)
# daymean['DOYnew']=[int(x) for x in daymean['DOY']]
# daymean.to_csv(savepath+"\\"+"AV2010db1_sifclean_daymean_8-18.csv",
#     header=True,index=False)
# print('writing ok')

## ================extract clear days data==========================
# load data
data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_8-18.csv",encoding='utf-8')
data1=data.copy()
idx=data['clear_index']<=0.5
data.loc[idx,1:]=np.nan
data.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_sunny.csv",
    header=True,index=False)
idx=~idx
data1.loc[idx,1:]=np.nan
data1.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_cloudy.csv",
    header=True,index=False)
data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_daymean_8-18.csv",encoding='utf-8')
data1=data.copy()
idx=data['clear_index']<=0.5
data.loc[idx,1:]=np.nan
data.to_csv(savepath+"\\"+"AV2010db1_sifclean_daymean_8-18_sunny.csv",
    header=True,index=False)
idx=~idx
data1.loc[idx,1:]=np.nan
data1.to_csv(savepath+"\\"+"AV2010db1_sifclean_daymean_8-18_cloudy.csv",
    header=True,index=False)

## --------------SIF，GPP和PAR的日变化----------------
data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_8-18_sunny.csv",encoding='utf-8')
print(data.shape)
# temp1=np.zeros((10,109,130))
temp=[]
daymean=[]
# count=1
for i in range(0,data.shape[0],16):
    # print(i)
    # temp1[:,:,count-1]=data.loc[i:i+9,:].values #和下面的效果一致
    # count=count+1
    temp.append(data.loc[i:i+15,:].values)
daymean=np.nanmean(temp,axis=0)
# daymean1=np.nanmean(temp1,axis=2)
daymean=pd.DataFrame(daymean,columns=data.columns)
daymean.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_onesunnyday.csv",
    header=True,index=False)

data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_8-18_cloudy.csv",encoding='utf-8')
temp=[]
daymean=[]
for i in range(0,data.shape[0],16):
    temp.append(data.loc[i:i+15,:].values)
daymean=np.nanmean(temp,axis=0)
daymean=pd.DataFrame(daymean,columns=data.columns)
daymean.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_onecloudyday.csv",
    header=True,index=False)