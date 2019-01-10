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

ticklabelsize=14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}

filepath = r"D:\Thesis2\data_processed\spain"
data = pd.read_csv(filepath + "//Majadas2017-Eddy_and_Flox_droptime_sifclean_8-18_norain.csv", encoding='utf-8')
# print(data.columns)

DOYsif=data['doy.dayfract_mean']
DOYgpp=data['new_DOY']
SIF_A_ifld=data['SIF_A_ifld_mean']
SIF_A_sfm=data['SIF_A_sfm_mean']
NDVI=data['NDVI_mean']
PRI=data['PRI_mean']
GPP=data['GPP_MR_f_Subcanopy']
PAR=data['PARd_North']
NetPAR=data['NetRad_North']
LAIgreen_from_NDVI=data['LAI_green_fromNDVI']

#
plt.subplots(figsize=(10,5))
temp=pd.concat([SIF_A_ifld,GPP],axis=1)
# print(temp)
temp=temp.dropna()
x=temp['SIF_A_ifld_mean']
y=temp['GPP_MR_f_Subcanopy']
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
plt.scatter(SIF_A_ifld,GPP,edgecolors='k',facecolors='',label='SIFA_ifld '+text_rsqu)
plt.plot(x, pred_y, label=text_line, color='k')
#
temp=pd.concat([SIF_A_sfm,GPP],axis=1)
temp=temp.dropna()
x=temp['SIF_A_sfm_mean']
y=temp['GPP_MR_f_Subcanopy']
a, b, pred_y = funcs_lzh.get_lingre(x.values.reshape(-1, 1), y)
r, p = pearsonr(x, y)
r2 = '%.2f' % np.square(r)
text_line = 'y=' + '%.2f' % a + 'x' + '+' + '%.2f' % b
text_rsqu = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
plt.scatter(SIF_A_sfm,GPP,edgecolors='orange',facecolors='',label='SIFA_sfm '+text_rsqu)
plt.plot(x, pred_y, label=text_line, color='orange')
plt.xlabel('SIF',**axis_font)
plt.ylabel('GPP',**axis_font)
plt.legend(frameon=False,loc=4)
plt.tick_params(labelsize=ticklabelsize)
#
# fig2=plt.figure()
# axs=fig2.add_subplot(111)
# p1,=axs.plot(DOYsif,SIF_A_sfm,'ro',label='SIF')
# axs1=axs.twinx()
# p2,=axs1.plot(DOYgpp,GPP,'go',label='GPP')
# lines=[p1,p2]
# plt.legend(lines,[line.get_label() for line in lines])
fig,axs=plt.subplots(3,1,figsize=(10,5))
plt.subplots_adjust(hspace=0)
p1=axs[0].scatter(DOYsif,data['SIF_A_ifld_mean'],marker='.',c='k',label='SIF_A_ifld_mean')
axs[0].set_ylabel('SIF',**axis_font)
axs[0].set_xticks([])
axs[0].set_xlim([60,244])
axs[0].tick_params(labelsize=ticklabelsize)
axs[0].legend()
p2=axs[1].scatter(DOYsif,data['SIF_A_sfm_mean'],marker='.',c='k',label='SIF_A_sfm_mean')
axs[1].set_ylabel('SIF',**axis_font)
axs[1].set_xticks([])
axs[1].set_xlim([60,244])
axs[1].tick_params(labelsize=ticklabelsize)
axs[1].legend()
p3=axs[2].scatter(DOYgpp,data['GPP_MR_f_Subcanopy'],marker='.',c='k',label='GPP_MR_f_Subcanopy')
axs[2].set_ylabel('GPP',**axis_font)
axs[2].set_xlabel('DOY',**axis_font)
axs[2].set_xlim([60,244])
axs[2].set_xticks([60,100,140,180,220])
axs[2].tick_params(labelsize=ticklabelsize)
axs[2].legend()


# axs1.plot(DOY,NetPAR/100,color='gray',marker='o',alpha=0.2)
plt.show()
