function plot_individual_home(H_usekW,homeNo,selected_day,no_days,interval,fontsize)
if selected_day == 1
   start_point=1;
else
   start_point=((selected_day-1)*(24*60/interval))+1;
end
stop_point=start_point+(no_days*(24*60/interval))-1;

usekW_H_day=H_usekW(start_point:stop_point); %time interval of the recorded data
plot(usekW_H_day); title(sprintf('Home %d: Load profile',homeNo),'Fontsize',fontsize); xlim([0 length(usekW_H_day)]);
xlabel('Time (hr)','Fontsize',fontsize);
ylabel('Load profile (kW)','Fontsize',fontsize);

if no_days==1
    set(gca,'XTick',0:3*60/interval:length(usekW_H_day));
    set(gca,'XTickLabel',{'0','3','6','9','12','15','18','21','24'},'Fontsize',fontsize);
    % set(gca,'XGrid','on') 
    % set(gca,'YGrid','on')
end    