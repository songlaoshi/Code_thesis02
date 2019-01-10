#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-22 15:15:46
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import pandas as pd
import numpy as np

filepath = r'D:\Data2018\jr2018\Results'
parpath = r'D:\Data2018\jr_sq_flux_2018\jrflux'
sif = pd.ExcelFile(filepath + '/2018句容水稻_SIF_Half_hour_8-18.xlsx')
sif = sif.parse('Sheet1')
print(sif.shape)
sif = sif.loc[((sif['DOY'] - np.fix(sif['DOY'])) >= 9 / 24) &
              ((sif['DOY'] - np.fix(sif['DOY'])) < 16.5 / 24), :]
print(sif.shape)
# 重新排列索引，不然写入数据时会乱序（因为写入是根据index来排列的）
sif.index=range(len(sif.index))
# print(sif.head())
ref = pd.read_csv(filepath + '/ref_extract.csv')
print(ref.shape)
# par data
par = pd.ExcelFile(parpath + '/EP_summary_2018jurong_rice.xlsx')
par = par.parse(0)
par=par.loc[1:,:]
idx = (par.loc[:,'DoY'] >= np.fix(sif.iloc[0,0])) & (par.loc[:,'DoY']<= np.fix(
    sif.iloc[-1,0])) & (par.loc[:,'Hour'] >= 9) & (par.loc[:,'Hour'] <= 16)
par = par.loc[idx,:]
par.index=range(len(par.index))
# 合并sif,ref,par
t=pd.concat([ref,sif['SFMlinear'],par[['Rg','GPP']]],axis=1)
# # save data
t.to_csv(filepath + '/' + 'ref_sif_par_all.csv', header=True, index=False)

