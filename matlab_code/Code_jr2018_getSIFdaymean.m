path='D:\Data2018\jr2018\Results';
[data,text]=xlsread([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18.xlsx']);
addpath('D:\Shared_Folder\Lzh py\SifAnalysis\SIF_GPP_reviewer\matlab_code');
addpath('D:\Data\Xilinhot2017 Code');
%% ¼ÆËãÌ«ÑôÌì¶¥½Ç
HS=[];
for i=1:size(data,1)
    DOY=fix(data(i,1));
    time=(data(i,1)-DOY)*24;
    HS=[HS;Solar_Altitude2(119.2173,31.8068,DOY,time)];
end
data=[data(:,1),data(:,3),HS];
%% È¥µôÌ«ÑôÌì¶¥½Ç>60µÄÊý¾Ý
data(data(:,end)>60,:)=[];
%%
Daymean=[];Daystd=[];
count1=1;
count2=1;
step=20;
for day=213:309
    idx=data(:,1)>=day & data(:,1)<day+1;
    temp=data(idx,:);
    sif_numnan=get_num_of_nan(temp(:,2));
    daymean=nanmean(temp,1);
    daystd=nanstd(temp,1);

    if sif_numnan.mor==5 || sif_numnan.noon==5 || sif_numnan.aft==5 || sif_numnan.all>=8
        daymean(1,2:end)=nan;
        daystd(1,2:end)=nan;
        count2=count2+1;
    end

    Daymean=[Daymean;[day,daymean(1,2:end)]];
    Daystd=[Daystd;[day,daystd(1,2:end)]];
    
end
title={'doy','3FLD','SZA'};
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],title,1,'A1');
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],Daymean,1,'A2');
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],title,2,'A1');
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],Daystd,2,'A2');

xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],title,1,'A1');
xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],Daymean,1,'A2');
xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],title,2,'A1');
xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],Daystd,2,'A2');
%% jurong2016ÈÕÆ½¾ù
data=xlsread('D:\Data\Jurong2016\SIF_jr2016_halfhour.xlsx');
Daymean=[];Daystd=[];
count1=1;
count2=1;
step=20;
for day=213:309
    idx=data(:,1)>=day & data(:,1)<day+1;
    temp=data(idx,:);
    sif_numnan=get_num_of_nan(temp(:,4));
    daymean=nanmean(temp,1);
    daystd=nanstd(temp,1);

%     if sif_numnan.mor==7 || sif_numnan.noon==7 || sif_numnan.aft==7 || sif_numnan.all>=10
%         daymean(1,2:end)=nan;
%         daystd(1,2:end)=nan;
%         count2=count2+1;
%     end

    Daymean=[Daymean;[day,daymean(1,2:end)]];
    Daystd=[Daystd;[day,daystd(1,2:end)]];
    
end
title={'doy','3FLD','SZA'};
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],title,1,'A1');
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],Daymean,1,'A2');
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],title,2,'A1');
% xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean.xlsx'],Daystd,2,'A2');

xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],title,1,'A1');
xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],Daymean,1,'A2');
xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],title,2,'A1');
xlswrite([path '\2018¾äÈÝË®µ¾_SIF_Half_hour_8-18_daymean_noszacontrol.xlsx'],Daystd,2,'A2');