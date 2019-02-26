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


class Date_data():
    """docstring for ClassName"""

    def __init__(self, year=0, mon=0, day=0, hour=0, mins=0, sec=0, doy=0):
        self.year = year
        self.mon = mon
        self.day = day
        self.hour = hour
        self.mins = mins
        self.sec = sec
        self.doy = doy


def get_time(filename, a):
    t = filename.split('_')
    a.year = int(t[1])
    a.mon = int(t[2])
    a.day = int(t[3])
    a.hour = int(t[4][0:2])
    a.mins = int(t[4][2:4])
    a.sec = int(t[4][4:6])
    a.doy = datetime.date(a.year, a.mon, a.day).timetuple().tm_yday
    return a


def get_frac_bias(x1, x2, y, allday, iter_num, sample_frac, ci_label, ci_threshold):
    '''
    计算x,y的阴天比例frac和gpp估算bias
    x1是SIF,x2是SIFesc
    '''
    a1, b1, pred_y1 = funcs_lzh.get_lingre(x1.values.reshape(-1, 1), y)
    a2, b2, pred_y2 = funcs_lzh.get_lingre(x2.values.reshape(-1, 1), y)
    frac = []
    bias1 = []
    bias2 = []
    for i in range(iter_num):
        sample = allday.sample(frac=sample_frac, replace=True, axis=0)
        allday_pred_y_x1 = a1 * sample[x1.name] + b1
        allday_pred_y_x2 = a2 * sample[x2.name] + b2
        bias_1 = sum(allday_pred_y_x1 - sample[y.name]) / (sample.shape[0])
        bias_2 = sum(allday_pred_y_x2 - sample[y.name]) / (sample.shape[0])
        sample_cloudy = sample.loc[sample[ci_label] <= ci_threshold, :]
        frac.append(sample_cloudy.shape[0] / sample.shape[0])
        bias1.append(bias_1)
        bias2.append(bias_2)
    return frac, bias1, bias2


def get_mean_std(x):
    mean_x = np.mean(x)
    std_x = np.mean(x)

def get_alpha_refPvalue(p):
	alpha=[]
	for i in p:
		if i<0.01:
			alpha.append(1)
		else:
			alpha.append(0.5)
	return alpha

# 全局变量
stime = 8.9 / 24
etime = 16.1 / 24
ci_threshold = 0.5
# 字体格式
ticklabelsize = 14
axis_font = {'fontname': 'Arial', 'size': 14}
legend_font = {'fontname': 'Arial', 'size': 14}
# ################site harvard###############################
# filepath = r'D:\Thesis2\data_processed\harvard'
# # 合并2013,2014年的数据,区分阴晴天
# data2013 = pd.read_csv(
#     filepath + '/USHa1_2013apar_sif_gpp_metho_hourly_8-18.csv')
# data2014 = pd.read_csv(
#     filepath + '/USHa1_2014apar_sif_gpp_metho_hourly_8-18.csv')
# dataall = pd.concat([data2013, data2014], axis=0)
# sunny = dataall.loc[(dataall['clear_index'] > ci_threshold), :]
# cloudy = dataall.loc[(dataall['clear_index'] <= ci_threshold), :]
# # 选择时间范围
# idx = (sunny['hour'] >= stime) & (sunny['hour'] <= etime)
# sunny = sunny.loc[idx, :]
# idx = (cloudy['hour'] >= stime) & (cloudy['hour'] <= etime)
# cloudy = cloudy.loc[idx, :]
# # 新建Dataframe,只提取sif和gpp
# sunny = pd.concat([sunny['doy'], sunny['SIF'], sunny[' GPP( umol/m2/s)'],
#                    sunny['r.750'], sunny['incident.ppfd'], sunny['ndvi.r'], sunny['apar'], sunny['clear_index']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['doy'], cloudy['SIF'], cloudy[' GPP( umol/m2/s)'],
#                     cloudy['r.750'], cloudy['incident.ppfd'], cloudy['ndvi.r'], cloudy['apar'], cloudy['clear_index']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['NIRv'] = sunny['ndvi.r'] * sunny['r.750']
# sunny['fPAR'] = sunny['apar'] / sunny['incident.ppfd']
# sunny['fesc'] = sunny['NIRv'] / sunny['fPAR']
# sunny['SIFesc'] = sunny['SIF'] / sunny['fesc']
# cloudy['NIRv'] = cloudy['ndvi.r'] * cloudy['r.750']
# cloudy['fPAR'] = cloudy['apar'] / cloudy['incident.ppfd']
# cloudy['fesc'] = cloudy['NIRv'] / cloudy['fPAR']
# cloudy['SIFesc'] = cloudy['SIF'] / cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x1 = sunny['SIF']
# x2 = sunny['SIFesc']
# y = sunny[' GPP( umol/m2/s)']

# frac, bias1,bias2 = get_frac_bias(
# x1, x2,y, allday, iter_num=1000, sample_frac=0.9, ci_label='clear_index',
# ci_threshold=0.5)

# result_har = pd.DataFrame(np.vstack([frac, bias1,bias2]).T, columns=[
#                           'frac', 'bias', 'bias_esc'])
# ################site Avignon###############################
# filepath = r'D:\Thesis2\data_processed\avignon'
# # 阴晴天
# dataall = pd.read_csv(
#     filepath + '/AV2010db1_sifclean_8-18_ref.csv')
# sunny = dataall.loc[(dataall['clear_index'] > ci_threshold), :]
# cloudy = dataall.loc[(dataall['clear_index'] <= ci_threshold), :]
# # 选择时间范围
# idx = ((sunny['DOY'] % 1) >= stime) & ((sunny['DOY'] % 1) <= etime)
# sunny = sunny.loc[idx, :]
# idx = ((cloudy['DOY'] % 1) >= stime) & ((cloudy['DOY'] % 1) <= etime)
# cloudy = cloudy.loc[idx, :]
# #
# sunny['apar'] = sunny['fAPAR'] * sunny['PAR']
# cloudy['apar'] = cloudy['fAPAR'] * cloudy['PAR']
# # 新建Dataframe,只提取sif和gpp
# sunny = pd.concat([sunny['DOY'], sunny['SIF760'], sunny['GPP'],
#                    sunny['Veg_reflectance_750_760'], sunny['PAR'], sunny['NDVI'], sunny['apar'], sunny['clear_index']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['DOY'], cloudy['SIF760'], cloudy['GPP'],
#                     cloudy['Veg_reflectance_750_760'], cloudy['PAR'], cloudy['NDVI'], cloudy['apar'], cloudy['clear_index']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['SIF'] = sunny['SIF760']
# cloudy['SIF'] = cloudy['SIF760']
# sunny['NIRv'] = sunny['NDVI'] * sunny['Veg_reflectance_790_800']
# sunny['fPAR'] = sunny['apar'] / sunny['PAR']
# sunny['fesc'] = sunny['NIRv'] / sunny['fPAR']
# sunny['SIFesc'] = sunny['SIF'] / sunny['fesc']
# cloudy['NIRv'] = cloudy['NDVI'] * cloudy['Veg_reflectance_790_800']
# cloudy['fPAR'] = cloudy['apar'] / cloudy['PAR']
# cloudy['fesc'] = cloudy['NIRv'] / cloudy['fPAR']
# cloudy['SIFesc'] = cloudy['SIF'] / cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x1 = sunny['SIF']
# x2 = sunny['SIFesc']
# y = sunny['GPP']
# frac, bias1,bias2 = get_frac_bias(
# x1, x2,y, allday, iter_num=1000, sample_frac=0.9, ci_label='clear_index',
# ci_threshold=0.5)

# result_avi = pd.DataFrame(np.vstack([frac, bias1,bias2]).T, columns=[
#                           'frac', 'bias', 'bias_esc'])
# ###############site shangqiu###############################
# filepath = r'D:\Thesis2\data_processed\shangqiu'
# # 阴晴天
# allday = pd.read_csv(filepath + '/shangqiu_2017_sif_gpp_ref_vi.csv')
# sunny = allday[allday['CI'] > ci_threshold]
# cloudy = allday[allday['CI'] <= ci_threshold]
# # 选择时间范围
# idx = ((sunny['DOY'] % 1) >= stime) & ((sunny['DOY'] % 1) <= etime)
# sunny = sunny.loc[idx, :]
# idx = ((cloudy['DOY'] % 1) >= stime) & ((cloudy['DOY'] % 1) <= etime)
# cloudy = cloudy.loc[idx, :]
# # 新建Dataframe,只提取sif和gpp
# sunny = pd.concat([sunny['DOY'], sunny['SFMlinear'], sunny['GPP'],
#                    sunny['ref_nir'], sunny['PAR'], sunny['NDVI'], sunny['APAR'], sunny['CIgreen'], sunny['CI']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['DOY'], cloudy['SFMlinear'], cloudy['GPP'],
#                     cloudy['ref_nir'], cloudy['PAR'], cloudy['NDVI'], cloudy['APAR'], cloudy['CIgreen'], cloudy['CI']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['SIF'] = sunny['SFMlinear']
# cloudy['SIF'] = cloudy['SFMlinear']
# sunny['fPARgreen'] = sunny['CIgreen'] * 0.13 - 0.13
# cloudy['fPARgreen'] = cloudy['CIgreen'] * 0.13 - 0.13
# sunny['NIRv'] = sunny['NDVI'] * sunny['ref_nir']
# # sunny['fPAR']=sunny['APAR']/sunny['PAR']
# sunny['fesc'] = sunny['NIRv'] / sunny['fPARgreen']
# sunny['SIFesc'] = sunny['SIF'] / sunny['fesc']
# cloudy['NIRv'] = cloudy['NDVI'] * cloudy['ref_nir']
# # cloudy['fPAR']=cloudy['APAR']/cloudy['PAR']
# cloudy['fesc'] = cloudy['NIRv'] / cloudy['fPARgreen']
# cloudy['SIFesc'] = cloudy['SIF'] / cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x1 = sunny['SIF']
# x2 = sunny['SIFesc']
# y = sunny['GPP']
# frac, bias1,bias2 = get_frac_bias(
# x1, x2,y, allday, iter_num=1000, sample_frac=0.9, ci_label='CI',
# ci_threshold=0.5)

# result_sha = pd.DataFrame(np.vstack([frac, bias1,bias2]).T, columns=[
#                           'frac', 'bias', 'bias_esc'])
# ################site shangqiu 2018 wheat###############################
# filepath = r'D:\Thesis2\data_processed\shangqiu'
# # 阴晴天
# allday = pd.ExcelFile(filepath + '/SIF_GPP_VI_ref_halfhourmean_sq2018wheat.xlsx')
# allday=allday.parse(0)
# allday['clear_index']=allday['RD_0_0_1(W/m2)']/allday['Rg(W/m2)']
# sunny = allday[allday['clear_index'] > ci_threshold]
# cloudy = allday[allday['clear_index'] <= ci_threshold]
# # 选择时间范围
# idx = ((sunny['DOY'] % 1) >= stime) & ((sunny['DOY'] % 1) <= etime)
# sunny = sunny.loc[idx, :]
# idx = ((cloudy['DOY'] % 1) >= stime) & ((cloudy['DOY'] % 1) <= etime)
# cloudy = cloudy.loc[idx, :]
# # 新建Dataframe,只提取sif和gpp
# sunny = pd.concat([sunny['DOY'], sunny['SFM'], sunny['GPP_gapfilled'],
#                    sunny['ref_nir'], sunny['PPFD_1_1_3'], sunny['NDVI'], sunny['APAR'], sunny['CIgreen'], sunny['clear_index']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['DOY'], cloudy['SFM'], cloudy['GPP_gapfilled'],
#                     cloudy['ref_nir'], cloudy['PPFD_1_1_3'], cloudy['NDVI'], cloudy['APAR'], cloudy['CIgreen'], cloudy['clear_index']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['SIF'] = sunny['SFM']
# cloudy['SIF'] = cloudy['SFM']
# sunny['fPARgreen'] = sunny['CIgreen'] * 0.13 - 0.13
# cloudy['fPARgreen'] = cloudy['CIgreen'] * 0.13 - 0.13
# sunny['NIRv'] = sunny['NDVI'] * sunny['ref_nir']
# # sunny['fPAR']=sunny['APAR']/sunny['PAR']
# sunny['fesc'] = sunny['NIRv'] / sunny['fPARgreen']
# sunny['SIFesc'] = sunny['SIF'] / sunny['fesc']
# cloudy['NIRv'] = cloudy['NDVI'] * cloudy['ref_nir']
# # cloudy['fPAR']=cloudy['APAR']/cloudy['PAR']
# cloudy['fesc'] = cloudy['NIRv'] / cloudy['fPARgreen']
# cloudy['SIFesc'] = cloudy['SIF'] / cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x1 = sunny['SIF']
# x2 = sunny['SIFesc']
# y = sunny['GPP_gapfilled']
# frac, bias1,bias2 = get_frac_bias(
# x1, x2,y, allday, iter_num=1000, sample_frac=0.9, ci_label='clear_index',
# ci_threshold=0.5)

# result_sha_2018wt = pd.DataFrame(np.vstack([frac, bias1,bias2]).T, columns=[
#                           'frac', 'bias', 'bias_esc'])
# ################site Majadas2017 grassland###############################
# filepath = r'D:\Thesis2\data_processed\spain'
# # 阴晴天
# allday = pd.ExcelFile(
#     filepath + '/Majadas2017-Eddy_and_Flox_droptime_sifclean_8-18_norain.xlsx')
# allday = allday.parse(0)
# # 去掉近红外（此处选用790nm）反射率大于1的值
# allday.loc[allday['Reflectance_790_mean'] > 1, 'Reflectance_790_mean'] = np.nan
# allday = allday.dropna()
# #
# allday['tempdoy'] = allday['new_DOY'] + 15 / 60  # 时间变成半小时
# sunny = allday[allday['CI'] > ci_threshold]
# cloudy = allday[allday['CI'] <= ci_threshold]
# # 选择时间范围
# idx = ((sunny['tempdoy'] % 1) >= stime) & ((sunny['tempdoy'] % 1) <= etime)
# sunny = sunny.loc[idx, :]
# idx = ((cloudy['tempdoy'] % 1) >= stime) & ((cloudy['tempdoy'] % 1) <= etime)
# cloudy = cloudy.loc[idx, :]
# # 新建Dataframe,只提取sif和gpp
# sunny = pd.concat([sunny['tempdoy'], sunny['SIF_A_sfm_mean'], sunny['GPP_MR_f_Subcanopy'],
#                    sunny['Reflectance_790_mean'], sunny['PARd_North'], sunny['NDVI_mean'],
#                     sunny['CI']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['tempdoy'], cloudy['SIF_A_sfm_mean'], cloudy['GPP_MR_f_Subcanopy'],
#                     cloudy['Reflectance_790_mean'], cloudy['PARd_North'], cloudy['NDVI_mean'],
#                     cloudy['CI']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['SIF'] = sunny['SIF_A_sfm_mean']
# cloudy['SIF'] = cloudy['SIF_A_sfm_mean']
# sunny['fPARgreen'] = sunny['NDVI_mean'] * 1.11 - 0.29
# cloudy['fPARgreen'] = cloudy['NDVI_mean'] * 1.11 - 0.29
# # fAPARchl_ndvi = 1.11 * NDVI - 0.29
# # fAPARchl_evi = 1.3 * EVI - 0.18
# sunny['NIRv'] = sunny['NDVI_mean'] * sunny['Reflectance_790_mean']
# # sunny['fPAR']=sunny['APAR']/sunny['PAR']
# sunny['fesc'] = sunny['NIRv'] / sunny['fPARgreen']
# sunny['SIFesc'] = sunny['SIF'] / sunny['fesc']
# cloudy['NIRv'] = cloudy['NDVI_mean'] * cloudy['Reflectance_790_mean']
# # cloudy['fPAR']=cloudy['APAR']/cloudy['PAR']
# cloudy['fesc'] = cloudy['NIRv'] / cloudy['fPARgreen']
# cloudy['SIFesc'] = cloudy['SIF'] / cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x1 = sunny['SIF_A_sfm_mean']
# x2 = sunny['SIFesc']
# y = sunny['GPP_MR_f_Subcanopy']
# frac, bias1, bias2 = get_frac_bias(
#     x1, x2, y, allday, iter_num=1000, sample_frac=0.9, ci_label='CI',
#     ci_threshold=0.5)

# result_maj_2017gr = pd.DataFrame(np.vstack([frac, bias1, bias2]).T, columns=[
#     'frac', 'bias', 'bias_esc'])
# ################site jurong 2018 rice paddy###############################
# filepath = r'D:\Thesis2\data_processed\jurong'
# # 阴晴天
# allday = pd.ExcelFile(filepath + '/SIF_GPP_VI_ref_halfhourmean_jr2018rice.xlsx')
# allday=allday.parse(0)

# allday['clear_index']=allday['Diff(W/m2)']/allday['Total(W/m2)']
# sunny = allday[allday['clear_index'] > ci_threshold]
# cloudy = allday[allday['clear_index'] <= ci_threshold]
# # ----------------晴空指数有大于1的怎么办？（此处去掉了）
# allday.loc[allday['clear_index']>1,'clear_index']=np.nan
# allday=allday.dropna()
# # 选择时间范围
# idx = ((sunny['DOY'] % 1) >= stime) & ((sunny['DOY'] % 1) <= etime)
# sunny = sunny.loc[idx, :]
# idx = ((cloudy['DOY'] % 1) >= stime) & ((cloudy['DOY'] % 1) <= etime)
# cloudy = cloudy.loc[idx, :]
# # 新建Dataframe,只提取sif和gpp
# # ----------------没有足够的总PPFD，此处用Rg代替
# # ----------------没有APAR，此处用CIgreen算
# sunny = pd.concat([sunny['DOY'], sunny['SFM'], sunny['GPP_gapfilled'],
#                    sunny['ref_nir'], sunny['Total(W/m2)'], sunny['NDVI'] ,sunny['CIgreen'], sunny['clear_index']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['DOY'], cloudy['SFM'], cloudy['GPP_gapfilled'],
#                     cloudy['ref_nir'], cloudy['Total(W/m2)'], cloudy['NDVI'],cloudy['CIgreen'], cloudy['clear_index']], axis=1)
# cloudy = cloudy.dropna()
# # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # SIF冠层emission
# sunny['SIF'] = sunny['SFM']
# cloudy['SIF'] = cloudy['SFM']
# sunny['fPARgreen'] = sunny['CIgreen'] * 0.13 - 0.13
# cloudy['fPARgreen'] = cloudy['CIgreen'] * 0.13 - 0.13
# sunny['NIRv'] = sunny['NDVI'] * sunny['ref_nir']
# # sunny['fPAR']=sunny['APAR']/sunny['PAR']
# sunny['fesc'] = sunny['NIRv'] / sunny['fPARgreen']
# sunny['SIFesc'] = sunny['SIF'] / sunny['fesc']
# cloudy['NIRv'] = cloudy['NDVI'] * cloudy['ref_nir']
# # cloudy['fPAR']=cloudy['APAR']/cloudy['PAR']
# cloudy['fesc'] = cloudy['NIRv'] / cloudy['fPARgreen']
# cloudy['SIFesc'] = cloudy['SIF'] / cloudy['fesc']
# # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # ------------------------------------------------------------
# # 建立线性回归模型
# x1 = sunny['SIF']
# x2 = sunny['SIFesc']
# y = sunny['GPP_gapfilled']
# frac, bias1,bias2 = get_frac_bias(
# x1, x2,y, allday, iter_num=1000, sample_frac=0.9, ci_label='clear_index',
# ci_threshold=0.5)

# result_jur_2018ri = pd.DataFrame(np.vstack([frac, bias1,bias2]).T, columns=[
#                           'frac', 'bias', 'bias_esc'])
# ###############site jurong 2016 rice paddy###############################
# filepath = r'D:\Thesis2\data_processed\jurong'
# # 阴晴天
# allday = pd.ExcelFile(filepath + '/jurong2016_sifclean_8-18_ref_norain.xlsx')
# allday = allday.parse(0)
# # 计算clear_index
# a=Date_data()
# # a=date_data('','','','','','','') #定义结构体对象
# hour=((allday['DOY-3Digit']%1)*24).values
# mins=np.zeros(allday['DOY-3Digit'].shape)
# sec=mins
# doy=allday['Day'].values
# # location of jurong site
# lat=31.8068
# lon=119.2173

# Ro=[]
# for i in range(len(doy)):
# 	a.hour=hour[i]
# 	a.min=mins[i]
# 	a.sec=sec[i]
# 	a.doy=doy[i]
# 	Ro.append(funcs_lzh.get_par(a,lon,lat))

# allday['clear_index']=allday['SWin_1_1_1']/Ro
# allday.loc[(allday['clear_index']>1) | (allday['clear_index']<0),'clear_index']=np.nan
# allday['CIgreen']=allday['Ref_790_800_Reflectance']/allday['Ref_560_570_Reflectance']-1
# # allday.to_csv(r'D:\Thesis2\data_processed\jurong\jurong2016_sifclean_8-18_ref_norain_addCI.csv',index=False,header=True)

# sunny = allday[allday['clear_index'] > ci_threshold]
# cloudy = allday[allday['clear_index'] <= ci_threshold]
# # # ----------------晴空指数有大于1的怎么办？（此处去掉了）
# # allday.loc[allday['clear_index'] > 1, 'clear_index'] = np.nan
# # allday = allday.dropna()
# # # 选择时间范围
# idx = ((sunny['DOY-3Digit'] % 1) >= stime) & ((sunny['DOY-3Digit'] % 1) <= etime)
# sunny = sunny.loc[idx, :]
# idx = ((cloudy['DOY-3Digit'] % 1) >= stime) & ((cloudy['DOY-3Digit'] % 1) <= etime)
# cloudy = cloudy.loc[idx, :]
# # # 新建Dataframe,只提取sif和gpp
# # # ----------------没有足够的总PPFD，此处用Rg代替
# # # ----------------没有APAR，此处用CIgreen算
# sunny = pd.concat([sunny['DOY-3Digit'], sunny['SIF760'], sunny['GPP(umol CO2 m-2 s-1)'],
#                    sunny['Ref_790_800_Reflectance'], sunny['NDVI'], sunny['CIgreen'], sunny['clear_index']], axis=1)
# sunny = sunny.dropna()
# cloudy = pd.concat([cloudy['DOY-3Digit'], cloudy['SIF760'], cloudy['GPP(umol CO2 m-2 s-1)'],
#                     cloudy['Ref_790_800_Reflectance'], cloudy['NDVI'], cloudy['CIgreen'], cloudy['clear_index']], axis=1)
# cloudy = cloudy.dropna()
# # # 重新设置index，不然会有重复的index
# sunny = sunny.reset_index()
# cloudy = cloudy.reset_index()
# # # SIF冠层emission
# sunny['SIF'] = sunny['SIF760']
# cloudy['SIF'] = cloudy['SIF760']
# sunny['fPARgreen'] = sunny['CIgreen'] * 0.13 - 0.13
# cloudy['fPARgreen'] = cloudy['CIgreen'] * 0.13 - 0.13
# sunny['NIRv'] = sunny['NDVI'] * sunny['Ref_790_800_Reflectance']
# # # sunny['fPAR']=sunny['APAR']/sunny['PAR']
# sunny['fesc'] = sunny['NIRv'] / sunny['fPARgreen']
# sunny['SIFesc'] = sunny['SIF'] / sunny['fesc']
# cloudy['NIRv'] = cloudy['NDVI'] * cloudy['Ref_790_800_Reflectance']
# # # cloudy['fPAR']=cloudy['APAR']/cloudy['PAR']
# cloudy['fesc'] = cloudy['NIRv'] / cloudy['fPARgreen']
# cloudy['SIFesc'] = cloudy['SIF'] / cloudy['fesc']
# # # 晴天+阴天
# allday = pd.concat([sunny, cloudy], axis=0)
# allday = allday.reset_index()
# # # ------------------------------------------------------------
# # # 建立线性回归模型
# x1 = sunny['SIF']
# x2 = sunny['SIFesc']
# y = sunny['GPP(umol CO2 m-2 s-1)']
# frac, bias1, bias2 = get_frac_bias(
#     x1, x2, y, allday, iter_num=1000, sample_frac=0.9, ci_label='clear_index',
#     ci_threshold=0.5)

# result_jur_2016ri = pd.DataFrame(np.vstack([frac, bias1, bias2]).T, columns=[
#     'frac', 'bias', 'bias_esc'])
# # ----------save file --------------
# result_har.to_csv(r'D:\Thesis2\data_processed\Database bias\harvard.csv',index=False,header=True)
# result_avi.to_csv(r'D:\Thesis2\data_processed\Database bias\avignon.csv',index=False,header=True)
# result_sha.to_csv(r'D:\Thesis2\data_processed\Database bias\shangqiu.csv',index=False,header=True)
# result_sha_2018wt.to_csv(r'D:\Thesis2\data_processed\Database bias\shangqiu_2018wheat.csv',index=False,header=True)
# result_maj_2017gr.to_csv(r'D:\Thesis2\data_processed\Database bias\majadas_2017grass.csv',index=False,header=True)
# result_jur_2018ri.to_csv(r'D:\Thesis2\data_processed\Database bias\jurong_2018rice.csv',index=False,header=True)
# result_jur_2016ri.to_csv(r'D:\Thesis2\data_processed\Database bias\jurong_2016rice.csv',index=False,header=True)

# # # -------------plot ----------------
result_har = pd.read_csv(
    r'D:\Thesis2\data_processed\Database bias\harvard.csv')
result_avi = pd.read_csv(
    r'D:\Thesis2\data_processed\Database bias\avignon.csv')
result_sha = pd.read_csv(
    r'D:\Thesis2\data_processed\Database bias\shangqiu.csv')
result_sha_2018wt = pd.read_csv(
    r'D:\Thesis2\data_processed\Database bias\shangqiu_2018wheat.csv')
result_maj_2017gr = pd.read_csv(
    r'D:\Thesis2\data_processed\Database bias\majadas_2017grass.csv')
result_jru_2016ri = pd.read_csv(
    r'D:\Thesis2\data_processed\Database bias\jurong_2016rice.csv')
result_jru_2018ri = pd.read_csv(
    r'D:\Thesis2\data_processed\Database bias\jurong_2018rice.csv')

plt.figure()
plt.scatter(result_har['frac'], result_har['bias'],
            edgecolors='r', facecolors='', marker='o', label='Harvard_Forest', alpha=0.5)
plt.scatter(result_avi['frac'], result_avi['bias'],
            edgecolors='g', facecolors='', marker='s', label='Avignon_wheat', alpha=0.5)
plt.scatter(result_sha['frac'], result_sha['bias'],
            edgecolors='b', facecolors='', marker='D', label='Shangqiu_corn', alpha=0.5)
plt.scatter(result_sha_2018wt['frac'], result_sha_2018wt[
            'bias'], edgecolors='k', facecolors='', marker='v', label='Shangqiu_wheat', alpha=0.5)
plt.scatter(result_maj_2017gr['frac'], result_maj_2017gr['bias'],
            edgecolors='darkred', facecolors='', marker='^', label='Majadas_grass', alpha=0.5)
plt.scatter(result_jru_2016ri['frac'], result_jru_2016ri['bias'],
            edgecolors='magenta', facecolors='', marker='h', label='Jurong_rice2016', alpha=0.5)
plt.scatter(result_jru_2018ri['frac'], result_jru_2018ri['bias'],
            edgecolors='gold', facecolors='', marker='p', label='Jurong_rice2018', alpha=0.5)

plt.scatter(result_har['frac'], result_har['bias_esc'],
            edgecolors='tomato', facecolors='', marker='o', label='Harvard_esc', alpha=0.5)
plt.scatter(result_avi['frac'], result_avi['bias_esc'],
            edgecolors='lime', facecolors='', marker='s', label='Avignon_esc', alpha=0.5)
plt.scatter(result_sha['frac'], result_sha['bias_esc'],
            edgecolors='cyan', facecolors='', marker='D', label='Shangqiu_esc', alpha=0.5)
plt.scatter(result_sha_2018wt['frac'], result_sha_2018wt['bias_esc'],
            edgecolors='gray', facecolors='', marker='v', label='Shangqiu_wheat_esc', alpha=0.5)
plt.scatter(result_maj_2017gr['frac'], result_maj_2017gr['bias_esc'],
            edgecolors='salmon', facecolors='', marker='^', label='Majadas_grass_esc', alpha=0.5)
plt.scatter(result_jru_2016ri['frac'], result_jru_2016ri['bias_esc'],
            edgecolors='hotpink', facecolors='', marker='h', label='Jurong_rice2016_esc', alpha=0.5)
plt.scatter(result_jru_2018ri['frac'], result_jru_2018ri['bias_esc'],
            edgecolors='tan', facecolors='', marker='p', label='Jurong_rice2018_esc', alpha=0.5)

plt.xlabel('fraction of cloudy days', **axis_font)
plt.ylabel('$bias (GPP_{mod}-GPP_{mea})$', **axis_font)
# plt.title('SIFesc',**axis_font)
plt.tick_params(labelsize=ticklabelsize)
plt.legend()

##------------------------------------------
plt.figure(figsize=(23,5))
medianprops=dict(color='orange')
labels=['$Har$','$Har_{esc}$','$Avi$','$Avi_{esc}$','$Sha_{corn}$'
,'$Sha_{cornesc}$','$Sha_{wheat}$','$Sha_{wheatesc}$','$Maj$',
'$Maj_{esc}$','$Jur_{rice2016}$','$Jur_{rice2016esc}$',
'$Jur_{rice2018}$','$Jur_{rice2018esc}$']
plt.boxplot([result_har['bias'], result_har['bias_esc'], result_avi['bias'],
	result_avi['bias_esc'], result_sha['bias'], result_sha['bias_esc'],
	result_sha_2018wt['bias'], result_sha_2018wt['bias_esc'],
	result_maj_2017gr['bias'],result_maj_2017gr['bias_esc'],
	result_jru_2016ri['bias'],result_jru_2016ri['bias_esc'],
	result_jru_2018ri['bias'],result_jru_2018ri['bias_esc']],labels=labels,medianprops=medianprops)
plt.ylabel('$bias (GPP_{mod}-GPP_{mea})$', **axis_font,color='orange')
plt.tick_params(labelsize=ticklabelsize)
ax=plt.twinx()
medianprops=dict(color='r')
ax.boxplot([result_har['frac'], result_har['frac'], result_avi['frac'],
	result_avi['frac'], result_sha['frac'], result_sha['frac'],
	result_sha_2018wt['frac'], result_sha_2018wt['frac'],
	result_maj_2017gr['frac'],result_maj_2017gr['frac'],
	result_jru_2016ri['frac'],result_jru_2016ri['frac'],
	result_jru_2018ri['frac'],result_jru_2018ri['frac']],labels=labels,medianprops=medianprops)
ax.set_ylabel('fraction of cloudy days', **axis_font,color='r')
ax.tick_params(labelsize=ticklabelsize)
# # -------------------------------------------
t = pd.concat([result_har, result_avi, result_sha, result_sha_2018wt,
	result_maj_2017gr,result_jru_2016ri,result_jru_2018ri], axis=1)
tt = pd.concat([result_har, result_avi, result_sha, result_sha_2018wt,
	result_maj_2017gr,result_jru_2016ri,result_jru_2018ri], axis=0)

width = 0.2
tick_label=['$Har$','$Avi$','$Sha_{corn}$','$Sha_{wheat}$',
'$Maj$','$Jur_{rice2016}$','$Jur_{rice2018}$','all site']
R = []
p_value=[]
R_esc = []
p_esc=[]
plt.figure(figsize=(10,4))
for i in range(0, 21, 3):
    r, p = pearsonr(t.iloc[:, i], t.iloc[:, i + 1])
    R.append(r)
    p_value.append(p)
for i in range(0, 21, 3):
    r, p = pearsonr(t.iloc[:, i], t.iloc[:, i + 2])
    R_esc.append(r)
    p_esc.append(p)

rr, pp = pearsonr(tt.iloc[:, 0], tt.iloc[:, 1])
R.append(rr);p_value.append(pp)
rr, pp = pearsonr(tt.iloc[:, 0], tt.iloc[:, 2])
R_esc.append(rr);p_esc.append(pp)
x = np.arange(len(R))
# print(x, x + np.ones(len(x)) * width)
plt.bar(x, R, width=width, facecolor='k', label='SIF')
plt.bar(x + np.ones(len(x)) * width, R_esc, width=width,
        facecolor='gray', label='SIFesc', tick_label=tick_label)
plt.axhline(0, color='k')
plt.ylabel('r',**axis_font)
plt.tick_params(labelsize=ticklabelsize)
plt.legend()


plt.show()
