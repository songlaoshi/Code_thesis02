#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 19:12:15
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import numpy as np
import pandas as pd
import VIs_calculation_func

sifpath = r'D:\Data\shangqiu data\shang\Results\GPP_PAR_APAR_SIF_8_18\ALLnew'
refpath = r'D:\Data\shangqiu data\shang\Results_HRdata_recal'
savepath=r'D:\Thesis2\data_processed\shangqiu'
# #get_vis_addMTVI2
# dataref=pd.ExcelFile(r'D:\Data\shangqiu data\shang\Results_HRdata_recal\halfhour_9_16_reflectance.xlsx')
# dataref=dataref.parse(0)
# wl=dataref.columns[1:].values
# ref=dataref.iloc[:,1:]
# #
# datara=pd.ExcelFile(r'D:\Data\shangqiu data\shang\Results_HRdata_recal\halfhour_9_16_radiance.xlsx')
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
#       setup.MTCI,setup.MTVI2,setup.PRI,setup.greenNDVI,setup.rededgeNDVI,
#         setup.CIgreen,setup.CVI,setup.SR,setup.Rblue,setup.Rgreen,setup.Rred,
#         setup.Rnir,setup.Rrededge,setup.Ra_blue,setup.Ra_green,setup.Ra_red,
#         setup.Ra_nir,setup.Ra_rededge]).T),columns=columns)
# savedata.to_csv(refpath+'/VI_ref_addMTVI2_halfhourlymean.csv',index=False,header=True)
# #导入数据
# sif = pd.ExcelFile(
#     sifpath + '/GPP_VPD_Ta_Tleaf_PAR_APAR_norain_SIF_VI_NIRv_CI_SIFyield_LUE_halfhour.xlsx')
# sif = sif.parse('Sheet1')
# # print(sif.shape)
# sif=sif.loc[((sif['DOY']%1)>=8.8/24) & ((sif['DOY']%1)<=16/24),:]
# sif.to_csv(refpath+'/sif.csv',index=False,header=True)
# # print(sif.head(20))
# # print(sif.shape)

#link sif&vi&radiance
datavi = pd.read_csv(refpath + '/VI_ref_addMTVI2_halfhourlymean.csv')
# 把所有冠层辐射参数提取出来
filecanopyra = r'D:\Thesis2\data_processed\Database REF\WalRefhalfhour_9-16_sq2017corn'
files = os.listdir(filecanopyra)
SRAD = pd.read_table(filecanopyra + '/' + files[0])
# print(SRAD.columns)
namedict = {'Rad-Down': files[0][:-4] + '_' + 'Rad-Down', 'Rad-up': files[0][
    :-4] + '_' + 'Rad-Up', 'Reflectance': files[0][:-4] + '_' + 'Reflectance'}
SRAD.rename(columns=namedict, inplace=True)
# print(SRAD.columns)
for file in files[1:]:
    srad=pd.read_table(filecanopyra+'/'+file)
    srad=srad.iloc[:,1:]
    namedict = {'Rad-Down': file[:-4] + '_' + 'Rad-Down', 'Rad-up': file[
    :-4] + '_' + 'Rad-Up', 'Reflectance': file[:-4] + '_' + 'Reflectance'}
    srad.rename(columns=namedict,inplace=True)
    SRAD=pd.concat([SRAD,srad],axis=1)
dataall=pd.concat([datavi,SRAD.iloc[:,1:]],axis=1)
dataall.to_csv(refpath+'/VIs_ref_radiance.csv',index=False,header=True)