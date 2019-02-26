#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-01-11 17:22:48
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import numpy as np
import pandas as pd
import datetime

# functions


def get_matlab2py_doy(mattime):
    '''
    把matlab格式datenum时间转换成doy
    只能转换一个值，数组的话用map吧
    '''
    python_datetime = datetime.datetime.fromordinal(
        int(mattime) - 366) + datetime.timedelta(days=mattime % 1)
    doy = python_datetime.timetuple().tm_yday + mattime % 1
    return doy


def get_data(data):
    wl = data.columns[5:].values
    time = data['time'].values
    # 计算doy
    doy = list(map(get_matlab2py_doy, time))
    doy = pd.DataFrame(doy, columns=['doy'])
    # print(doy.shape)
    newdata = pd.concat([doy, data.iloc[:, 5:]], axis=1)
    # print(newdata.shape)
    return wl, newdata


def get_mean(wl, data, wl_range, step):
    '''
    求波长内的平均
    '''
    idx = (wl >= wl_range) & (wl < wl_range + step)
    # 注意要把data的index和idx个数保持一致，不然会把范围选错
    tdata = data.iloc[:, 1:]
    dataave = np.nanmean(tdata.loc[:, idx], axis=1)
    #
    dataave = pd.DataFrame(dataave, columns=['temp'])
    dataave.index = range(len(dataave))
    data.index = range(len(data))
    result = pd.concat([data['doy'], dataave['temp']], axis=1)
    return result


def get_halfmean(saveresult, stime, etime):
    '''
        求半小时平均
    '''
    hour = saveresult['doy'] % 1
    idxt = (hour >= stime / 24) & (hour < (stime + 0.5) / 24)
    Tdata = np.nanmean(saveresult.loc[idxt, :], axis=0)
    for t in np.arange(stime + 0.5, etime, 0.5):
        idxt = (hour >= t / 24) & (hour < (t + 0.5) / 24)
        tdata = np.nanmean(saveresult.loc[idxt, :], axis=0)
        Tdata = np.vstack([Tdata, tdata])
    Tdata = pd.DataFrame(Tdata, columns=saveresult.columns)
    # 修改时间为7-17半小时格式
    newhour = np.arange(stime, etime, 0.5) / 24
    t = newhour + np.ones(len(newhour)) * int(saveresult.iloc[0, 0])
    Tdata['doy'] = t
    return Tdata
    # print(Tdata.shape)

#
irradpath = r'D:\Data\jurong\jur\Results\Radiance\HR\Irradiance'
radpath = r'D:\Data\jurong\jur\Results\Radiance\HR\Radiance'
refpath = r'D:\Data\jurong\jur\Results\REF\HR_REF'
savepath = r'D:\Data\jurong\jur\Results\Database JR2017\2-Canopy radiances'

fileir = os.listdir(irradpath)
filera = os.listdir(radpath)
fileref = os.listdir(refpath)

step = 10
for wl_range in range(410, 900, step):
    print(str(wl_range) + '_' + str(wl_range + step) + ' start...')
    for i in range(len(fileir)):
        print(fileir[i] + ' start...')
        datair = pd.ExcelFile(irradpath + '/' + fileir[i])
        datair = datair.parse('Sheet1')
        datara = pd.ExcelFile(radpath + '/' + filera[i])
        datara = datara.parse('Sheet1')
        dataref = pd.ExcelFile(refpath + '/' + fileref[i])
        dataref = dataref.parse('Sheet1')
        # 计算均值
        wl, datair = get_data(datair)
        # print(datair.shape)
        resultir = get_mean(wl, datair, wl_range, step)
        # print(resultir.shape)
        wl, datara = get_data(datara)
        resultra = get_mean(wl, datara, wl_range, step)
        wl, dataref = get_data(dataref)
        resultref = get_mean(wl, dataref, wl_range, step)
        saveresult = pd.concat(
            [resultir, resultra['temp'], resultref['temp']], axis=1)

        wl_str = str(wl_range) + '_' + str(wl_range + step)
        saveresult.columns = ['doy', 'Veg_radiance_' + wl_str,
                                  'Ref_radiance_' + wl_str, 'Veg_reflectance_' + wl_str]
        # 筛选时间7-17点的
        hour = saveresult['doy'] % 1
        idx = (hour >= 7 / 24) & (hour < 17 / 24)
        saveresult = saveresult.loc[idx, :]
        # # 求半小时平均
        Tdata = get_halfmean(saveresult, 7, 17)
        if i==0:
            Saveresult = Tdata
        else:
            Saveresult = pd.concat([Saveresult, Tdata], axis=0)
            # print(Saveresult.shape)

    savename = 'Ref_' + wl_str + '.csv'
    Saveresult.to_csv(savepath + '/' + savename,
                      index=False, header=True)
