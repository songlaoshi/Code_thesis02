sifpath='D:\Data\shangqiu data\shang\Results\GPP_PAR_APAR_SIF_8_18\ALLnew';
vispath='D:\Data\shangqiu data\shang\Results_HRdata_recal';

[datasif text]=xlsread([sifpath '\GPP_VPD_Ta_Tleaf_SWC_PAR_APAR_rain_SIF_VI_NIRv_CI_SIFyield_LUE_halfhour.xlsx']);
[datavi text1]=xlsread([vispath '\VI_ref_addMTVI2_halfhourlymean_8-18.csv']);

datasifnew=[datasif(:,1:12),datasif(:,14:15),datasif(:,18),datasif(:,37)];


doyvi=datavi(:,1)+datavi(:,2)/24;

new=[];
for i=1:size(datasifnew,1)
    [num,idx]=min(abs(datasifnew(i,2)-doyvi));
    if num<1e-2
        new=[new;datasifnew(i,:),datavi(idx,:)];
    else
        new=[new;datasifnew(i,:),datavi(idx,:)*nan];
    end
end

title=[text(1:12),text(14:15),text(18),text(37),text1];

xlswrite([vispath '\SIF_GPP_VI_ref_halfhourmean_sq2017corn_8-18.xlsx'],title,1,'A1');
xlswrite([vispath '\SIF_GPP_VI_ref_halfhourmean_sq2017corn_8-18.xlsx'],new,1,'A2');