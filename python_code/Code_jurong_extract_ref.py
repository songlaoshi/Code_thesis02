#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-21 13:00:58
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import pandas as pd
import numpy as np

fileref = r'D:\Data2018\jr2018\Results'

##
ref=pd.ExcelFile(fileref+'/'+'HR_REF_2018句容水稻_halfhour_9_16_reflectance.xlsx')
ref=ref.parse('Sheet1')
wl=ref.columns
wl=np.array(wl)[1:]
doy=ref['DOY']
refdata=ref.iloc[:,1:]
# #
iblue=(wl>=459) & (wl<=479)
igreen=(wl>=545) & (wl<=565)
ired=(wl>=620) & (wl<=670)
inir=(wl>=841) & (wl<=876)
# #
Blue=np.mean(refdata.iloc[:,iblue],axis=1)
Green=np.mean(refdata.iloc[:,igreen],axis=1)
Red=np.mean(refdata.iloc[:,ired],axis=1)
NIR=np.mean(refdata.iloc[:,inir],axis=1)
# clean data
Blue[Blue>1]=np.nan
Green[Green>1]=np.nan
Red[Red>1]=np.nan
NIR[NIR>1]=np.nan
# save to file

t=pd.DataFrame(np.vstack([doy,Blue,Green,Red,NIR]).T,columns=['doy','blue','green','red','nir'])
t.to_csv(fileref+'/'+'ref_extract_halfhour.csv',header=True,index=False)

# # extract all ref data
# files = os.listdir(fileref + '/REF/HR_REF')
# # print(files)

# filename = fileref + '/REF/HR_REF' + '/' + files[0]
# ref = pd.ExcelFile(filename)
# ref = ref.parse('Sheet1')
# wl = ref.columns
# wl = np.array(wl)[1:]
# TIME = ref['Time']
# refdata = ref.iloc[:, 1:]

# iblue = (wl >= 459) & (wl <= 479)
# igreen = (wl >= 545) & (wl <= 565)
# ired = (wl >= 620) & (wl <= 670)
# inir = (wl >= 841) & (wl <= 876)
# # # get average values
# BLUE = np.mean(refdata.iloc[:, iblue], axis=1)
# GREEN = np.mean(refdata.iloc[:, igreen], axis=1)
# RED = np.mean(refdata.iloc[:, ired], axis=1)
# Nir = np.mean(refdata.iloc[:, inir], axis=1)

# for i in range(1, len(files)):
#     filename = fileref + '/REF/HR_REF' + '/' + files[i]
#     ref = pd.ExcelFile(filename)
#     ref = ref.parse('Sheet1')
#     time = ref['Time']
#     refdata = ref.iloc[:, 1:]
#     # # get average values
#     Blue = np.mean(refdata.iloc[:, iblue], axis=1)
#     Green = np.mean(refdata.iloc[:, igreen], axis=1)
#     Red = np.mean(refdata.iloc[:, ired], axis=1)
#     NIR = np.mean(refdata.iloc[:, inir], axis=1)

#     # connect
#     BLUE = pd.concat([BLUE, Blue], axis=0)
#     GREEN = pd.concat([GREEN, Green], axis=0)
#     RED = pd.concat([RED, Red], axis=0)
#     Nir = pd.concat([Nir, NIR], axis=0)
#     TIME = pd.concat([TIME, time], axis=0)
#     print(files[i]+' is ok....')
#     ##
# BLUE = BLUE.reset_index()
# TIME = TIME.reset_index()
# GREEN=GREEN.reset_index()
# RED=RED.reset_index()
# Nir=Nir.reset_index()

# t = pd.concat([TIME.iloc[:, 1], BLUE.iloc[:, 1], GREEN.iloc[:, 1], RED.iloc[
#                  :, 1], Nir.iloc[:, 1]], axis=1)
# t.columns=['time','blue','green','red','nir']
# # data clean
# idx1=((t['time']-np.fix(t['time']))>=8/24) & ((t['time']-np.fix(t['time']))<=17/24)
# idx2=t['blue']>0.2 
# idx3=t['green']>0.2
# idx4=t['red']>0.2
# idx5=t['nir']>0.6
# t=t[idx1]
# t.loc[idx2,'blue']=np.nan
# t.loc[idx3,'green']=np.nan
# t.loc[idx4,'red']=np.nan
# t.loc[idx5,'nir']=np.nan
# t.dropna()
# t.reset_index()
# # save data
# t.to_csv(fileref + '/' + 'ref_extract_all_clean.csv', header=True, index=False)
