#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 18-12-9 下午5:06
# @Author: zhaohui li
# @File  : Code_avignon.py

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcs_lzh
from scipy.stats.stats import pearsonr
import math
# 字体格式
ticklabelsize = 14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}
# 文件路径
filepath=r"D:\Thesis2\data\Avignon\Database db1\1 - SIF-EC"
savepath=r'D:\Thesis2\data_processed\avignon'
# 读取数据
# data=pd.read_table(filepath+"//AV2010db1.txt",encoding='utf-8')
data = pd.read_csv(
    savepath + "/" + "AV2010db1_sifclean_daymean_8-18.csv", encoding='utf-8')
# 
DOY = data['DOY']
PAR = data['PAR']
PAR2 = data['PAR2']
PAR2diff = data['PAR2diff']
NDVI = data['NDVI']
PRI = data['PRI']
data.loc[data['SIF687']<0,'SIF687']=np.nan
data['SIF687']=data['SIF687']*1000
data.loc[data['SIF760']<0,'SIF760']=np.nan
data['SIF760']=data['SIF760']*1000
data.loc[data['GPP']<0,'GPP']=np.nan
PAR_fromfapar = data['PAR_fromfapar']
fAPAR = data['fAPAR'].values
fAPAR = [float(x) for x in fAPAR]  # fAPAR读出来是字符串,所以先转成float
data['fPAR']=pd.DataFrame(fAPAR,columns=['fPAR'])
# 新建APAR列
data['APAR']=data['fPAR']*data['PAR']
data.loc[data['APAR']<0,'APAR']=np.nan
data['LUE']=data['GPP']/data['APAR']
data['SIFyield']=data['SIF760']/data['APAR']
# # ------------------SIF-GPP相关性图-------------
SIF=data['SIF760']
GPP=data['GPP']
fig,axs=plt.subplots(1,4,figsize=(14, 5))
plt.subplots_adjust(wspace=0.48, bottom=0.19, top=0.93)
x=SIF
y=GPP
xlabel='SIF(mW/m2/nm/sr)'
ylabel='GPP( umol/m2/s)'
funcs_lzh.plot_xy(x, y, xlabel, ylabel,axs[0])
funcs_lzh.plot_xy(SIF, data['APAR'], 'SIF(mW/m2/nm/sr)', 'APAR',axs[1])
funcs_lzh.plot_xy(data['GPP'], data['APAR'], 'GPP( umol/m2/s)', 'APAR',axs[2])
funcs_lzh.plot_xy(data['SIFyield'], data['LUE'], 'SIFyield', 'LUE',axs[3])
axs[3].set_xlim(0,0.002)
axs[3].set_ylim(0,0.12)
# # ------------------VPD-SIF-GPP-PAR-APAR季节变化图-------------
fig, axs = plt.subplots(9, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=0)
# cv = np.nanmean(data['Water_vapour_concentration']) / np.nanstd(data['Water_vapour_concentration'])
# funcs_lzh.bar_xy(DOY, data['Water_vapour_concentration'], '', 'Water_vapour_concentration',
#                  'Water_vapour_concentration' + ',CV=' + '%.2f' % cv, 0.3, axs[0])

cv = np.nanmean(data['SIF760']) / np.nanstd(data['SIF760'])
funcs_lzh.scatter_xy(DOY, data['SIF760'], '', 'SIF',
                     'o', 'k', '', 'SIF' + ',CV=' + '%.2f' % cv, axs[1])

cv = np.nanmean(data['GPP']) / np.nanstd(data['GPP'])
funcs_lzh.scatter_xy(DOY, data['GPP'], '', 'GPP',
                     'o', 'k', '', 'GPP' + ',CV=' + '%.2f' % cv, axs[2])

cv = np.nanmean(data['APAR']) / np.nanstd(data['APAR'])
funcs_lzh.bar_xy(DOY, data['APAR'], '', 'APAR',
                      'APAR' + ',CV=' + '%.2f' % cv, 0.5,axs[3])

data['fpar']=data['fPAR']
cv = np.nanmean(data['fpar']) / np.nanstd(data['fpar'])
funcs_lzh.scatter_xy(DOY, data['fpar'], '', '$f_{PAR}$',
                     'o', 'k', '', '$f_{PAR}$' + ',CV=' + '%.2f' % cv, axs[4])

cv1 = np.nanmean(data['LUE']) / np.nanstd(data['LUE'])
funcs_lzh.scatter_xy(DOY, data['LUE'], '', 'LUE',
                     'o', 'k', '', 'LUE' + ',CV=' + '%.2f' % cv1, axs[5])
axs[5].set_ylim([0,0.05])

cv2 = np.nanmean(data['SIFyield']) / np.nanstd(data['SIFyield'])
funcs_lzh.scatter_xy(DOY, data['SIFyield'], '', 'SIF$_{yield}$',
                     'o', 'k', '', 'SIF$_{yield}$' + ',CV=' + '%.2f' % cv2, axs[6])
axs[6].set_ylim([0,0.0013])

cv = np.nanmean(data['NDVI']) / np.nanstd(data['NDVI'])
funcs_lzh.scatter_xy(DOY, data['NDVI'], '', 'NDVI',
                     'o', 'k', '', 'NDVI' + ',CV=' + '%.2f' % cv, axs[7])

cv = np.nanmean(data['PRI']) / np.nanstd(data['PRI'])
funcs_lzh.scatter_xy(DOY, data['PRI'], '', 'PRI',
                     'o', 'k', '', 'PRI' + ',CV=' + '%.2f' % cv, axs[8])

axs[8].set_xlabel('DOY', **axis_font)
# axs[8].set_xticks([170, 200, 230, 260, 290])

plt.show()
