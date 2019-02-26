#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 15:33:02
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcs_lzh
from scipy.stats.stats import pearsonr
import math
import VIs_calculation_func
import datetime

savepath = r"D:\Thesis2\data_processed\jurong"
filepath = r"D:\Thesis2\data\Jurong\Database-JR\1 - SIF-EC"
# # -------------------------------------------------
# # 把所有冠层辐射参数提取出来
# filecanopyra = r'D:\Thesis2\data\Jurong\Database-JR\2 - Canopy radiances'
# files = os.listdir(filecanopyra)
# SRAD = pd.read_table(filecanopyra + '/' + files[0])
# # print(SRAD.columns)
# namedict = {'Rad-Down': files[0][:-4] + '_' + 'Rad-Down', 'Rad-Up': files[0][
#     :-4] + '_' + 'Rad-Up', 'Reflectance': files[0][:-4] + '_' + 'Reflectance'}
# SRAD.rename(columns=namedict, inplace=True)
# # print(SRAD.columns)
# for file in files[1:]:
#     srad=pd.read_table(filecanopyra+'/'+file)
#     srad=srad.iloc[:,1:]
#     namedict = {'Rad-Down': file[:-4] + '_' + 'Rad-Down', 'Rad-Up': file[
#     :-4] + '_' + 'Rad-Up', 'Reflectance': file[:-4] + '_' + 'Reflectance'}
#     srad.rename(columns=namedict,inplace=True)
#     SRAD=pd.concat([SRAD,srad],axis=1)
# # print(SRAD.shape)
# # sif& GPP data
# data=pd.ExcelFile(filepath+"//2016db_JR.xlsx")
# data=data.parse('data')
# print(data.shape)
# # # 剔除有雨的数据
# data.replace('*',1,inplace=True)
# data.replace('NAN',1,inplace=True)
# # print(data['日降水量(mm)']==np.nan)
# idxvalue=list(map(int,data['日降水量(mm)']))
# idx=pd.DataFrame(idxvalue,columns=['idxvalue'])
# data.loc[idx['idxvalue']>0,'日降水量(mm)']=None
# # # 补全时间
# hour=np.arange(7,17.5,0.5)/24  # [7：00-17:30)
# datestart=int(data.loc[0]['DOY'])
# dateend=int(data.loc[data.shape[0]-1]['DOY'])
# day=range(datestart,dateend+1)
# newdoy=np.ones((dateend-datestart+1)*len(hour))
# for i in range(0,len(newdoy),len(hour)):
#     newdoy[i:i+len(hour)]=day[int(i/len(hour))]+hour
# # SIF&GPP补全时间
# temp=pd.DataFrame(newdoy,columns=['newdoy'])
# new=pd.DataFrame(np.empty((temp.shape[0],data.shape[1])),columns=data.columns)
# new['DOY']=temp
# # print(new.index)
# count=0
# for i in range(temp.shape[0]):
#     if (abs(new.loc[i]['DOY']-data.loc[count]['DOY']))<1e-5:
#         # print(i,count)
#         new.iloc[i,1:]=data.iloc[count,1:]
#         count=count+1
#     else:
#         new.iloc[i,1:]=np.nan
#     if count>data.shape[0]-1:
#         break
# # canopy Ra and ref 补全时间
# new1=pd.DataFrame(np.empty((temp.shape[0],SRAD.shape[1])),columns=SRAD.columns)
# new1['DOY']=temp
# count=0
# for i in range(temp.shape[0]):
#     if (abs(new1.loc[i]['DOY']-SRAD.loc[count]['DOY']))<1e-5:
#         # print(i,count)
#         new1.iloc[i,1:]=SRAD.iloc[count,1:]
#         count=count+1
#     else:
#         new1.iloc[i,1:]=np.nan
#     if count>SRAD.shape[0]-1:
#         print(count)
#         break
# #去掉new1中最后的DOY列
# data=pd.concat([new,new1.iloc[:,1:]],axis=1)
# print(data.shape)
# # 剔除SIF<0的值
# idx=data['SIF760']<0
# idx1=data['SIF760']>3
# data.loc[idx.values | idx1.values,'SIF760']=None
# # 剔除GPP<0的值
# data.loc[data['GPP(umol CO2 m-2 s-1)']<0,'GPP(umol CO2 m-2 s-1)']=None
# print(data.shape)
# #时间筛选
# doy=data['DOY']
# for i in range(len(data.index)): #
#     # doy 小数部分
#     t=math.modf(doy[i])[0]
#     if t<7.5/24 or t>18/24:
#         data.drop([i],inplace=True)
# print(data.shape)
# #修改删除行之后的index
# data.index=range(len(data.index))
# # 替换值NAN
# data.replace('NAN',np.nan,inplace=True)
# data.replace(-9999,np.nan,inplace=True)
# # data.replace(0,np.nan,inplace=True) # 降雨数据为0的不能去掉
# # data['clear_index']=data['PAR2diff']/data['PAR2'] # 没有PARdiff
# # 保存剔除的结果
# data.to_csv(savepath+"/"+"jurong2016_sifclean_8-18_ref_norain.csv",
#     header=True,index=False)

# # # # -------------------求日平均--------------------------------
# data=pd.read_csv(savepath+"/"+"jurong2016_sifclean_8-18_ref_norain.csv",encoding='utf-8')
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
# daymean.to_csv(savepath+"\\"+"jurong2016_sifclean_daymean_8-18_ref_norain.csv",
#     header=True,index=False)
# print('writing ok')

# ## ================extract clear days data==========================
# # load data
# data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_8-18_ref.csv",encoding='utf-8')
# data1=data.copy()
# idx=data['clear_index']<=0.5
# data.loc[idx,1:]=np.nan
# data.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_sunny_ref.csv",
#     header=True,index=False)
# idx=~idx
# data1.loc[idx,1:]=np.nan
# data1.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_cloudy_ref.csv",
#     header=True,index=False)
# data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_daymean_8-18_ref.csv",encoding='utf-8')
# data1=data.copy()
# idx=data['clear_index']<=0.5
# data.loc[idx,1:]=np.nan
# data.to_csv(savepath+"\\"+"AV2010db1_sifclean_daymean_8-18_sunny_ref.csv",
#     header=True,index=False)
# idx=~idx
# data1.loc[idx,1:]=np.nan
# data1.to_csv(savepath+"\\"+"AV2010db1_sifclean_daymean_8-18_cloudy_ref.csv",
#     header=True,index=False)

# ## --------------SIF，GPP和PAR的日变化----------------
# data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_8-18_sunny_ref.csv",encoding='utf-8')
# print(data.shape)
# # temp1=np.zeros((10,109,130))
# temp=[]
# daymean=[]
# # count=1
# for i in range(0,data.shape[0],18):
#     # print(i)
#     # temp1[:,:,count-1]=data.loc[i:i+9,:].values #和下面的效果一致
#     # count=count+1
#     temp.append(data.loc[i:i+17,:].values)
# daymean=np.nanmean(temp,axis=0)
# # daymean1=np.nanmean(temp1,axis=2)
# daymean=pd.DataFrame(daymean,columns=data.columns)
# daymean.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_onesunnyday_ref.csv",
#     header=True,index=False)

# data=pd.read_csv(savepath+"/"+"AV2010db1_sifclean_8-18_cloudy_ref.csv",encoding='utf-8')
# temp=[]
# daymean=[]
# for i in range(0,data.shape[0],18):
#     temp.append(data.loc[i:i+17,:].values)
# daymean=np.nanmean(temp,axis=0)
# daymean=pd.DataFrame(daymean,columns=data.columns)
# daymean.to_csv(savepath+"\\"+"AV2010db1_sifclean_8-18_onecloudyday_ref.csv",
#     header=True,index=False)


# ==============2017&2018年句容=======================
# 2017年句容由于通量数据缺失较多，不用于分析
# functions
def get_matlab2py_doy(mattime):
    '''
    把matlab格式datenum时间转换成doy
    只能转换一个值，数组的话用map吧
    '''
    python_datetime = datetime.datetime.fromordinal(
        int(mattime) - 366) + datetime.timedelta(days=mattime % 1)
    doy = python_datetime.timetuple().tm_yday + mattime % 1
    return doy

## ---------2017-------------
savepath1=r'D:\Data\jurong\jur\Results'
# dataref=pd.ExcelFile(r'D:\Data\jurong\jur\Results\halfhour_9_16_reflectance.xlsx')
# dataref=dataref.parse(0)
# wl=dataref.columns[1:].values
# ref=dataref.iloc[:,1:]
# #
# datara=pd.ExcelFile(r'D:\Data\jurong\jur\Results\halfhour_9_16_radiance.xlsx')
# datara=datara.parse(0)
# radiance=datara.iloc[:,1:]
# #
# doy=dataref['DOY']
# hour=(doy%1)*24
# setup=VIs_calculation_func.get_vegetation_indices(wl,ref,radiance)
# columns=['doy','hour','NDVI','EVI','MTCI','MTVI2'
#     ,'PRI','greenNDVI','rededgeNDVI','CIgreen','CVI','SR','ref_blue',
#     'ref_green','ref_red','ref_nir','ref_rededge','radiance_blue',
#     'radiance_green','radiance_red','radiance_nir','radiance_rededge']
#
# savedata=pd.DataFrame((np.vstack([doy,hour,setup.NDVI,setup.EVI,
#     	setup.MTCI,setup.MTVI2,setup.PRI,setup.greenNDVI,setup.rededgeNDVI,
#         setup.CIgreen,setup.CVI,setup.SR,setup.Rblue,setup.Rgreen,setup.Rred,
#         setup.Rnir,setup.Rrededge,setup.Ra_blue,setup.Ra_green,setup.Ra_red,
#         setup.Ra_nir,setup.Ra_rededge]).T),columns=columns)
# savedata.to_csv(savepath1+'/VI_ref_addMTVI2_halfhourlymean_2017.csv',index=False,header=True)

# get SIF
# sif=pd.ExcelFile(r'D:\Data\jurong\jur\Results\Jurong_2017_SIF_Half_hour.xlsx')
# sif=sif.parse(0)
# doy=sif['DOY']
# time=list(map(int,doy))
# idx=((doy-time)>8.6/24) & ((doy-time)<16.1/24)
# newdata=pd.concat([sif.loc[idx,'DOY'],sif.loc[idx,'3FLD'],sif.loc[idx,'iFLD'],sif.loc[idx,'SFMlinear']],axis=1)
# newdata.index=range(len(newdata))
# newdata.to_csv(savepath1+'/Jurong_2017_SIF_Half_hour_extract.csv',index=False,header=True)
# # # link sif&vi&radiance
# datasif = pd.read_csv(savepath1 + '/Jurong_2017_SIF_Half_hour_extract.csv')
# print(datasif.shape)
# datavi = pd.read_csv(savepath1 + '/VI_ref_addMTVI2_halfhourlymean_2017.csv')
# print(datavi.shape)
# # 把所有冠层辐射参数提取出来
# filecanopyra = r'D:\Thesis2\data_processed\Database REF\WalRefhalfhour_9-16_jr2017rice'
# files = os.listdir(filecanopyra)
# SRAD = pd.read_table(filecanopyra + '/' + files[0])
# # print(SRAD.columns)
# namedict = {'Rad-Down': files[0][:-4] + '_' + 'Rad-Down', 'Rad-up': files[0][
#     :-4] + '_' + 'Rad-Up', 'Reflectance': files[0][:-4] + '_' + 'Reflectance'}
# SRAD.rename(columns=namedict, inplace=True)
# # print(SRAD.columns)
# for file in files[1:]:
#     srad=pd.read_table(filecanopyra+'/'+file)
#     srad=srad.iloc[:,1:]
#     namedict = {'Rad-Down': file[:-4] + '_' + 'Rad-Down', 'Rad-up': file[
#     :-4] + '_' + 'Rad-Up', 'Reflectance': file[:-4] + '_' + 'Reflectance'}
#     srad.rename(columns=namedict,inplace=True)
#     SRAD=pd.concat([SRAD,srad],axis=1)
# dataall=pd.concat([datasif,datavi.iloc[:,2:],SRAD.iloc[:,1:]],axis=1)
# dataall.to_csv(savepath1+'\SIF_vi_ref_radiance_jurong2017.csv',index=False,header=True)

## ---------2018-------------
# ----------------get ref & VIs & radiance-------------
savepath = r'D:\Data2018\jr2018\Results'
# get_vis_addMTVI2
# dataref=pd.ExcelFile(r'D:\Data2018\jr2018\Results\halfhour_9_16_reflectance.xlsx')
# dataref=dataref.parse(0)
# wl=dataref.columns[1:].values
# ref=dataref.iloc[:,1:]
# #
# datara=pd.ExcelFile(r'D:\Data2018\jr2018\Results\halfhour_9_16_radiance.xlsx')
# datara=datara.parse(0)
# radiance=datara.iloc[:,1:]
# # 
# doy=dataref['DOY']
# hour=(doy%1)*24
# setup=VIs_calculation_func.get_vegetation_indices(wl,ref,radiance)
# columns=['doy','hour','NDVI','EVI','MTCI','MTVI2'
#     ,'PRI','greenNDVI','rededgeNDVI','CIgreen','CVI','SR','ref_blue',
#     'ref_green','ref_red','ref_nir','ref_rededge','radiance_blue',
#     'radiance_green','radiance_red','radiance_nir','radiance_rededge']

# savedata=pd.DataFrame((np.vstack([doy,hour,setup.NDVI,setup.EVI,
#     	setup.MTCI,setup.MTVI2,setup.PRI,setup.greenNDVI,setup.rededgeNDVI,
#         setup.CIgreen,setup.CVI,setup.SR,setup.Rblue,setup.Rgreen,setup.Rred,
#         setup.Rnir,setup.Rrededge,setup.Ra_blue,setup.Ra_green,setup.Ra_red,
#         setup.Ra_nir,setup.Ra_rededge]).T),columns=columns)
# savedata.to_csv(savepath+'/VI_ref_addMTVI2_halfhourlymean.csv',index=False,header=True)

# get SIF
# filepath=r'D:\Data2018\jr2018\Results\SIF day'
# filesifs=os.listdir(filepath)
# for filesif in filesifs:
# 	data=pd.ExcelFile(filepath+'/'+filesif)
# 	data=data.parse(0)
# 	# 只选取 3fLD，ifld和SFM_lin方法
# 	newdata=pd.concat([data['3FLD'],data['iFLD'],data['SFM_lin']],axis=1)
# 	mattime=data['time'].values
# 	doy = list(map(get_matlab2py_doy, mattime))
# 	doy = pd.DataFrame(doy, columns=['doy'])
# 	hour=doy%1*24
# 	idx=(hour>=9) & (hour<9+0.5)
# 	tdata=np.hstack([int(doy.iloc[0,0]),9,np.nanmean(newdata.loc[idx['doy'],:],axis=0)]) #这里idx的‘doy’是上面doy的，因为由其生成的
# 	for h in np.arange(9.5,16.5,0.5):
# 		idx=(hour>=h) & (hour<h+0.5)
# 		ttdata=np.hstack([int(doy.iloc[0,0]),h,np.nanmean(newdata.loc[idx['doy'],:],axis=0)])
# 		tdata=np.vstack([tdata,ttdata])
# 	tdata=pd.DataFrame(tdata,columns=['doy','hour','3FLD','iFLD','SFM'])
# 	if filesif==filesifs[0]:
# 		Tdata=tdata
# 	else:
# 		Tdata=pd.concat([Tdata,tdata],axis=0)
# 	print(filesif +' is ok...')
# Tdata.loc[(Tdata['3FLD']<0) | (Tdata['3FLD']>4),'3FLD']=np.nan 
# Tdata.loc[(Tdata['iFLD']<0) | (Tdata['iFLD']>4),'iFLD']=np.nan 
# Tdata.loc[(Tdata['SFM']<0) | (Tdata['SFM']>4),'SFM']=np.nan
# Tdata.to_csv(r'D:\Data2018\jr2018\Results'+'/SIF_halfhourmean.csv',index=False,header=True)
# ## get SIF method02
# filepath=r'D:\Data2018\jr2018\Results\2018句容水稻_SIF_Half_hour_8-18.xlsx'
# data=pd.ExcelFile(filepath)
# data=data.parse(0)
# doy=data['DOY']
# hour=doy%1
# idx=(hour>=9/24) & (hour<=16.2/24)
# data=data.loc[idx,:]
# newdata=pd.concat([data['DOY']-(data['DOY']%1),24*(data['DOY']%1),data['3FLD'],data['iFLD'],data['SFMlinear']],axis=1)
# newdata.columns=['doy','hour','3FLD','iFLD','SFM']
# newdata.to_csv(r'D:\Data2018\jr2018\Results\SIF_halfhourmean_method02.csv',index=False,header=True)

# # link sif&vi&radiance
# savepath=r'D:\Data2018\jr2018\Results'
# datasif = pd.read_csv(savepath + '/SIF_halfhourmean_method02.csv')
# print(datasif.shape)
# datavi = pd.read_csv(savepath + '/VI_ref_addMTVI2_halfhourlymean.csv')
# print(datavi.shape)
# # 把所有冠层辐射参数提取出来
# filecanopyra = r'D:\Thesis2\data_processed\Database REF\WalRefhalfhour_9-16_jr2018rice'
# files = os.listdir(filecanopyra)
# SRAD = pd.read_table(filecanopyra + '/' + files[0])
# # print(SRAD.columns)
# namedict = {'Rad-Down': files[0][:-4] + '_' + 'Rad-Down', 'Rad-up': files[0][
#     :-4] + '_' + 'Rad-Up', 'Reflectance': files[0][:-4] + '_' + 'Reflectance'}
# SRAD.rename(columns=namedict, inplace=True)
# # print(SRAD.columns)
# for file in files[1:]:
#     srad=pd.read_table(filecanopyra+'/'+file)
#     srad=srad.iloc[:,1:]
#     namedict = {'Rad-Down': file[:-4] + '_' + 'Rad-Down', 'Rad-up': file[
#     :-4] + '_' + 'Rad-Up', 'Reflectance': file[:-4] + '_' + 'Reflectance'}
#     srad.rename(columns=namedict,inplace=True)
#     SRAD=pd.concat([SRAD,srad],axis=1)
# dataall=pd.concat([datasif,datavi.iloc[:,2:],SRAD.iloc[:,1:]],axis=1)
# dataall.to_csv(r'D:\Data2018\jr2018\Results\SIF_vi_ref_radiance.csv',index=False,header=True)
# ## link dataall & EC flux data
# dataall=pd.read_csv(r'D:\Data2018\jr2018\Results\SIF_vi_ref_radiance.csv')
# print(dataall.shape)
# #link all
# dataflux = pd.ExcelFile(
#     r'D:\Data2018\jr_sq_flux_2018\jrflux\Jurong_2018_ECflux_data_final.xlsx')
# dataflux = dataflux.parse(0)  # 即Sheet1
#
# idx1 = (dataflux['date'] >= dataall.iloc[0, 0]) & (dataflux[
#     'date'] <= dataall.iloc[-1, 0]) & (dataflux['hour'] >= 9) & (dataflux['hour'] <= 16)
# dataflux = dataflux.loc[idx1, :]
# dataflux.index = range(dataflux.shape[0])
# dataflux.to_csv(r'D:\Data2018\jr2018\Results\jurong_2018_ecfluc.csv',index=False,header=True)
# newall=pd.concat([dataall,dataflux.iloc[:,3:]],axis=1)
# newall.to_csv(r'D:\Data2018\jr2018\Results\SIF_GPP_VI_ref_halfhourmean_jr2018rice.csv',index=False,header=True)
# print(dataflux.shape)
# dataflux['tempdoy']=dataflux['date']+dataflux['hour']/24
# dataall['tempdoy']=dataall['doy']+dataall['hour']/24
# start=1000
# for i in range(start,dataall.shape[0]):  # dataall.shape[0]
#     for j in range(start,dataflux.shape[0]):  # dataflux.shape[0]
#         if (dataflux.loc[j,'tempdoy']==dataall.loc[i,'tempdoy']):
#         # if (dataflux.loc[j, 'date'] == dataall.loc[i, 'doy']) & (dataflux.loc[j, 'hour'] == dataall.loc[i, 'hour']):
#             # pass
#             print(i, j)
#             if i == start:
#                 tdata = np.hstack(
#                     [dataall.iloc[i, :].values, dataflux.iloc[j, 3:].values])
#                 Tdata = tdata
#                 # print(Tdata)
#             else:
#                 tdata = np.hstack(
#                     [dataall.iloc[i, :].values, dataflux.iloc[j, 3:].values])
#                 Tdata = np.vstack([Tdata, tdata])
#                 # print(tdata)
#             continue

# print(Tdata.shape)
# Tdata = pd.DataFrame(Tdata, columns=np.hstack([dataall.columns,dataflux.columns[3:]]))
# # print(Tdata.shape)
# Tdata.to_csv(savepath + '/SIF_GPP_VI_ref_halfhourmean_jr2018rice.csv',
#              index=False, header=True)