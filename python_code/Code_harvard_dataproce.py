#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-13 22:28:54
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcs_lzh
from scipy.stats.stats import pearsonr
# import scipy.io as scio
import h5py


ticklabelsize = 14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}

filepath = r"D:\Thesis2\data_processed\harvard"
savepath=filepath
# ## -----------------2013--------------------------
# data2013 = pd.ExcelFile(filepath + "\\USHa1_2013apar_sif_gpp_metho_hourly.xlsx")
# data2013=data2013.parse(sheet_name='Sheet1')

# # 提取出时间在8-18的数据并保存
# hour=data2013['hour']
# idx=(hour>=7.5/24).values & (hour<18/24).values
# data2013=data2013.loc[idx,:]
# data2013.index=range(len(data2013.index))
# # sif和GPP删选
# sif=data2013['SIF']
# idx=(sif>2.5).values | (sif<=0).values
# data2013.loc[idx,'SIF']=np.nan
# gpp=data2013[' GPP( umol/m2/s)']
# idx=(gpp>45).values | (gpp<=0).values
# data2013.loc[idx,' GPP( umol/m2/s)']=np.nan
# # 替换值NAN
# data2013.replace('NAN',np.nan,inplace=True)
# data2013.replace(-6999,np.nan,inplace=True)
# data2013.replace(-9999,np.nan,inplace=True)
# data2013.replace(0,np.nan,inplace=True)
# data2013['clear_index']=data2013['diffuse']/data2013['total']
# # 保存
# data2013.to_csv(savepath+"/"+"USHa1_2013apar_sif_gpp_metho_hourly_8-18.csv",
#     header=True,index=False)

# # # # 求日平均
# DOYnew=data2013['doy']
# all1=[]
# daymean=[]
# for i in range(len(data2013.index)-1):
#     doy=np.fix(DOYnew[i])
#     doy1=np.fix(DOYnew[i+1])
#     if doy==doy1:
#         all1.append(data2013.loc[i].values)
#     else:
#         all1.append(data2013.loc[i].values)
#         # print(all1)
#         daymean.append(np.nanmean(all1,axis=0))
#         all1=[]
#     if i==len(data2013.index)-2:
#         all1.append(data2013.loc[i+1].values)
#         daymean.append(np.nanmean(all1,axis=0))

# daymean=pd.DataFrame(daymean,columns=data2013.columns)
# daymean['DOYnew']=[int(x) for x in daymean['doy']]
# daymean.to_csv(savepath+"\\"+"USHa1_2013apar_sif_gpp_metho_daily_8-18.csv",
#     header=True,index=False)
# print('writing ok')
# # ## ----------------2014---------------------------
# data2013 = pd.ExcelFile(filepath + "\\USHa1_2014apar_sif_gpp_metho_hourly.xlsx")
# data2013=data2013.parse(sheet_name='Sheet1')

# # 提取出时间在8-18的数据并保存
# hour=data2013['hour']
# idx=(hour>=7.5/24).values & (hour<18/24).values
# data2013=data2013.loc[idx,:]
# data2013.index=range(len(data2013.index))
# # sif和GPP删选
# sif=data2013['SIF']
# idx=(sif>2.5).values | (sif<=0).values
# data2013.loc[idx,'SIF']=np.nan
# gpp=data2013[' GPP( umol/m2/s)']
# idx=(gpp>45).values | (gpp<=0).values
# data2013.loc[idx,' GPP( umol/m2/s)']=np.nan
# # 替换值NAN
# data2013.replace('NAN',np.nan,inplace=True)
# data2013.replace(-6999,np.nan,inplace=True)
# data2013.replace(-9999,np.nan,inplace=True)
# data2013.replace(0,np.nan,inplace=True)
# data2013['clear_index']=data2013['diffuse']/data2013['total']
# # 保存
# data2013.to_csv(savepath+"/"+"USHa1_2014apar_sif_gpp_metho_hourly_8-18.csv",
#     header=True,index=False)

# # # # 求日平均
# DOYnew=data2013['doy']
# all1=[]
# daymean=[]
# for i in range(len(data2013.index)-1):
#     doy=np.fix(DOYnew[i])
#     doy1=np.fix(DOYnew[i+1])
#     if doy==doy1:
#         all1.append(data2013.loc[i].values)
#     else:
#         all1.append(data2013.loc[i].values)
#         # print(all1)
#         daymean.append(np.nanmean(all1,axis=0))
#         all1=[]
#     if i==len(data2013.index)-2:
#         all1.append(data2013.loc[i+1].values)
#         daymean.append(np.nanmean(all1,axis=0))

# daymean=pd.DataFrame(daymean,columns=data2013.columns)
# daymean['DOYnew']=[int(x) for x in daymean['doy']]
# daymean.to_csv(savepath+"\\"+"USHa1_2014apar_sif_gpp_metho_daily_8-18.csv",
#     header=True,index=False)
# print('writing ok')

# ## ================extract clear days data==========================
# # load data
# # 2013
# data=pd.read_csv(savepath+"/"+"USHa1_2013apar_sif_gpp_metho_hourly_8-18.csv",encoding='utf-8')
# data1=data.copy()
# idx=data['clear_index']<=0.5
# data.loc[idx,5:]=np.nan
# data.to_csv(savepath+"\\"+"USHa1_2013apar_sif_gpp_metho_hourly_8-18_sunny.csv",
#     header=True,index=False)
# idx=~idx
# data1.loc[idx,5:]=np.nan
# data1.to_csv(savepath+"\\"+"USHa1_2013apar_sif_gpp_metho_hourly_8-18_cloudy.csv",
#     header=True,index=False)
# data=pd.read_csv(savepath+"/"+"USHa1_2013apar_sif_gpp_metho_daily_8-18.csv",encoding='utf-8')
# data1=data.copy()
# idx=data['clear_index']<=0.5
# data.loc[idx,5:]=np.nan
# data.to_csv(savepath+"\\"+"USHa1_2013apar_sif_gpp_metho_daily_8-18_sunny.csv",
#     header=True,index=False)
# idx=~idx
# data1.loc[idx,5:]=np.nan
# data1.to_csv(savepath+"\\"+"USHa1_2013apar_sif_gpp_metho_daily_8-18_cloudy.csv",
#     header=True,index=False)

# # 2014
# data=pd.read_csv(savepath+"/"+"USHa1_2014apar_sif_gpp_metho_hourly_8-18.csv",encoding='utf-8')
# data1=data.copy()
# idx=data['clear_index']<=0.5
# data.loc[idx,5:]=np.nan
# data.to_csv(savepath+"\\"+"USHa1_2014apar_sif_gpp_metho_hourly_8-18_sunny.csv",
#     header=True,index=False)
# idx=~idx
# data1.loc[idx,5:]=np.nan
# data1.to_csv(savepath+"\\"+"USHa1_2014apar_sif_gpp_metho_hourly_8-18_cloudy.csv",
#     header=True,index=False)
# data=pd.read_csv(savepath+"/"+"USHa1_2014apar_sif_gpp_metho_daily_8-18.csv",encoding='utf-8')
# data1=data.copy()
# idx=data['clear_index']<=0.5
# data.loc[idx,5:]=np.nan
# data.to_csv(savepath+"\\"+"USHa1_2014apar_sif_gpp_metho_daily_8-18_sunny.csv",
#     header=True,index=False)
# idx=~idx
# data1.loc[idx,5:]=np.nan
# data1.to_csv(savepath+"\\"+"USHa1_2014apar_sif_gpp_metho_daily_8-18_cloudy.csv",
#     header=True,index=False)

## --------------SIF，GPP和PAR的日变化----------------
# 2013
data=pd.read_csv(savepath+"/"+"USHa1_2013apar_sif_gpp_metho_hourly_8-18_sunny.csv",encoding='utf-8')
print(data.shape)
# temp1=np.zeros((10,109,130))
temp=[]
daymean=[]
# count=1
for i in range(0,data.shape[0],10):
    # print(i)
    # temp1[:,:,count-1]=data.loc[i:i+9,:].values #和下面的效果一致
    # count=count+1
    temp.append(data.loc[i:i+9,:].values)
daymean=np.nanmean(temp,axis=0)
# daymean1=np.nanmean(temp1,axis=2)
daymean=pd.DataFrame(daymean,columns=data.columns)
daymean.to_csv(savepath+"\\"+"USHa1_2013apar_sif_gpp_metho_8-18_onesunnyday.csv",
    header=True,index=False)

data=pd.read_csv(savepath+"/"+"USHa1_2013apar_sif_gpp_metho_hourly_8-18_cloudy.csv",encoding='utf-8')
temp=[]
daymean=[]
for i in range(0,data.shape[0],10):
    temp.append(data.loc[i:i+9,:].values)
daymean=np.nanmean(temp,axis=0)
daymean=pd.DataFrame(daymean,columns=data.columns)
daymean.to_csv(savepath+"\\"+"USHa1_2013apar_sif_gpp_metho_8-18_onecloudyday.csv",
    header=True,index=False)
# 2014
data=pd.read_csv(savepath+"/"+"USHa1_2014apar_sif_gpp_metho_hourly_8-18_sunny.csv",encoding='utf-8')
temp=[]
daymean=[]
for i in range(0,data.shape[0],10):
    temp.append(data.loc[i:i+9,:].values)
daymean=np.nanmean(temp,axis=0)
daymean=pd.DataFrame(daymean,columns=data.columns)
daymean.to_csv(savepath+"\\"+"USHa1_2014apar_sif_gpp_metho_8-18_onesunnyday.csv",
    header=True,index=False)
data=pd.read_csv(savepath+"/"+"USHa1_2014apar_sif_gpp_metho_hourly_8-18_cloudy.csv",encoding='utf-8')
temp=[]
daymean=[]
for i in range(0,data.shape[0],10):
    temp.append(data.loc[i:i+9,:].values)
daymean=np.nanmean(temp,axis=0)
daymean=pd.DataFrame(daymean,columns=data.columns)
daymean.to_csv(savepath+"\\"+"USHa1_2014apar_sif_gpp_metho_8-18_onecloudyday.csv",
    header=True,index=False)