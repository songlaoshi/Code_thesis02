#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 10:32:32
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from scipy.stats.stats import pearsonr
import matplotlib.pyplot as plt
import funcs_lzh
# 全局变量
stime=10.9/24
etime=13.1/24
# ################site harvard###############################
# filepath = r'D:\Thesis2\data_processed\harvard'
# # 合并2013,2014年的数据,区分阴晴天
# sunny1 = pd.read_csv(
#     filepath + '/USHa1_2013apar_sif_gpp_metho_hourly_8-18_sunny.csv')
# sunny2 = pd.read_csv(
#     filepath + '/USHa1_2014apar_sif_gpp_metho_hourly_8-18_sunny.csv')
# cloudy1 = pd.read_csv(
#     filepath + '/USHa1_2013apar_sif_gpp_metho_hourly_8-18_cloudy.csv')
# cloudy2 = pd.read_csv(
#     filepath + '/USHa1_2014apar_sif_gpp_metho_hourly_8-18_cloudy.csv')
# sunny = pd.concat([sunny1, sunny2], axis=0)
# cloudy = pd.concat([cloudy1, cloudy2], axis=0)
# # 选择时间范围
# idx=(sunny['hour']>=stime) & (sunny['hour']<=etime)
# sunny=sunny.loc[idx,:]
# # idx=(cloudy['hour']>=10.9/24) & (cloudy['hour']<=13.1/24)
# cloudy=cloudy.loc[idx,:]
# # 新建Dataframe,只提取sif和gpp
# sunny = pd.concat([sunny['doy'], sunny['SIF'], sunny[' GPP( umol/m2/s)'],
#                    sunny['r.750'], sunny['incident.ppfd'], sunny['ndvi.r'],sunny['apar']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['doy'], cloudy['SIF'], cloudy[' GPP( umol/m2/s)'],
#                     cloudy['r.750'], cloudy['incident.ppfd'], cloudy['ndvi.r'],cloudy['apar']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['NIRv']=sunny['ndvi.r']*sunny['r.750']
# sunny['fPAR']=sunny['apar']/sunny['incident.ppfd']
# sunny['fesc']=sunny['NIRv']/sunny['fPAR']
# sunny['SIFesc']=sunny['SIF']/sunny['fesc']
# cloudy['NIRv']=cloudy['ndvi.r']*cloudy['r.750']
# cloudy['fPAR']=cloudy['apar']/cloudy['incident.ppfd']
# cloudy['fesc']=cloudy['NIRv']/cloudy['fPAR']
# cloudy['SIFesc']=cloudy['SIF']/cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x = sunny['SIF']
# y = sunny[' GPP( umol/m2/s)']
# a, b, pred_y = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# cloudy_pred_y = a * cloudy['SIF'] + b
# allday_pred_y = a * allday['SIF'] + b
# pred_y = pd.DataFrame(pred_y, columns=['sunny_pred_y'])

# x = cloudy['SIF']
# y = cloudy[' GPP( umol/m2/s)']
# a, b, pred_y1 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y1 = pd.DataFrame(pred_y1, columns=['cloudy_pred_y'])

# x = allday['SIF']
# y = allday[' GPP( umol/m2/s)']
# a, b, pred_y2 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y2 = pd.DataFrame(pred_y2, columns=['allday_pred_y'])
# # 显示结果
# fig, axs = plt.subplots(3, 3, figsize=(10, 10))
# fig.subplots_adjust(hspace=0.4)
# funcs_lzh.plot_xy(sunny['SIF'], sunny[' GPP( umol/m2/s)'],
#                   'SIF_sunny', 'GPP_sunny', axs[0, 0])
# funcs_lzh.plot_xy(sunny[' GPP( umol/m2/s)'], pred_y['sunny_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[0, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     sunny[' GPP( umol/m2/s)'], pred_y['sunny_pred_y'])
# axs[0, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# funcs_lzh.plot_xy(cloudy['SIF'], cloudy[' GPP( umol/m2/s)'],
#                   'SIF_cloudy', 'GPP_cloudy', axs[1, 0])
# funcs_lzh.plot_xy(cloudy[' GPP( umol/m2/s)'], pred_y1['cloudy_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[1, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy[' GPP( umol/m2/s)'], pred_y1['cloudy_pred_y'])
# axs[1, 1].text(0, 28, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# funcs_lzh.plot_xy(cloudy[' GPP( umol/m2/s)'],
#                   cloudy_pred_y, 'GPP_mea', 'GPP_pre', axs[1, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy[' GPP( umol/m2/s)'], cloudy_pred_y)
# axs[1, 2].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# funcs_lzh.plot_xy(allday['SIF'], allday[
#                   ' GPP( umol/m2/s)'], 'SIF_all', 'GPP_all', axs[2, 0])
# funcs_lzh.plot_xy(allday[' GPP( umol/m2/s)'], pred_y2['allday_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[2, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday[' GPP( umol/m2/s)'], pred_y2['allday_pred_y'])
# axs[2, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# funcs_lzh.plot_xy(allday[' GPP( umol/m2/s)'],
#                   allday_pred_y, 'GPP_mea', 'GPP_pre', axs[2, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday[' GPP( umol/m2/s)'], allday_pred_y)
# axs[2, 2].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# # 消除冠层结构的影响会怎样？
# # ------------------------------------------------------------
# # 建立线性回归模型
# x = sunny['SIFesc']
# y = sunny[' GPP( umol/m2/s)']
# a, b, pred_y = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# cloudy_pred_y = a * cloudy['SIFesc'] + b
# allday_pred_y = a * allday['SIFesc'] + b
# pred_y = pd.DataFrame(pred_y, columns=['sunny_pred_y'])

# x = cloudy['SIFesc']
# y = cloudy[' GPP( umol/m2/s)']
# a, b, pred_y1 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y1 = pd.DataFrame(pred_y1, columns=['cloudy_pred_y'])

# x = allday['SIFesc']
# y = allday[' GPP( umol/m2/s)']
# a, b, pred_y2 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y2 = pd.DataFrame(pred_y2, columns=['allday_pred_y'])
# # 显示结果
# fig, axs = plt.subplots(3, 3, figsize=(10, 10))
# fig.subplots_adjust(hspace=0.4)
# funcs_lzh.plot_xy(sunny['SIFesc'], sunny[' GPP( umol/m2/s)'],
#                   'SIF_sunny', 'GPP_sunny', axs[0, 0])
# funcs_lzh.plot_xy(sunny[' GPP( umol/m2/s)'], pred_y['sunny_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[0, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     sunny[' GPP( umol/m2/s)'], pred_y['sunny_pred_y'])
# axs[0, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# funcs_lzh.plot_xy(cloudy['SIFesc'], cloudy[' GPP( umol/m2/s)'],
#                   'SIF_cloudy', 'GPP_cloudy', axs[1, 0])
# funcs_lzh.plot_xy(cloudy[' GPP( umol/m2/s)'], pred_y1['cloudy_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[1, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy[' GPP( umol/m2/s)'], pred_y1['cloudy_pred_y'])
# axs[1, 1].text(0, 28, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# funcs_lzh.plot_xy(cloudy[' GPP( umol/m2/s)'],
#                   cloudy_pred_y, 'GPP_mea', 'GPP_pre', axs[1, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy[' GPP( umol/m2/s)'], cloudy_pred_y)
# axs[1, 2].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# funcs_lzh.plot_xy(allday['SIFesc'], allday[
#                   ' GPP( umol/m2/s)'], 'SIF_all', 'GPP_all', axs[2, 0])
# funcs_lzh.plot_xy(allday[' GPP( umol/m2/s)'], pred_y2['allday_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[2, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday[' GPP( umol/m2/s)'], pred_y2['allday_pred_y'])
# axs[2, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# funcs_lzh.plot_xy(allday[' GPP( umol/m2/s)'],
#                   allday_pred_y, 'GPP_mea', 'GPP_pre', axs[2, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday[' GPP( umol/m2/s)'], allday_pred_y)
# axs[2, 2].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

################site Avignon###############################
filepath = r'D:\Thesis2\data_processed\avignon'
# 阴晴天
sunny = pd.read_csv(
    filepath + '/AV2010db1_sifclean_8-18_sunny_ref.csv')
cloudy = pd.read_csv(
    filepath + '/AV2010db1_sifclean_8-18_cloudy_ref.csv')
# 选择时间范围
idx=((sunny['DOY']%1)>=stime) & ((sunny['DOY']%1)<=etime)
sunny=sunny.loc[idx,:]
cloudy=cloudy.loc[idx,:]
# 
sunny['apar']=sunny['fAPAR']*sunny['PAR']
cloudy['apar']=cloudy['fAPAR']*cloudy['PAR']
# 新建Dataframe,只提取sif和gpp
sunny = pd.concat([sunny['DOY'], sunny['SIF760'], sunny['GPP'],
                   sunny['Veg_reflectance_750_760'], sunny['PAR'], sunny['NDVI'],sunny['apar']], axis=1)
sunny = sunny.dropna()
cloudy = pd.concat([cloudy['DOY'], cloudy['SIF760'], cloudy['GPP'],
                    cloudy['Veg_reflectance_750_760'], cloudy['PAR'], cloudy['NDVI'],cloudy['apar']], axis=1)
cloudy = cloudy.dropna()
# 重新设置index，不然会有重复的index
sunny = sunny.reset_index()
cloudy = cloudy.reset_index()
# SIF冠层emission
sunny['SIF']=sunny['SIF760']
cloudy['SIF']=cloudy['SIF760']
sunny['NIRv']=sunny['NDVI']*sunny['Veg_reflectance_750_760']
sunny['fPAR']=sunny['apar']/sunny['PAR']
sunny['fesc']=sunny['NIRv']/sunny['fPAR']
sunny['SIFesc']=sunny['SIF']/sunny['fesc']
cloudy['NIRv']=cloudy['NDVI']*cloudy['Veg_reflectance_750_760']
cloudy['fPAR']=cloudy['apar']/cloudy['PAR']
cloudy['fesc']=cloudy['NIRv']/cloudy['fPAR']
cloudy['SIFesc']=cloudy['SIF']/cloudy['fesc']
# 晴天+阴天
allday = pd.concat([sunny, cloudy], axis=0)
allday = allday.reset_index()
# ------------------------------------------------------------
# 建立线性回归模型
x = sunny['SIF']
y = sunny['GPP']
a, b, pred_y = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
cloudy_pred_y = a * cloudy['SIF'] + b
allday_pred_y = a * allday['SIF'] + b
pred_y = pd.DataFrame(pred_y, columns=['sunny_pred_y'])

x = cloudy['SIF']
y = cloudy['GPP']
a, b, pred_y1 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
pred_y1 = pd.DataFrame(pred_y1, columns=['cloudy_pred_y'])

x = allday['SIF']
y = allday['GPP']
a, b, pred_y2 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
pred_y2 = pd.DataFrame(pred_y2, columns=['allday_pred_y'])
# 显示结果
fig, axs = plt.subplots(3, 3, figsize=(10, 10))
fig.subplots_adjust(hspace=0.4)
funcs_lzh.plot_xy(sunny['SIF'], sunny['GPP'],
                  'SIF_sunny', 'GPP_sunny', axs[0, 0])
axs[0,0].set_xlim([0,0.0022])
funcs_lzh.plot_xy(sunny['GPP'], pred_y['sunny_pred_y'],
                  'GPP_mea_self', 'GPP_pre_self', axs[0, 1])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    sunny['GPP'], pred_y['sunny_pred_y'])
axs[0, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')

funcs_lzh.plot_xy(cloudy['SIF'], cloudy['GPP'],
                  'SIF_cloudy', 'GPP_cloudy', axs[1, 0])
axs[1,0].set_xlim([0,0.0022])
funcs_lzh.plot_xy(cloudy['GPP'], pred_y1['cloudy_pred_y'],
                  'GPP_mea_self', 'GPP_pre_self', axs[1, 1])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    cloudy['GPP'], pred_y1['cloudy_pred_y'])
axs[1, 1].text(0, 28, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')
axs[1,1].set_xlim([-2,55])
funcs_lzh.plot_xy(cloudy['GPP'],
                  cloudy_pred_y, 'GPP_mea', 'GPP_pre', axs[1, 2])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    cloudy['GPP'], cloudy_pred_y)
axs[1, 2].text(0, 35, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')
axs[1,2].set_xlim([-2,55])

funcs_lzh.plot_xy(allday['SIF'], allday[
                  'GPP'], 'SIF_all', 'GPP_all', axs[2, 0])
axs[2,0].set_xlim([0,0.0022])
funcs_lzh.plot_xy(allday['GPP'], pred_y2['allday_pred_y'],
                  'GPP_mea_self', 'GPP_pre_self', axs[2, 1])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    allday['GPP'], pred_y2['allday_pred_y'])
axs[2, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')
funcs_lzh.plot_xy(allday['GPP'],
                  allday_pred_y, 'GPP_mea', 'GPP_pre', axs[2, 2])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    allday['GPP'], allday_pred_y)
axs[2, 2].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')

# 消除冠层结构的影响会怎样？
# ------------------------------------------------------------
# 建立线性回归模型
x = sunny['SIFesc']
y = sunny['GPP']
a, b, pred_y = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
cloudy_pred_y = a * cloudy['SIFesc'] + b
allday_pred_y = a * allday['SIFesc'] + b
pred_y = pd.DataFrame(pred_y, columns=['sunny_pred_y'])

x = cloudy['SIFesc']
y = cloudy['GPP']
a, b, pred_y1 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
pred_y1 = pd.DataFrame(pred_y1, columns=['cloudy_pred_y'])

x = allday['SIFesc']
y = allday['GPP']
a, b, pred_y2 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
pred_y2 = pd.DataFrame(pred_y2, columns=['allday_pred_y'])
# 显示结果
fig, axs = plt.subplots(3, 3, figsize=(10, 10))
fig.subplots_adjust(hspace=0.4)
funcs_lzh.plot_xy(sunny['SIFesc'], sunny['GPP'],
                  'SIF_sunny', 'GPP_sunny', axs[0, 0])
axs[0,0].set_xlim([0,0.005])
funcs_lzh.plot_xy(sunny['GPP'], pred_y['sunny_pred_y'],
                  'GPP_mea_self', 'GPP_pre_self', axs[0, 1])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    sunny['GPP'], pred_y['sunny_pred_y'])
axs[0, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')

funcs_lzh.plot_xy(cloudy['SIFesc'], cloudy['GPP'],
                  'SIF_cloudy', 'GPP_cloudy', axs[1, 0])
axs[1,0].set_xlim([0,0.006])
funcs_lzh.plot_xy(cloudy['GPP'], pred_y1['cloudy_pred_y'],
                  'GPP_mea_self', 'GPP_pre_self', axs[1, 1])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    cloudy['GPP'], pred_y1['cloudy_pred_y'])
axs[1, 1].text(0, 35, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')
axs[1,1].set_xlim([-2,55])
funcs_lzh.plot_xy(cloudy['GPP'],
                  cloudy_pred_y, 'GPP_mea', 'GPP_pre', axs[1, 2])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    cloudy['GPP'], cloudy_pred_y)
axs[1, 2].text(0, 40, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')
axs[1,2].set_xlim([-2,55])

funcs_lzh.plot_xy(allday['SIFesc'], allday[
                  'GPP'], 'SIF_all', 'GPP_all', axs[2, 0])
axs[2,0].set_xlim([0,0.006])
funcs_lzh.plot_xy(allday['GPP'], pred_y2['allday_pred_y'],
                  'GPP_mea_self', 'GPP_pre_self', axs[2, 1])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    allday['GPP'], pred_y2['allday_pred_y'])
axs[2, 1].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')
funcs_lzh.plot_xy(allday['GPP'],
                  allday_pred_y, 'GPP_mea', 'GPP_pre', axs[2, 2])
rmse, rrmse = funcs_lzh.get_rmse_rrmse(
    allday['GPP'], allday_pred_y)
axs[2, 2].text(0, 30, "RMSE=%.2f" % rmse + '\n' +
               "RRMSE=%.2f" % (rrmse * 100) + '%')


# ################site shangqiu###############################
# filepath = r'D:\Thesis2\data_processed\shangqiu'
# # 阴晴天
# allday=pd.read_csv(filepath+'/shangqiu_2017_sif_gpp_ref_vi.csv')
# sunny=allday[allday['CI']>0.5]
# cloudy=allday[allday['CI']<=0.5]
# # 选择时间范围
# idx=((sunny['DOY']%1)>=stime) & ((sunny['DOY']%1)<=etime)
# sunny=sunny.loc[idx,:]
# idx=((cloudy['DOY']%1)>=stime) & ((cloudy['DOY']%1)<=etime)
# cloudy=cloudy.loc[idx,:]
# # 新建Dataframe,只提取sif和gpp
# sunny = pd.concat([sunny['DOY'], sunny['SFMlinear'], sunny['GPP'],
#                    sunny['ref_nir'], sunny['PAR'], sunny['NDVI'],sunny['APAR'],sunny['CIgreen']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['DOY'], cloudy['SFMlinear'], cloudy['GPP'],
#                     cloudy['ref_nir'], cloudy['PAR'], cloudy['NDVI'],cloudy['APAR'],cloudy['CIgreen']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['SIF']=sunny['SFMlinear']
# cloudy['SIF']=cloudy['SFMlinear']
# sunny['fPARgreen']=sunny['CIgreen']*0.13-0.13
# cloudy['fPARgreen']=sunny['CIgreen']*0.13-0.13
# sunny['NIRv']=sunny['NDVI']*sunny['ref_nir']
# # sunny['fPAR']=sunny['APAR']/sunny['PAR']
# sunny['fesc']=sunny['NIRv']/sunny['fPARgreen']
# sunny['SIFesc']=sunny['SIF']/sunny['fesc']
# cloudy['NIRv']=cloudy['NDVI']*cloudy['ref_nir']
# # cloudy['fPAR']=cloudy['APAR']/cloudy['PAR']
# cloudy['fesc']=cloudy['NIRv']/cloudy['fPARgreen']
# cloudy['SIFesc']=cloudy['SIF']/cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x = sunny['SIF']
# y = sunny['GPP']
# a, b, pred_y = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# cloudy_pred_y = a * cloudy['SIF'] + b
# allday_pred_y = a * allday['SIF'] + b
# pred_y = pd.DataFrame(pred_y, columns=['sunny_pred_y'])

# x = cloudy['SIF']
# y = cloudy['GPP']
# a, b, pred_y1 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y1 = pd.DataFrame(pred_y1, columns=['cloudy_pred_y'])

# x = allday['SIF']
# y = allday['GPP']
# a, b, pred_y2 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y2 = pd.DataFrame(pred_y2, columns=['allday_pred_y'])
# # 显示结果
# fig, axs = plt.subplots(3, 3, figsize=(10, 10))
# fig.subplots_adjust(hspace=0.4)
# funcs_lzh.plot_xy(sunny['SIF'], sunny['GPP'],
#                   'SIF_sunny', 'GPP_sunny', axs[0, 0])
# # axs[0,0].set_xlim([0,0.0022])
# funcs_lzh.plot_xy(sunny['GPP'], pred_y['sunny_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[0, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     sunny['GPP'], pred_y['sunny_pred_y'])
# axs[0, 1].text(0, 50, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# funcs_lzh.plot_xy(cloudy['SIF'], cloudy['GPP'],
#                   'SIF_cloudy', 'GPP_cloudy', axs[1, 0])
# # axs[1,0].set_xlim([0,0.0022])
# funcs_lzh.plot_xy(cloudy['GPP'], pred_y1['cloudy_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[1, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy['GPP'], pred_y1['cloudy_pred_y'])
# axs[1, 1].text(0, 28, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# # axs[1,1].set_xlim([-2,55])
# funcs_lzh.plot_xy(cloudy['GPP'],
#                   cloudy_pred_y, 'GPP_mea', 'GPP_pre', axs[1, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy['GPP'], cloudy_pred_y)
# axs[1, 2].text(0, 35, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# # axs[1,2].set_xlim([-2,55])

# funcs_lzh.plot_xy(allday['SIF'], allday[
#                   'GPP'], 'SIF_all', 'GPP_all', axs[2, 0])
# # axs[2,0].set_xlim([0,0.0022])
# funcs_lzh.plot_xy(allday['GPP'], pred_y2['allday_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[2, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday['GPP'], pred_y2['allday_pred_y'])
# axs[2, 1].text(0, 50, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# funcs_lzh.plot_xy(allday['GPP'],
#                   allday_pred_y, 'GPP_mea', 'GPP_pre', axs[2, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday['GPP'], allday_pred_y)
# axs[2, 2].text(0, 50, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# # 消除冠层结构的影响会怎样？
# # ------------------------------------------------------------
# # 建立线性回归模型
# x = sunny['SIFesc']
# y = sunny['GPP']
# a, b, pred_y = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# cloudy_pred_y = a * cloudy['SIFesc'] + b
# allday_pred_y = a * allday['SIFesc'] + b
# pred_y = pd.DataFrame(pred_y, columns=['sunny_pred_y'])

# x = cloudy['SIFesc']
# y = cloudy['GPP']
# a, b, pred_y1 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y1 = pd.DataFrame(pred_y1, columns=['cloudy_pred_y'])

# x = allday['SIFesc']
# y = allday['GPP']
# a, b, pred_y2 = funcs_lzh.get_lingre(x.reshape(-1, 1), y)
# pred_y2 = pd.DataFrame(pred_y2, columns=['allday_pred_y'])
# # 显示结果
# fig, axs = plt.subplots(3, 3, figsize=(10, 10))
# fig.subplots_adjust(hspace=0.4)
# funcs_lzh.plot_xy(sunny['SIFesc'], sunny['GPP'],
#                   'SIF_sunny', 'GPP_sunny', axs[0, 0])
# # axs[0,0].set_xlim([0,0.005])
# funcs_lzh.plot_xy(sunny['GPP'], pred_y['sunny_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[0, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     sunny['GPP'], pred_y['sunny_pred_y'])
# axs[0, 1].text(0, 50, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

# funcs_lzh.plot_xy(cloudy['SIFesc'], cloudy['GPP'],
#                   'SIF_cloudy', 'GPP_cloudy', axs[1, 0])
# # axs[1,0].set_xlim([0,0.006])
# funcs_lzh.plot_xy(cloudy['GPP'], pred_y1['cloudy_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[1, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy['GPP'], pred_y1['cloudy_pred_y'])
# axs[1, 1].text(0, 25, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# # axs[1,1].set_xlim([-2,55])
# funcs_lzh.plot_xy(cloudy['GPP'],
#                   cloudy_pred_y, 'GPP_mea', 'GPP_pre', axs[1, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     cloudy['GPP'], cloudy_pred_y)
# axs[1, 2].text(0, 38, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# # axs[1,2].set_xlim([-2,55])

# funcs_lzh.plot_xy(allday['SIFesc'], allday[
#                   'GPP'], 'SIF_all', 'GPP_all', axs[2, 0])
# # axs[2,0].set_xlim([0,0.006])
# funcs_lzh.plot_xy(allday['GPP'], pred_y2['allday_pred_y'],
#                   'GPP_mea_self', 'GPP_pre_self', axs[2, 1])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday['GPP'], pred_y2['allday_pred_y'])
# axs[2, 1].text(0, 50, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')
# funcs_lzh.plot_xy(allday['GPP'],
#                   allday_pred_y, 'GPP_mea', 'GPP_pre', axs[2, 2])
# rmse, rrmse = funcs_lzh.get_rmse_rrmse(
#     allday['GPP'], allday_pred_y)
# axs[2, 2].text(0, 50, "RMSE=%.2f" % rmse + '\n' +
#                "RRMSE=%.2f" % (rrmse * 100) + '%')

plt.show()
