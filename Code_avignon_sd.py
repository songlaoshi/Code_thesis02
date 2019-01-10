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

filepath=r"D:\Thesis2\data\Avignon\Database db1\1 - SIF-EC"

data=pd.read_table(filepath+"//AV2010db1sd.txt",encoding='utf-8')

# print(data.head(5))
DOY = data['DOY'].values
PAR = data['PAR'].values
PAR2 = data['PAR2'].values
PAR2diff = data['PAR2diff'].values
NDVI = data['NDVI'].values
PRI = data['PRI'].values
SIF687 = data['SIF687'].values * 1000
SIF687[SIF687 < 0] = np.nan
SIF760 = data['SIF760'].values * 1000
SIF760[SIF760 < 0] = np.nan
GPP = data['GPP'].values
GPP[GPP < 0] = np.nan
PAR_fromfapar = data['PAR_fromfapar'].values
fAPAR = data['fAPAR'].values
fAPAR = [float(x) for x in fAPAR]  # fAPAR读出来是字符串,所以先转成float

# # ------------------SIF, GPP, PAR ----------------------------
fig, axs = plt.subplots(2, 1)
plt.subplots_adjust(hspace=0)

temp = pd.DataFrame(np.vstack((PAR, GPP)).T, columns=['PAR', 'GPP'])
temp = temp.dropna()
x = temp['PAR']
y = temp['GPP']
# 线性回归+相关系数
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
axs[0].scatter(x, y, label=text_rsqu, edgecolors='k', facecolors='')
axs[0].plot(x, pred_y, label=text_line, color='k')
axs[0].set_xlabel('PAR')
axs[0].set_ylabel('GPP')
axs[0].set_ylim([0, 70])
axs[0].set_xlim([0, 2000])
axs[0].set_xticks([])
axs[0].legend(loc=2, frameon=False)

temp = pd.DataFrame(np.vstack((PAR, SIF760)).T, columns=['PAR', 'SIF760'])
temp = temp.dropna()
x = temp['PAR']
y = temp['SIF760']
# 线性回归+相关系数
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
axs[1].scatter(x, y, label=text_rsqu, edgecolors='k', facecolors='')
axs[1].plot(x, pred_y, label='SIF760 ' + text_line, color='k')

temp = pd.DataFrame(np.vstack((PAR, SIF687)).T, columns=['PAR', 'SIF760'])
temp = temp.dropna()
x = temp['PAR']
y = temp['SIF760']
# 线性回归+相关系数
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
axs[1].scatter(x, y, label=text_rsqu, edgecolors='r', facecolors='')
axs[1].plot(x, pred_y, label='SIF687 ' + text_line, color='r')

axs[1].set_xlabel('PAR')
axs[1].set_ylabel('SIF')
axs[1].set_ylim([0, 3])
axs[1].set_xlim([0, 2000])
axs[1].legend(loc=2, frameon=False)

# # # ------------------SIF, GPP, APAR ----------------------------
fig, axs = plt.subplots(2, 1)
plt.subplots_adjust(hspace=0)

temp = pd.DataFrame(np.vstack((PAR, GPP, fAPAR)).T, columns=['PAR', 'GPP', 'fapar'])
temp = temp.dropna()
x = temp['PAR'] * temp['fapar']
y = temp['GPP']
# 线性回归+相关系数
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
axs[0].scatter(x, y, label=text_rsqu, edgecolors='k', facecolors='')
axs[0].plot(x, pred_y, label=text_line, color='k')
axs[0].set_xlabel('APAR')
axs[0].set_ylabel('GPP')
axs[0].set_ylim([0, 70])
axs[0].set_xlim([0, 2000])
axs[0].set_xticks([])
axs[0].legend(loc=2, frameon=False)

temp = pd.DataFrame(np.vstack((PAR, SIF760, fAPAR)).T, columns=['PAR', 'SIF760', 'fapar'])
temp = temp.dropna()
x = temp['PAR'] * temp['fapar']
y = temp['SIF760']
# 线性回归+相关系数
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
axs[1].scatter(x, y, label=text_rsqu, edgecolors='k', facecolors='')
axs[1].plot(x, pred_y, label='SIF760 ' + text_line, color='k')

temp = pd.DataFrame(np.vstack((PAR, SIF687, fAPAR)).T, columns=['PAR', 'SIF760', 'fapar'])
temp = temp.dropna()
x = temp['PAR'] * temp['fapar']
y = temp['SIF760']
# 线性回归+相关系数
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
axs[1].scatter(x, y, label=text_rsqu, edgecolors='r', facecolors='')
axs[1].plot(x, pred_y, label='SIF687 ' + text_line, color='r')

axs[1].set_xlabel('APAR')
axs[1].set_ylabel('SIF')
axs[1].set_ylim([0, 3])
axs[1].set_xlim([0, 2000])
axs[1].legend(loc=2, frameon=False)

plt.show()
