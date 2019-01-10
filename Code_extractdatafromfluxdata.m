filepath='D:\Thesis2\data_processed\harvard\useless';
datapar=importdata([filepath '\HarvardBarnTower_data_2013_2014.xlsx']);
doy=datapar.data(:,5);
year=datapar.data(:,1);
idx2013=year==2013 & doy>=170 & doy<300;
data2013=datapar.data(idx2013,:);
idx2014=year==2014 & doy>=127 & doy<300;
data2014=datapar.data(idx2014,:);
% halfhourly
xlswrite('USHa1_2013_halfhourly.xlsx',datapar.textdata,1,'A1');
xlswrite('USHa1_2013_halfhourly.xlsx',data2013,1,'A2');
xlswrite('USHa1_2014_halfhourly.xlsx',datapar.textdata,1,'A1');
xlswrite('USHa1_2014_halfhourly.xlsx',data2014,1,'A2');
% hourly
T=[];
for i=1:2:size(data2013,1)
    t=nanmean(data2013(i:i+1,:));
    T=[T;t];
end
T1=[];
for i=1:2:size(data2014,1)
    t=nanmean(data2014(i:i+1,:));
    T1=[T1;t];
end

xlswrite('USHa1_2013_hourly.xlsx',datapar.textdata,1,'A1');
xlswrite('USHa1_2013_hourly.xlsx',T,1,'A2');
xlswrite('USHa1_2014_hourly.xlsx',datapar.textdata,1,'A1');
xlswrite('USHa1_2014_hourly.xlsx',T1,1,'A2');
% extract gpp
datagpp=importdata('D:\Thesis2\data\AMF_USHa1_2013_L2_GF_V010 (2).csv');
data=datagpp.data(2:end,:);
doy=data(:,3);
year=data(:,1);
idx2013=year==2013 & doy>=170 & doy<300;
data2013=data(idx2013,:);
title=datagpp.textdata{18,1};
title=strsplit(title,',');
xlswrite('USHa1_2013gpp_hourly.xlsx',title,1,'A1');
xlswrite('USHa1_2013gpp_hourly.xlsx',datagpp.colheaders,1,'A2');
xlswrite('USHa1_2013gpp_hourly.xlsx',data2013,1,'A3');

datagpp=importdata('D:\Thesis2\data\AMF_USHa1_2014_L2_GF_V010 (1).csv');
data=datagpp.data(2:end,:);
doy=data(:,3);
year=data(:,1);
idx2014=year==2014 & doy>=127 & doy<300;
data2014=data(idx2014,:);
title=datagpp.textdata{18,1};
title=strsplit(title,',');
xlswrite('USHa1_2014gpp_hourly.xlsx',title,1,'A1');
xlswrite('USHa1_2014gpp_hourly.xlsx',datagpp.colheaders,1,'A2');
xlswrite('USHa1_2014gpp_hourly.xlsx',data2014,1,'A3');
% get sif hourly 2013,2014
datasif2013=xlsread('D:\Thesis2\data_processed\harvard\useless\SIF_30min_HF_Barn_2013.xlsx');
T=[];
for i=1:2:size(datasif2013,1)
    t=nanmean(datasif2013(i:i+1,:));
    T=[T;t];
end
xlswrite('USHa1_2013sif_hourly.xlsx',{'DOY','SIF'},1,'A1');
xlswrite('USHa1_2013sif_hourly.xlsx',T,1,'A2');

