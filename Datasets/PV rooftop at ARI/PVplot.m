clear;
clc;
figure()
%read 15second data.
PV15sec = csvread('2012.06.22.csv');
a = size(PV15sec)
for i=1:a(1)
    PV15secTEMP(i,1) = 240*PV15sec(i,4)+4*PV15sec(i,5)+round(PV15sec(i,6)*3/45)+1; %round to prevent data that come in not showing 0, 15, 30 and 45 seconds
    PV15secTEMP(i,2) = PV15sec(i,19);
end
%find missing data & recreate the full array of size 5760(=60*24*4) for plotting
n = 1;
m = 0;
for i=1:24*60*4
    if i == PV15secTEMP(n,1)
        PV15secPLOT(i) = PV15secTEMP(n,2);
        n = n+1;
    else
      %  if i == PV15secTEMP(n+1,1) %prevent data repeating like on 6/21.2012
      %      n=n+1;
      %  else
            PV15secPLOT(i) = PV15secTEMP(i-1,2);
            missingData (m+1) = n % tell us which data points are missing
            m=m+1;
      %  end
    end
end
missingData
%plot(PV15secPLOT)


%Find average of "res" minute data, then plot
res = 15 %resolution = 15 minutes
for i = 1:5760/(res*4)
    for j = 1:res*4 %10 minutes/hour * 4 samplings/minute
        PV15minPLOT((i-1)*res*4+j) = sum(PV15secPLOT(((i-1)*res*4+1):i*res*4))/(res*4);
    end
end

res = 60
%Find average of 1 hour data, then plot
for i = 1:5760/(res*4)
    for j = 1:res*4 %60 mins/hour * 4 samplings/minute
        PV1hourPLOT((i-1)*res*4+j) = sum(PV15secPLOT(((i-1)*res*4+1):i*res*4))/(res*4);
    end
end



%========================================================
%read 5min data, convert to the same scale, then plot.
%PV5min = csvread('2012-06-22.csv',6,18,'S7..S294');
%b = size(PV5min)
%========================================================
%i=1;
%j=1;
%while ((i-1)*20+j) < a(1)
%    for i=1:b
%        for j=1:ceil(a/b)
 %           PV5min4plot ((i-1)*ceil(a/b)+j) = PV5min(i);        
%            PV5minAVE ((i-1)*ceil(a/b)+j) = sum(PV15secPLOT((i-1)*ceil(a/b)+1:i*ceil(a/b)))/ceil(a/b);
%        end
%    end
%end
    
%plot(PV5min4plot,'g')
%%hold on
%plot(PV15minPLOT, 'g')
%hold on
%plot(PV1hourPLOT,'r')


var15min = PV15secPLOT - PV15minPLOT;
var1hour = PV15secPLOT - PV1hourPLOT;

%figure(2);
%plot(var15min, 'g')
%hold on
%plot(var1hour,'r')



subplot(5,1,1:2)
plot(1:5760,PV15secPLOT,1:5760,PV15minPLOT,1:5760,PV1hourPLOT) 
  title('PV output (kW)')
  XLIM([0,5760])
  YLIM([0,6500])
  set(gca,'XTick',0:480:5760)
  set(gca,'XTickLabel',{'00:00','02:00','04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00','24:00'})
  set(gca,'YTick',0:1000:6000)
  set(gca,'YTickLabel',{'0','1000','2000','3000','4000','5000','6000'})
  legend('15-second data','15-min average','1-hour average')
  ylabel('PV output (kW)')


subplot(5,1,3)
plot(1:5760,var15min,'g',1:5760,var1hour,'r') 
  title('Variation from 15-second power output (kW)')
  XLIM([0,5760])
  YLIM([-4000,4000])
  set(gca,'XTick',0:480:5760)
  set(gca,'XTickLabel',{'00:00','02:00','04:00','06:00','08:00','10:00','12:00','14:00','16:00','18:00','20:00','22:00','24:00'})
  legend ('15min vs 15sec data', '1hour vs 15sec data')
  ylabel('Variation (kW)')

  maxVar15min = strcat('Max=',num2str(max(var15min),'%4.0f'),'kW');
  minVar15min = strcat('Min=',num2str(min(var15min),'%4.0f'),'kW');

  maxVar1hour = strcat('Max=',num2str(max(var1hour),'%4.0f'),'kW');
  minVar1hour = strcat('Min=',num2str(min(var1hour),'%4.0f'),'kW');
  
  
  %bin = round((abs(floor(min(var15min)/1000)*1000)+ceil(max(var15min)/1000)*1000)/100);
  bin = 50;
subplot(5,1,4)
    hist(var15min,bin)
   title('Histogram - Variation of 15-minute output from 15-second power output')
    h = findobj(gca,'Type','Patch');
    set(h,'FaceColor','g','EdgeColor','w')
    XLIM([floor(min(var15min)/1000)*1000,ceil(max(var15min)/1000)*1000])
    YLIM([0,4000])
    ylabel('Frequency count')
    xlabel('Variation (kW)')
    text(ceil(max(var15min)/1000)*1000-1000,3500,maxVar15min)
    text(ceil(max(var15min)/1000)*1000-1000,3000,minVar15min)
    
subplot(5,1,5)
    hist(var1hour,bin)
   title('Histogram - Variation of 1-hour output from 15-second power output')
    h = findobj(gca,'Type','Patch');
    set(h,'FaceColor','r','EdgeColor','w')
    XLIM([floor(min(var15min)/1000)*1000,ceil(max(var15min)/1000)*1000])
    YLIM([0,4000])
    ylabel('Frequency count')
    xlabel('Variation (kW)')
    text(ceil(max(var15min)/1000)*1000-1000,3500,maxVar1hour)
    text(ceil(max(var15min)/1000)*1000-1000,3000,minVar1hour)

