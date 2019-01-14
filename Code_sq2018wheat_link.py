#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-12 16:32:56
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import pandas as pd
import numpy as np
import datetime
import VIs_calculation_func

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

#
savepath = r'D:\Data2018\SIF_Tower'
# # get_vis_addMTVI2
# dataref=pd.ExcelFile(r'D:\Data2018\SIF_Tower\halfhour_9_16_reflectance.xlsx')
# dataref=dataref.parse(0)
# wl=dataref.columns[1:].values
# ref=dataref.iloc[:,1:]
# doy=dataref['DOY']
# hour=(doy%1)*24
# setup=VIs_calculation_func.get_vegetation_indices(wl,ref)
# columns=['doy','hour','NDVI','EVI','MTCI','MTVI2'
#     ,'PRI','greenNDVI','rededgeNDVI','CIgreen','CVI','SR','ref_blue',
#     'ref_green','ref_red','ref_nir','ref_rededge']

# savedata=pd.DataFrame((np.vstack([doy,hour,setup.NDVI,setup.EVI,
#     	setup.MTCI,setup.MTVI2,setup.PRI,setup.greenNDVI,setup.rededgeNDVI,
#         setup.CIgreen,setup.CVI,setup.SR,setup.Rblue,setup.Rgreen,setup.Rred,
#         setup.Rnir,setup.Rrededge]).T),columns=columns)
# savedata.to_csv(savepath+'/VI_ref_addMTVI2_halfhourlymean.csv',index=False,header=True)

# ## get SIF
# filepath=r'D:\Data2018\SIF_Tower\SIF day'
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
# Tdata.to_csv(savepath+'/SIF_halfhourmean.csv',index=False,header=True)

# # link sif&vi&radiance
datasif = pd.read_csv(savepath + '/SIF_halfhourmean.csv')
datavi = pd.read_csv(savepath + '/VI_ref_addMTVI2_halfhourlymean.csv')
# 把所有冠层辐射参数提取出来
filecanopyra = r'D:\Thesis2\data_processed\Database REF\WalRefhalfhour_9-19_sq2018wheat'
files = os.listdir(filecanopyra)
SRAD = pd.read_table(filecanopyra + '/' + files[0])
# print(SRAD.columns)
namedict = {'Rad-Down': files[0][:-4] + '_' + 'Rad-Down', 'Rad-Up': files[0][
    :-4] + '_' + 'Rad-Up', 'Reflectance': files[0][:-4] + '_' + 'Reflectance'}
SRAD.rename(columns=namedict, inplace=True)
# print(SRAD.columns)
for file in files[1:]:
    srad=pd.read_table(filecanopyra+'/'+file)
    srad=srad.iloc[:,1:]
    namedict = {'Rad-Down': file[:-4] + '_' + 'Rad-Down', 'Rad-Up': file[
    :-4] + '_' + 'Rad-Up', 'Reflectance': file[:-4] + '_' + 'Reflectance'}
    srad.rename(columns=namedict,inplace=True)
    SRAD=pd.concat([SRAD,srad],axis=1)
dataall=pd.concat([datasif,datavi.iloc[:,2:],SRAD.iloc[:,1:]],axis=1)
# link all
dataflux = pd.ExcelFile(
    r'D:\Data2018\sq_flux_2018\SQ_ECflux_2018wheat_0226_0526.xlsx')
dataflux = dataflux.parse(0)  # 即Sheet1

idx1 = (dataflux['date'] >= dataall.iloc[0, 0]) & (dataflux[
    'date'] <= dataall.iloc[-1, 0]) & (dataflux['hour'] >= 9) & (dataflux['hour'] <= 16)
dataflux = dataflux.loc[idx1, :]
dataflux.index = range(dataflux.shape[0])

for i in range(dataall.shape[0]):  # dataall.shape[0]
    for j in range(dataflux.shape[0]):  # dataflux.shape[0]
        if (dataflux.loc[j, 'date'] == dataall.loc[i, 'doy']) & (dataflux.loc[j, 'hour'] == dataall.loc[i, 'hour']):
            # pass
            print(i, j)
            if i == 0:
                tdata = np.hstack(
                    [dataall.iloc[i, :].values, dataflux.iloc[j, 3:].values])
                Tdata = tdata
                # print(Tdata)
            else:
                tdata = np.hstack(
                    [dataall.iloc[i, :].values, dataflux.iloc[j, 3:].values])
                Tdata = np.vstack([Tdata, tdata])
                # print(tdata)
            continue

Tdata = pd.DataFrame(Tdata, columns=np.hstack([dataall.columns,dataflux.columns[3:]]))
# print(Tdata.shape)
Tdata.to_csv(savepath + '/SIF_GPP_VI_ref_halfhourmean_sq2018wheat.csv',
             index=False, header=True)
