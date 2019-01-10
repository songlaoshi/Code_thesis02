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
# idx=(sunny['hour']>=10.9/24) & (sunny['hour']<=13.1/24)
# sunny=sunny.loc[idx,:]
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


plt.show()
