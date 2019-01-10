#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-14 14:47:35
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcs_lzh
from scipy.stats.stats import pearsonr

ticklabelsize = 14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}

# define file folder and save folder
filepath = r"D:\Thesis2\data_processed\harvard"
savepath = filepath
# load data
data = pd.read_csv(
    savepath + "/" + "USHa1_2014apar_sif_gpp_metho_daily_8-18.csv", encoding='utf-8')
# print(data.shape)
# analysis
DOY = data['DOYnew']
# # ------------------VPD-SIF-GPP-PAR-APAR季节变化图-------------
# fig=plt.subplots(3,1,figsize=(10,5))
fig, axs = plt.subplots(9, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=0)
cv = np.nanmean(data[' VPD']) / np.nanstd(data[' VPD'])
funcs_lzh.bar_xy(DOY, data[' VPD'], '', 'VPD',
                 'VPD' + ',CV=' + '%.2f' % cv, 0.3, axs[0])

cv = np.nanmean(data['SIF']) / np.nanstd(data['SIF'])
funcs_lzh.scatter_xy(DOY, data['SIF'], '', 'SIF',
                     'o', 'k', '', 'SIF' + ',CV=' + '%.2f' % cv, axs[1])

cv = np.nanmean(data[' GPP( umol/m2/s)']) / np.nanstd(data[' GPP( umol/m2/s)'])
funcs_lzh.scatter_xy(DOY, data[' GPP( umol/m2/s)'], '', 'GPP',
                     'o', 'k', '', 'GPP' + ',CV=' + '%.2f' % cv, axs[2])

cv = np.nanmean(data['apar']) / np.nanstd(data['apar'])
funcs_lzh.bar_xy(DOY, data['apar'], '', 'APAR',
                      'APAR' + ',CV=' + '%.2f' % cv, 0.5,axs[3])

data['fpar']=data['apar']/data['incident.ppfd']
cv = np.nanmean(data['fpar']) / np.nanstd(data['fpar'])
funcs_lzh.scatter_xy(DOY, data['fpar'], '', '$f_{PAR}$',
                     'o', 'k', '', '$f_{PAR}$' + ',CV=' + '%.2f' % cv, axs[4])

data['LUE']=data[' GPP( umol/m2/s)']/data['apar']
cv1 = np.nanmean(data['LUE']) / np.nanstd(data['LUE'])
funcs_lzh.scatter_xy(DOY, data['LUE'], '', 'LUE',
                     'o', 'k', '', 'LUE' + ',CV=' + '%.2f' % cv1, axs[5])
axs[5].set_ylim([0,0.05])

data['SIFyield']=data['SIF']/data['apar']
cv2 = np.nanmean(data['SIFyield']) / np.nanstd(data['SIFyield'])
funcs_lzh.scatter_xy(DOY, data['SIFyield'], '', 'SIF$_{yield}$',
                     'o', 'k', '', 'SIF$_{yield}$' + ',CV=' + '%.2f' % cv2, axs[6])
axs[6].set_ylim([0,0.0013])

cv = np.nanmean(data['ndvi']) / np.nanstd(data['ndvi'])
funcs_lzh.scatter_xy(DOY, data['ndvi'], '', 'NDVI',
                     'o', 'k', '', 'NDVI' + ',CV=' + '%.2f' % cv, axs[7])

cv = np.nanmean(data['pri']) / np.nanstd(data['pri'])
funcs_lzh.scatter_xy(DOY, data['pri'], '', 'PRI',
                     'o', 'k', '', 'PRI' + ',CV=' + '%.2f' % cv, axs[8])

axs[8].set_xlabel('DOY', **axis_font)
# axs[8].set_xticks([170, 200, 230, 260, 290])

# # ------------------SIF-GPP相关性图-------------
SIF=data['SIF']
GPP=data[' GPP( umol/m2/s)']
fig,axs=plt.subplots(1,4,figsize=(14, 5))
plt.subplots_adjust(wspace=0.48, bottom=0.19, top=0.93)
x=SIF
y=GPP
xlabel='SIF(mW/m2/nm/sr)'
ylabel='GPP( umol/m2/s)'
funcs_lzh.plot_xy(x, y, xlabel, ylabel,axs[0])
funcs_lzh.plot_xy(data['SIF'], data['apar'], 'SIF(mW/m2/nm/sr)', 'APAR',axs[1])
funcs_lzh.plot_xy(data[' GPP( umol/m2/s)'], data['apar'], 'GPP( umol/m2/s)', 'APAR',axs[2])
data['LUE']=data[' GPP( umol/m2/s)']/data['apar']
data['SIFyield']=data['SIF']/data['apar']
funcs_lzh.plot_xy(data['SIFyield'], data['LUE'], 'SIFyield', 'LUE',axs[3])
axs[3].set_xlim(0,0.0013)
axs[3].set_ylim(0,0.05)
# --------------SIF，GPP和PAR的日变化----------------
# 2013
plt.show()
