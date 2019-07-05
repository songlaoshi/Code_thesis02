#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-03 19:52:35
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import funcs_lzh
from scipy.stats.stats import pearsonr

ticklabelsize=14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}

filepath = r"D:\Thesis2\data_processed\harvard"
data = pd.read_csv(filepath + "//USHa1_2014apar_sif_gpp_metho_hourly_8-18.csv", encoding='utf-8')
# print(data.columns)
ndata=pd.concat([data['SIF'],data['r.860'],data['incident.ppfd'],data['ndvi']
	,data[' GPP( umol/m2/s)'],data['apar']],axis=1)
print(ndata.shape)
ndata=ndata.dropna()
##
SIF=ndata['SIF']
NIRv=ndata['r.860']
PAR=ndata['incident.ppfd']
NDVI=ndata['ndvi']
NIRvP=NIRv*PAR
GPP=ndata[' GPP( umol/m2/s)']
APAR=ndata['apar']
fPAR=APAR/PAR # 或者用植被指数替代
fesc=NIRv/fPAR
SIFesc=SIF/fesc
#NIRvR=NDVI*R_nir_radiance
columns=['SIF','APAR','SIFesc','GPP','NIRvP']
newdata=pd.concat([SIF,APAR,SIFesc,GPP,NIRvP],axis=1)
newdata.columns=columns
## plot
# r, p = pearsonr(APAR, GPP)
# r2_apar_gpp = np.square(r)
# # r2_apar_gpp = '$R^2$= ' + r2 + funcs_lzh.funcstar(p)
# r, p = pearsonr(SIF, GPP)
# r2_sif_gpp =  np.square(r)
# r, p = pearsonr(SIFesc, GPP)
# r2_sifesc_gpp =  np.square(r)
# r, p = pearsonr(NIRvP, GPP)
# r2_nirvp_gpp =  np.square(r)

# plt.figure(figsize=(5,5))
# t=np.array([r2_apar_gpp,r2_sif_gpp,r2_sifesc_gpp,r2_nirvp_gpp])
# # print(t)
# plt.bar(range(4),t)
# plt.xticks([0,1,2,3],["APAR","SIF","SIFesc","NIRvP"])
# plt.ylabel('$R^2$')
# plt.title('GPP')
# plt.show()

## correlation matrix plot
corrs=newdata.corr()
# plot correlation matrix
cax=plt.imshow(corrs,vmin=0,vmax=1) 
plt.colorbar()
ticks=np.arange(0,5)
plt.xticks(ticks,["SIF","APAR","SIFesc","GPP","NIRvP"])
plt.yticks(ticks,["SIF","APAR","SIFesc","GPP","NIRvP"])
# print(corrs)

## scatterplot matrix
pd.plotting.scatter_matrix(newdata,figsize=(10,10),c='k')

plt.show()

