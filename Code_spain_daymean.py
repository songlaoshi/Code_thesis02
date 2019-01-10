#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Time  : 18-12-10 下午2:18
#@Author: zhaohui li
#@File  : Code_spain.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcs_lzh
from scipy.stats.stats import pearsonr

ticklabelsize = 14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}

filepath = r"D:\Thesis2\data_processed\spain"
data = pd.read_csv(
    filepath + "//Majadas2017-Eddy_and_Flox_daymean_8-18.csv", encoding='utf-8')
# print(data.columns)
data=data.loc[(data['doy.dayfract_mean']<178).values,:]

DOYsif = data['doy.dayfract_mean']
DOYgpp = data['DOY.x_North']  # data['new_DOY'] #
DOY = data['DOY']
SIF_A_ifld = data['SIF_A_ifld_mean']
SIF_A_sfm = data['SIF_A_sfm_mean']
NDVI = data['NDVI_mean']
PRI = data['PRI_mean']
GPP = data['GPP_MR_f_Subcanopy']
PAR = data['PARd_North']
NetPAR = data['NetRad_North']
LAIgreen_from_NDVI = data['LAI_green_fromNDVI']

# # # ------------------SIF-GPP相关性图-------------
# plt.subplots(figsize=(5, 4.5))
# plt.subplots_adjust(left=0.2, bottom=0.15, right=0.9)
# temp = pd.concat([SIF_A_ifld, GPP], axis=1)
# # print(temp)
# temp = temp.dropna()
# x = temp['SIF_A_ifld_mean']
# y = temp['GPP_MR_f_Subcanopy']
# a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
# r, p = pearsonr(x, y)
# r2 = '%.2f' % np.square(r)
# text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
# text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
# plt.scatter(SIF_A_ifld, GPP, edgecolors='k',
#             facecolors='', label='SIFA_ifld ' + text_rsqu)
# plt.plot(x, pred_y, label=text_line, color='k')
# #
# temp = pd.concat([SIF_A_sfm, GPP], axis=1)
# temp = temp.dropna()
# x = temp['SIF_A_sfm_mean']
# y = temp['GPP_MR_f_Subcanopy']
# a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
# r, p = pearsonr(x, y)
# r2 = '%.2f' % np.square(r)
# text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
# text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
# plt.scatter(SIF_A_sfm, GPP, edgecolors='orange',
#             facecolors='', label='SIFA_sfm ' + text_rsqu)
# plt.plot(x, pred_y, label=text_line, color='orange')
# plt.xlabel('SIF', **axis_font)
# plt.ylabel('GPP', **axis_font)
# plt.legend(frameon=False, loc=4)
# plt.tick_params(labelsize=ticklabelsize)
# # ------------------SIF-GPP季节变化图-------------
# fig2 = plt.figure(figsize=(10, 3))
# axs = fig2.add_subplot(111)
# p1,= axs.plot(DOY, SIF_A_sfm, 'ro-', markerfacecolor='none',label='SIF')
# axs.set_ylabel('SIF', **axis_font)
# axs.set_xlabel('DOY', **axis_font)
# axs1 = axs.twinx()
# p2,= axs1.plot(DOY, GPP, 'go-', markerfacecolor='none', label='GPP')
# lines = [p1, p2]
# axs.legend(lines, [line.get_label() for line in lines])
# axs1.set_ylabel('GPP', **axis_font)
# axs.set_xticks([60, 100, 140, 180, 220])
# axs.tick_params(labelsize=ticklabelsize)
# axs1.tick_params(labelsize=ticklabelsize)
# # # ------------------VPD-SIF-GPP-PAR-APAR季节变化图-------------
fig, axs = plt.subplots(7, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=0)

cv = np.nanmean(data['VPD_f_Subcanopy']) / np.nanstd(data['VPD_f_Subcanopy'])
funcs_lzh.bar_xy(DOY, data['VPD_f_Subcanopy'], '', 'VPD',
                 'VPD_f_Subcanopy' + ',CV=' + '%.2f' % cv, 0.3, axs[0])

cv = np.nanmean(data['SIF_A_sfm_mean']) / np.nanstd(data['SIF_A_sfm_mean'])
funcs_lzh.scatter_xy(DOY, data['SIF_A_sfm_mean'], '', 'SIF',
                     'o', 'k', '', 'SIF' + ',CV=' + '%.2f' % cv, axs[1])

cv = np.nanmean(data['GPP_MR_f_Subcanopy']) / np.nanstd(data['GPP_MR_f_Subcanopy'])
funcs_lzh.scatter_xy(DOY, data['GPP_MR_f_Subcanopy'], '', 'GPP',
                     'o', 'k', '', 'GPP_MR_f_Subcanopy' + ',CV=' + '%.2f' % cv, axs[2])

cv = np.nanmean(data['PARd_North']) / np.nanstd(data['PARd_North'])
funcs_lzh.bar_xy(DOY, data['PARd_North'], '', 'PAR',
                      'PARd_North' + ',CV=' + '%.2f' % cv, 0.5,axs[3])

cv = np.nanmean(data['NDVI_mean']) / np.nanstd(data['NDVI_mean'])
funcs_lzh.scatter_xy(DOY, data['NDVI_mean'], '', 'NDVI',
                     'o', 'k', '', 'NDVI' + ',CV=' + '%.2f' % cv, axs[4])

cv = np.nanmean(data['PRI_mean']) / np.nanstd(data['PRI_mean'])
funcs_lzh.scatter_xy(DOY, data['PRI_mean'], '', 'PRI',
                     'o', 'k', '', 'PRI' + ',CV=' + '%.2f' % cv, axs[5])

cv = np.nanmean(data['Rain_North']) / np.nanstd(data['Rain_North'])
funcs_lzh.scatter_xy(DOY, data['Rain_North'], '', 'Rain',
                     'o', 'k', '', 'Rain_North' + ',CV=' + '%.2f' % cv, axs[6])

axs[6].set_xlabel('DOY',**axis_font)



# # ------------------SIFyield-LUE季节变化图-------------
# fig, axs = plt.subplots(5, 1, figsize=(10, 5))
# plt.subplots_adjust(hspace=0)

# axs1.plot(DOY,NetPAR/100,color='gray',marker='o',alpha=0.2)

# # ------------------SIF-GPP-PAR-相关性图-------------
SIF=data['SIF_A_sfm_mean']
GPP=data['GPP_MR_f_Subcanopy']
fig,axs=plt.subplots(1,4,figsize=(14, 5))
plt.subplots_adjust(wspace=0.48, bottom=0.19, top=0.93)
x=SIF
y=GPP
xlabel='SIF (mW/m2/nm/sr)'
ylabel='GPP (umol/m2/s)'
funcs_lzh.plot_xy(x, y, xlabel, ylabel,axs[0])
funcs_lzh.plot_xy(data['SIF_A_sfm_mean'], data['PARd_North'], 'SIF (mW/m2/nm/sr)', 'PAR',axs[1])
funcs_lzh.plot_xy(data['GPP_MR_f_Subcanopy'], data['PARd_North'], 'GPP (umol/m2/s)', 'PAR',axs[2])
data['LUE']=data['GPP_MR_f_Subcanopy']/data['PARd_North']
data['SIFyield']=data['SIF_A_sfm_mean']/data['PARd_North']
funcs_lzh.plot_xy(data['SIFyield'], data['LUE'], 'SIFyield', 'LUE',axs[3])
axs[3].set_xlim(0,0.0015)
axs[3].set_ylim(0,0.04)


plt.show()
