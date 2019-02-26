#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-14 14:25:21
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# functions
def heatmap(data, text,row_labels, col_labels, ax=None, rotation=0,cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """
    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax)
    cbar.ax.set_ylabel(cbarlabel, rotation=90, va="top")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=rotation, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=1)
    ax.tick_params(which="minor", bottom=False, left=False)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            text = ax.text(j, i, '%.2f' % data.iloc[
                        i, j], ha='center', va='center', color='w')

    return im, cbar

def corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath):
    '''
    保存相关系数矩阵（图像和excel文件）
    '''
    fig,ax=plt.subplots()
    fig.subplots_adjust(top=0.86)
    im,cbar=heatmap(corrs1,corrs1,labels1,labels1,ax=ax,vmin=-1, vmax=1,cmap='RdGy',cbarlabel='Pearson r [-]')
    ax.set_xlabel(sitename,**axis_font)
    plt.savefig(savepath+'/'+sitename+'_corr.png')
    fig,ax=plt.subplots()
    fig.subplots_adjust(top=0.86)
    im,cbar=heatmap(corrs2,corrs2,labels2,labels2,ax=ax,vmin=-1, vmax=1,rotation=-30,cmap='RdGy',cbarlabel='Pearson r [-]')
    ax.set_xlabel(sitename,**axis_font)
    plt.savefig(savepath+'/'+sitename+'_corr_yield.png')
    # save file
    writer=pd.ExcelWriter(savepath+'/'+sitename+'_corr.xlsx')
    corrs1.to_excel(writer,'Sheet1')
    corrs2.to_excel(writer,'Sheet2')
    writer.save()

# 全局变量
stime = 8.9 / 24
etime = 16.1 / 24
ci_threshold = 0.5
# 字体格式
ticklabelsize = 14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}
# labels
labels1=["SIF", "GPP", 'SIFesc', "APAR", "NIRvP", 'NIRvR']
labels2=["SIFyield", "LUE", '$SIFyield_{NIRvP}$', "$SIFyield_{NIRvR}$", "fesc", 'NIRv']
# savepath
savepath=r'D:\Thesis2\data_processed\Database r'
################site harvard###############################
filepath = r'D:\Thesis2\data_processed\harvard'
# 合并2013,2014年的数据,区分阴晴天
data2013 = pd.read_csv(
    filepath + '/USHa1_2013apar_sif_gpp_metho_hourly_8-18.csv')
data2014 = pd.read_csv(
    filepath + '/USHa1_2014apar_sif_gpp_metho_hourly_8-18.csv')
dataall = pd.concat([data2013, data2014], axis=0)
# SIF冠层emission
dataall['NIRv'] = dataall['ndvi.r'] * dataall['r.750']
dataall['fPAR'] = dataall['apar'] / dataall['incident.ppfd']
dataall['fesc'] = dataall['NIRv'] / dataall['fPAR']

dataall['SIF'] = dataall['SIF']
dataall['GPP'] = dataall[' GPP( umol/m2/s)']
dataall['APAR'] = dataall['apar']
dataall['SIFesc'] = dataall['SIF'] / dataall['fesc']
dataall['NIRvP'] = dataall['NIRv'] * dataall['incident.ppfd']
dataall['NIRvR'] = dataall['ndvi.r'] * dataall['out.750'] / np.pi

dataall['SIFyield'] = dataall['SIF'] / dataall['APAR']
dataall['SIFyield_NIRvP'] = dataall['SIF'] / dataall['NIRvP']
dataall['SIFyield_NIRvR'] = dataall['SIF'] / dataall['NIRvR']
dataall['LUE'] = dataall['GPP'] / dataall['APAR']
# correlation matrix plot
newdata = pd.concat([dataall['SIF'], dataall['GPP'], dataall['SIFesc'],
                     dataall['APAR'], dataall['NIRvP'], dataall['NIRvR']], axis=1)
corrs1 = newdata.corr()
newdata = pd.concat([dataall['SIFyield'], dataall['LUE'], dataall['SIFyield_NIRvP'],
                     dataall['SIFyield_NIRvR'], dataall['fesc'], dataall['NIRv']], axis=1)
corrs2 = newdata.corr()
sitename='harvard'
corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath)
################site avignon###############################
# filepath = r'D:\Thesis2\data_processed\avignon'
# dataall = pd.read_csv(
#     filepath + '/AV2010db1_sifclean_8-18_ref.csv')
# # SIF冠层emission
# dataall['apar']=dataall['fAPAR']*dataall['PAR']
# dataall['NIRv'] = dataall['NDVI'] * dataall['Veg_reflectance_790_800']
# dataall['fPAR'] = dataall['apar'] / dataall['PAR']
# dataall['fesc'] = dataall['NIRv'] / dataall['fPAR']

# dataall['SIF'] = dataall['SIF760']
# dataall['GPP'] = dataall['GPP']
# dataall['APAR'] = dataall['apar']
# dataall['SIFesc'] = dataall['SIF'] / dataall['fesc']
# dataall['NIRvP'] = dataall['NIRv'] * dataall['PAR']
# dataall['NIRvR'] = dataall['NDVI'] * dataall['Veg_radiance_790_800']

# dataall['SIFyield'] = dataall['SIF'] / dataall['APAR']
# dataall['SIFyield_NIRvP'] = dataall['SIF'] / dataall['NIRvP']
# dataall['SIFyield_NIRvR'] = dataall['SIF'] / dataall['NIRvR']
# dataall['LUE'] = dataall['GPP'] / dataall['APAR']
# # correlation matrix plot
# newdata = pd.concat([dataall['SIF'], dataall['GPP'], dataall['SIFesc'],
#                      dataall['APAR'], dataall['NIRvP'], dataall['NIRvR']], axis=1)
# corrs1 = newdata.corr()
# newdata = pd.concat([dataall['SIFyield'], dataall['LUE'], dataall['SIFyield_NIRvP'],
#                      dataall['SIFyield_NIRvR'], dataall['fesc'], dataall['NIRv']], axis=1)
# corrs2 = newdata.corr()
# sitename='avignon'
# corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath)
# ################site shangqiu corn###############################
# filepath = r'D:\Thesis2\data_processed\shangqiu'
# dataall = pd.ExcelFile(
#     filepath + '/SIF_GPP_VI_ref_halfhourmean_sq2017corn.xlsx')
# dataall=dataall.parse(0)
# # SIF冠层emission
# dataall['NIRv'] = dataall['NDVI'] * dataall['Ref_790_800_Reflectance']
# dataall['fPAR'] = dataall['APAR'] / dataall['PAR']
# dataall['fesc'] = dataall['NIRv'] / dataall['fPAR']

# dataall['SIF'] = dataall['SFM']
# dataall['GPP'] = dataall['GPP']
# # dataall['APAR'] = dataall['apar']
# dataall['SIFesc'] = dataall['SIF'] / dataall['fesc']
# dataall['NIRvP'] = dataall['NIRv'] * dataall['PAR']
# dataall['NIRvR'] = dataall['NDVI'] * dataall['Ref_790_800_Rad-Down']

# dataall['SIFyield'] = dataall['SIF'] / dataall['APAR']
# dataall['SIFyield_NIRvP'] = dataall['SIF'] / dataall['NIRvP']
# dataall['SIFyield_NIRvR'] = dataall['SIF'] / dataall['NIRvR']
# dataall['LUE'] = dataall['GPP'] / dataall['APAR']
# # correlation matrix plot
# newdata = pd.concat([dataall['SIF'], dataall['GPP'], dataall['SIFesc'],
#                      dataall['APAR'], dataall['NIRvP'], dataall['NIRvR']], axis=1)
# corrs1 = newdata.corr()
# newdata = pd.concat([dataall['SIFyield'], dataall['LUE'], dataall['SIFyield_NIRvP'],
#                      dataall['SIFyield_NIRvR'], dataall['fesc'], dataall['NIRv']], axis=1)
# corrs2 = newdata.corr()
# sitename='shangqiu_corn'
# corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath)
################site shangqiu wheat###############################
filepath = r'D:\Thesis2\data_processed\shangqiu'
dataall = pd.ExcelFile(
    filepath + '/SIF_GPP_VI_ref_halfhourmean_sq2018wheat.xlsx')
dataall=dataall.parse(0)
# SIF冠层emission
dataall['NIRv'] = dataall['NDVI'] * dataall['Ref_790_800_Reflectance']
dataall['fPAR'] = dataall['APAR'] / dataall['PPFD_1_1_3']
dataall['fesc'] = dataall['NIRv'] / dataall['fPAR']

dataall['SIF'] = dataall['SFM']
dataall['GPP'] = dataall['GPP_gapfilled']
# dataall['APAR'] = dataall['apar']
dataall['SIFesc'] = dataall['SIF'] / dataall['fesc']
dataall['NIRvP'] = dataall['NIRv'] * dataall['PPFD_1_1_3']
dataall['NIRvR'] = dataall['NDVI'] * dataall['Ref_790_800_Rad-Down']

dataall['SIFyield'] = dataall['SIF'] / dataall['APAR']
dataall['SIFyield_NIRvP'] = dataall['SIF'] / dataall['NIRvP']
dataall['SIFyield_NIRvR'] = dataall['SIF'] / dataall['NIRvR']
dataall['LUE'] = dataall['GPP'] / dataall['APAR']
# correlation matrix plot
newdata = pd.concat([dataall['SIF'], dataall['GPP'], dataall['SIFesc'],
                     dataall['APAR'], dataall['NIRvP'], dataall['NIRvR']], axis=1)
corrs1 = newdata.corr()
newdata = pd.concat([dataall['SIFyield'], dataall['LUE'], dataall['SIFyield_NIRvP'],
                     dataall['SIFyield_NIRvR'], dataall['fesc'], dataall['NIRv']], axis=1)
corrs2 = newdata.corr()
sitename='shangqiu_wheat'
corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath)
################site avignon###############################
# filepath = r'D:\Thesis2\data_processed\spain'
# dataall = pd.ExcelFile(
#     filepath + '/Majadas2017-Eddy_and_Flox_droptime_sifclean_8-18_norain.xlsx')
# dataall=dataall.parse(0)
# # SIF冠层emission
# dataall['NIRv'] = dataall['NDVI_mean'] * dataall['Reflectance_790_mean']
# dataall['fPAR'] = dataall['NDVI_mean'] * 1.11 - 0.29
# # dataall['fPAR'] = dataall['APAR'] / dataall['PAR']
# dataall['fesc'] = dataall['NIRv'] / dataall['fPAR']

# dataall['SIF'] = dataall['SIF_A_sfm_mean']
# dataall['GPP'] = dataall['GPP_MR_f_Subcanopy']
# dataall['APAR'] = dataall['fPAR']*dataall['PARd_North']
# dataall['SIFesc'] = dataall['SIF'] / dataall['fesc']
# dataall['NIRvP'] = dataall['NIRv'] * dataall['PARd_North']
# dataall['NIRvR'] = dataall['NDVI_mean'] * dataall['Reflected_radiance_790_mean']

# dataall['SIFyield'] = dataall['SIF'] / dataall['APAR']
# dataall['SIFyield_NIRvP'] = dataall['SIF'] / dataall['NIRvP']
# dataall['SIFyield_NIRvR'] = dataall['SIF'] / dataall['NIRvR']
# dataall['LUE'] = dataall['GPP'] / dataall['APAR']
# # correlation matrix plot
# newdata = pd.concat([dataall['SIF'], dataall['GPP'], dataall['SIFesc'],
#                      dataall['APAR'], dataall['NIRvP'], dataall['NIRvR']], axis=1)
# corrs1 = newdata.corr()
# newdata = pd.concat([dataall['SIFyield'], dataall['LUE'], dataall['SIFyield_NIRvP'],
#                      dataall['SIFyield_NIRvR'], dataall['fesc'], dataall['NIRv']], axis=1)
# corrs2 = newdata.corr()
# sitename='majadas'
# corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath)
# ################site jurong 2016###############################
# filepath = r'D:\Thesis2\data_processed\jurong'
# dataall = pd.ExcelFile(
#     filepath + '/jurong2016_sifclean_8-18_ref_norain_addCI.xlsx')
# dataall=dataall.parse(0)
# # SIF冠层emission
# dataall['CIgreen']=dataall['Ref_790_800_Reflectance']/dataall['Ref_560_570_Reflectance']-1
# dataall['NIRv'] = dataall['NDVI'] * dataall['Ref_790_800_Reflectance']
# # dataall['fPAR'] = dataall['APAR'] / dataall['PAR']
# dataall['fPAR'] = dataall['CIgreen'] * 0.13 - 0.13
# dataall['fesc'] = dataall['NIRv'] / dataall['fPAR']

# dataall['SIF'] = dataall['SIF760']
# dataall['GPP'] = dataall['GPP(umol CO2 m-2 s-1)']

# dataall['APAR'] = dataall['fPAR']*dataall['PAR']
# dataall['SIFesc'] = dataall['SIF'] / dataall['fesc']
# dataall['NIRvP'] = dataall['NIRv'] * dataall['PAR']
# dataall['NIRvR'] = dataall['NDVI'] * dataall['Ref_790_800_Rad-Down']

# dataall['SIFyield'] = dataall['SIF'] / dataall['APAR']
# dataall['SIFyield_NIRvP'] = dataall['SIF'] / dataall['NIRvP']
# dataall['SIFyield_NIRvR'] = dataall['SIF'] / dataall['NIRvR']
# dataall['LUE'] = dataall['GPP'] / dataall['APAR']
# # correlation matrix plot
# newdata = pd.concat([dataall['SIF'], dataall['GPP'], dataall['SIFesc'],
#                      dataall['APAR'], dataall['NIRvP'], dataall['NIRvR']], axis=1)
# corrs1 = newdata.corr()
# newdata = pd.concat([dataall['SIFyield'], dataall['LUE'], dataall['SIFyield_NIRvP'],
#                      dataall['SIFyield_NIRvR'], dataall['fesc'], dataall['NIRv']], axis=1)
# corrs2 = newdata.corr()
# sitename='jurong2016'
# corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath)
# ################site jurong 2018###############################
# filepath = r'D:\Thesis2\data_processed\jurong'
# dataall = pd.ExcelFile(
#     filepath + '/SIF_GPP_VI_ref_halfhourmean_jr2018rice.xlsx')
# dataall=dataall.parse(0)
# # SIF冠层emission
# dataall['NIRv'] = dataall['NDVI'] * dataall['Ref_790_800_Reflectance']
# dataall['fPAR'] = dataall['CIgreen'] * 0.13 - 0.13
# # dataall['fPAR'] = dataall['APAR'] / dataall['Rg(W/m2)']
# dataall['fesc'] = dataall['NIRv'] / dataall['fPAR']

# dataall['SIF'] = dataall['SFM']
# dataall['GPP'] = dataall['GPP_gapfilled']
# dataall['APAR'] = dataall['Rg(W/m2)']*dataall['fPAR']
# dataall['SIFesc'] = dataall['SIF'] / dataall['fesc']
# dataall['NIRvP'] = dataall['NIRv'] * dataall['Rg(W/m2)']
# dataall['NIRvR'] = dataall['NDVI'] * dataall['Ref_790_800_Rad-Down']

# dataall['SIFyield'] = dataall['SIF'] / dataall['APAR']
# dataall['SIFyield_NIRvP'] = dataall['SIF'] / dataall['NIRvP']
# dataall['SIFyield_NIRvR'] = dataall['SIF'] / dataall['NIRvR']
# dataall['LUE'] = dataall['GPP'] / dataall['APAR']
# # correlation matrix plot
# newdata = pd.concat([dataall['SIF'], dataall['GPP'], dataall['SIFesc'],
#                      dataall['APAR'], dataall['NIRvP'], dataall['NIRvR']], axis=1)
# corrs1 = newdata.corr()
# newdata = pd.concat([dataall['SIFyield'], dataall['LUE'], dataall['SIFyield_NIRvP'],
#                      dataall['SIFyield_NIRvR'], dataall['fesc'], dataall['NIRv']], axis=1)
# corrs2 = newdata.corr()
# sitename='jurong2018'
# corr_save_map(corrs1,corrs2,labels1,labels2,sitename,savepath)

plt.show()

