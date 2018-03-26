clear all; clc;
%% Read PV output data, 10 min resolution
% Type:M55, Installation capacity:53*18=954W @ Colomn AA
% Jan
P_Jan = xlsread('2001_01.xls','AA1:AA4464');% 31 days
for i = 1:31
    P01(i,:)=P_Jan(i*144-143:i*144);
end
clear P_Jan;
% Feb
P_Feb = xlsread('2001_02.xls','AA1:AA4032');% 28 days
for i = 1:28
    P02(i,:)=P_Feb(i*144-143:i*144);
end
clear P_Feb;
% Mar
P_Mar = xlsread('2001_03.xls','AA1:AA4464');% 31 days
for i = 1:31
    P03(i,:)=P_Mar(i*144-143:i*144);
end
clear P_Mar;
% Apr
P_Apr = xlsread('2001_04.xls','AA1:AA4320');% 30 days
for i = 1:30
    P04(i,:)=P_Apr(i*144-143:i*144);
end
clear P_Apr;
% May
P_May = xlsread('2001_05.xls','AA1:AA4464');% 31 days
for i = 1:31
    P05(i,:)=P_May(i*144-143:i*144);
end
clear P_May;
% Jun
P_Jun = xlsread('2001_06.xls','AA1:AA4320');% 30 days
for i = 1:30
    P06(i,:)=P_Jun(i*144-143:i*144);
end
clear P_Jun;
% Jul
P_Jul = xlsread('2001_07.xls','AA1:AA4464');% 31 days
for i = 1:31
    P07(i,:)=P_Jul(i*144-143:i*144);
end
clear P_Jul;
% Aug
P_Aug = xlsread('2001_08.xls','AA1:AA4464');% 31 days
for i = 1:31
    P08(i,:)=P_Aug(i*144-143:i*144);
end
clear P_Aug;
% Sep
P_Sep = xlsread('2001_09.xls','AA1:AA4320');% 30 days
for i = 1:30
    P09(i,:)=P_Sep(i*144-143:i*144);
end
clear P_Sep;
% Oct
P_Oct = xlsread('2001_10.xls','AA1:AA4464');% 31 days
for i = 1:31
    P10(i,:)=P_Oct(i*144-143:i*144);
end
clear P_Oct;
% Nov
P_Nov = xlsread('2001_11.xls','AA1:AA4320');% 30 days
for i = 1:30
    P11(i,:)=P_Nov(i*144-143:i*144);
end
clear P_Nov;
% Dec
P_Dec = xlsread('2001_12.xls','AA1:AA4464');% 31 days
for i = 1:31
    P12(i,:)=P_Dec(i*144-143:i*144);
end
clear P_Dec;