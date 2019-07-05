#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-22 18:36:30
# @Author  : Lzh (lizhaoh2015@gmail.com)
# @Link    : http://songlaoshi.github.io
# @Version : $Id$

import os
import cv2
import pandas as pd 
import numpy as np 
import datetime
import funcs_lzh

datapath=r'D:\Thesis2\imgdata'
savepath=r'D:\Thesis2\imgdata\csvfiles'

class Date_data():
	"""docstring for ClassName"""
	def __init__(self,year=0,mon=0,day=0,hour=0,mins=0,sec=0,doy=0):
		self.year=year
		self.mon=mon
		self.day=day
		self.hour=hour
		self.mins=mins
		self.sec=sec
		self.doy=doy

		
def get_time(filename,a):
	t=filename.split('_')
	a.year=int(t[1])
	a.mon=int(t[2])
	a.day=int(t[3])
	a.hour=int(t[4][0:2])
	a.mins=int(t[4][2:4])
	a.sec=int(t[4][4:6])
	a.doy=datetime.date(a.year,a.mon,a.day).timetuple().tm_yday
	return a



fileir=os.listdir(datapath+'/ir')
filergb=os.listdir(datapath+'/rgb')
for i in range(len(fileir)): #len(fileir)
	savefilename=filergb[i][0:-4]+'.csv'
	imgnir=cv2.imread(datapath+'/ir/'+fileir[i])
	imgrgb=cv2.imread(datapath+'/rgb/'+filergb[i])
	b, g, r = cv2.split(imgrgb)
	nir=imgnir[:,:,0]
	b=b.reshape(-1,1)
	g=g.reshape(-1,1)
	r=r.reshape(-1,1)
	nir=nir.reshape(-1,1)
	sum_val=np.sum([b,g,r,nir],axis=0)
	b=b/sum_val
	g=g/sum_val
	r=r/sum_val
	nir=nir/sum_val
	
	a=Date_data()
	# a=date_data('','','','','','','') #定义结构体对象
	date_data=get_time(filergb[i],a)
	# location of jurong site
	lat=31.8068
	lon=119.2173
	Ro=funcs_lzh.get_par(date_data, lon, lat)
	par=Ro*np.ones(b.shape)

	t=pd.DataFrame(np.hstack([b,g,r,nir,par]),columns=['bule','green','red','nir','par'])
	t.to_csv(savepath+'/'+savefilename,index=False,header=True)

	print(savefilename+' is ok....')


# imgrgb = cv2.imread(datapath + '/' + 'jurong_2018_08_15_121405.jpg')
# b, g, r = cv2.split(imgrgb)
# imgnir=cv2.imread(datapath+'/'+'jurong_IR_2018_08_15_121405.jpg')
# nir=imgnir[:,:,0]

# b=b.reshape(-1,1)
# g=g.reshape(-1,1)
# r=r.reshape(-1,1)
# nir=nir.reshape(-1,1)

# sum_val=np.sum([b,g,r,nir],axis=0)
# b=b/sum_val
# g=g/sum_val
# r=r/sum_val
# nir=nir/sum_val

# par=1000*np.ones(b.shape)

# t=pd.DataFrame(np.hstack([b,g,r,nir,par]),columns=['bule','green','red','nir','par'])
# t.to_csv(datapath+'/img_data.csv',index=False,header=True)

