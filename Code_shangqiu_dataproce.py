#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 19:12:15
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import numpy as np
import pandas as pd

sifpath = r'D:\Data\shangqiu data\shang\Results\GPP_PAR_APAR_SIF_8_18\ALLnew'
refpath = r'D:\Data\shangqiu data\shang\Results_HRdata_recal'
savepath=r'D:\Thesis2\data_processed\shangqiu'
# 导入数据
sif = pd.ExcelFile(
    sifpath + '/GPP_VPD_Ta_Tleaf_PAR_APAR_norain_SIF_VI_NIRv_CI_SIFyield_LUE_halfhour.xlsx')
ref = pd.read_csv(refpath + '/VI_ref_addMTVI2_halfhourlymean.csv')
sif = sif.parse('Sheet1')
ref.columns = ['doy', 'hour', 'ndvi', 'evi', 'mtci', 'mtvi2', 'pri', 'greenndvi',
               'rededgendvi', 'cigreen', 'cvi', 'sr', 'ref_blue', 'ref_green', 'ref_red', 'ref_nir', 'ref_rededge']
ref[ref>100]=np.nan
# link
ref_extract = ref.iloc[0:sif.shape[0], :]
alldata = pd.concat([sif, ref_extract.iloc[:, 2:]], axis=1)
# save data
alldata.to_csv(savepath+'/shangqiu_2017_sif_gpp_ref_vi.csv',index=False,header=True)
#
