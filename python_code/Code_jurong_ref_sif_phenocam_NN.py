#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-22 16:15:48
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPRegressor  # 多层线性回归
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import cv2

filepath = r'D:\Data2018\jr2018\Results'
data = pd.read_csv(filepath + '/ref_sif_par_all.csv')
data.loc[data['SFMlinear'] == 0, 'SFMlinear'] = np.nan
data.loc[(np.fix(data['doy']) == 216) | (
    np.fix(data['doy']) == 275), :] = np.nan
data = data.dropna()
data.index = range(len(data.index))
data['sifyield'] = data['SFMlinear'] / data['Rg']

# data.to_csv(filepath + '/' + 'ref_sif_par_all_clean.csv', header=True,
# index=False)

# plt.figure()
# plt.scatter(data['doy'],data['blue'])

x = data.loc[:, ['blue', 'green', 'red', 'nir', 'Rg']]
y = data['SFMlinear']
x_train, x_test, y_trian, y_test = train_test_split(x, y, test_size=0.25)

x_train_scaler = StandardScaler().fit(x_train)
standardized_x_train = x_train_scaler.transform(x_train)
x_test_scaler = StandardScaler().fit(x_test)
standardized_x_test = x_test_scaler.transform(x_test)


# solver='lbfgs', MLP的求解方法：L-BFGS在小数据上表现较好，Adom较为鲁棒
# SGD在参数调整优化时会有最佳表现
# alpha： L2的参数，MLP支持正则化
# hidden_layer_sizes=(5),一层隐含层，5个神经元。[(5,2):两层隐含层，第一层5个，第二层2个]
clf = MLPRegressor(solver='lbfgs', alpha=1e-5,
                   hidden_layer_sizes=(5), random_state=1)
#
clf.fit(standardized_x_train, y_trian)
# #
y_train_pred = clf.predict(standardized_x_train)
y_test_pred = clf.predict(standardized_x_test)

plt.figure()
r, p = pearsonr(y_trian, y_train_pred)
plt.scatter(y_trian, y_train_pred, label='TrainData,' +
            'r2= ' + '%.2f' % np.square(r), c='k')
r, p = pearsonr(y_test, y_test_pred)
plt.scatter(y_test, y_test_pred, label='TestData,' +
            'r2= ' + '%.2f' % np.square(r), c='gray')
plt.xlabel('SIF_measured')
plt.ylabel('SIF_predicted')
plt.grid()
plt.legend()
plt.savefig(r'D:\Thesis2\imgdata\sif2' + '/' + 'train_test.png')
# plt.show()

#
filecsv = os.listdir('D:\Thesis2\imgdata\csvfiles')
for i in range(37,len(filecsv)): #len(filecsv)
	savefilename = filecsv[i][0:-4] + '.png'
	imgdata = pd.read_csv(r'D:\Thesis2\imgdata\csvfiles' + '/' + filecsv[i])
	x = imgdata
	x_scaler = StandardScaler().fit(x)
	standardized_x_train = x_scaler.transform(x)
	y_pred = clf.predict(standardized_x_train)
	y_pred = y_pred.reshape(960, 1296)
	newg = np.ones(y_pred.shape)
	newr = np.ones(y_pred.shape)
	y_pred[y_pred < 0.2] = np.nan
	y_pred[y_pred > 4] = np.nan
	plt.figure(figsize=(10,10))
	plt.imshow(y_pred,cmap='hot')
	plt.xticks([])
	plt.yticks([])
	plt.colorbar()
	plt.savefig(r'D:\Thesis2\imgdata\sif2'+'/'+savefilename)

	print(savefilename +' is ok....')


# imgdata=pd.read_csv(filepath+'/img_data.csv')
# x=imgdata
# x_scaler=StandardScaler().fit(x)
# standardized_x_train=x_scaler.transform(x)
# y_pred=clf.predict(standardized_x_train)
# y_pred=y_pred.reshape(960,1296)
# newg=np.ones(y_pred.shape)
# newr=np.ones(y_pred.shape)
# y_pred[y_pred<0.2]=np.nan
# y_pred[y_pred>4]=np.nan

# plt.imshow(y_pred,cmap='hot')
# plt.xticks([])
# plt.yticks([])
# plt.colorbar()
# plt.show()

# cv2.imshow("Image",imgrgb)
# cv2.waitKey(0)

