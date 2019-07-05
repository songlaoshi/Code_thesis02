#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-16 22:02:28
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import funcs_lzh
# 全局变量
stime = 8.9 / 24
etime = 16.1 / 24
ci_threshold = 0.5
# 字体格式
ticklabelsize = 14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}
# labels
labels1=['NIRvP-SIF','NIRvP',"SIF", "NIRvR", 'NIRvR-SIF']
labels11=['SIFyield_NIRvP'+'\n'+'-SIFyield','SIFyield_NIRvP'
,"SIFyield", "SIFyield_NIRvR", 'SIFyield_NIRvR'+'\n'+'-SIFyield']
labels2=['$Har$','$Avi$','$Sha_{corn}$','$Sha_{wheat}$',
'$Maj$','$Jur_{rice2016}$','$Jur_{rice2018}$']
# path
filepath=r'D:\Thesis2\data_processed\Database r'
savepath=r'D:\Thesis2\data_processed\Database r\minu_corr'
# NIRvP/NIRvR能否提高 SIFyield与LUE关系
files=os.listdir(filepath)
gpp=[]
lue=[]
for file in files:
	print(file)
	if os.path.splitext(file)[1]=='.xlsx':
		# print(file)
		data=pd.ExcelFile(filepath+'/'+file)
		data1=data.parse(0)
		data2=data.parse(1)
		gpp.append([data1.iloc[4,1],data1.iloc[0,1],data1.iloc[5,1]])
		lue.append([data2.iloc[2,1],data2.iloc[0,1],data2.iloc[3,1]])

GPP=np.ones([5,7])
GPP[1:4,:]=np.array(gpp).reshape(3,7)
GPP[0,:]=GPP[1,:]-GPP[2,:]
GPP[4,:]=GPP[3,:]-GPP[2,:]
LUE=np.ones([5,7])
LUE[1:4,:]=np.array(lue).reshape(3,7)
LUE[0,:]=LUE[1,:]-LUE[2,:]
LUE[4,:]=LUE[3,:]-LUE[2,:]
print(GPP,LUE)
GPP=pd.DataFrame(GPP,columns=labels2)
LUE=pd.DataFrame(LUE,columns=labels2)
## heatmap
fig,ax=plt.subplots()
fig.subplots_adjust(left=0.16,right=0.94)
im,cbar=funcs_lzh.heatmap(GPP,GPP,labels1,labels2,ax=ax,vmin=-1, vmax=1,rotation=-30,cmap='RdGy',cbarlabel='Pearson r [-]')
ax.set_xlabel('SIF/NIRvP/NIRvR vs GPP',**axis_font)
plt.savefig(savepath+'/minu_corr.png')

fig,ax=plt.subplots()
fig.subplots_adjust(left=0.16,right=0.94)
im,cbar=funcs_lzh.heatmap(LUE,LUE,labels11,labels2,ax=ax,vmin=-1, vmax=1,rotation=-30,cmap='RdGy',cbarlabel='Pearson r [-]')
ax.set_xlabel('SIF/NIRvP/NIRvR vs GPP',**axis_font)
plt.savefig(savepath+'/minus_corr_yield.png')

plt.show()

