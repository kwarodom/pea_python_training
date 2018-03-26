%% plot
close all;clc;
fontsize=14;
%% plot homes load profile all day
selected_day=1; %**** or start day
no_days=7;
interval=15; %min
f1 = figure;
set(f1,'name',sprintf('Homes load profile start_day %d stop_day %d',selected_day,selected_day+no_days-1),'numbertitle','off');
subplot(2,5,1); plot_individual_home(usekW_H1,1,selected_day,no_days,interval,fontsize) % plot_individual_home(H_usekW,homeNo,selected_day,no_days,interval,fontsize)
subplot(2,5,2); plot_individual_home(usekW_H2,2,selected_day,no_days,interval,fontsize)
subplot(2,5,3); plot_individual_home(usekW_H3,3,selected_day,no_days,interval,fontsize)
subplot(2,5,4); plot_individual_home(usekW_H4,4,selected_day,no_days,interval,fontsize)
subplot(2,5,5); plot_individual_home(usekW_H5,5,selected_day,no_days,interval,fontsize)
subplot(2,5,6); plot_individual_home(usekW_H6,6,selected_day,no_days,interval,fontsize)
subplot(2,5,7); plot_individual_home(usekW_H7,7,selected_day,no_days,interval,fontsize)
subplot(2,5,8); plot_individual_home(usekW_H8,8,selected_day,no_days,interval,fontsize)
subplot(2,5,9); plot_individual_home(usekW_H9,9,selected_day,no_days,interval,fontsize)
subplot(2,5,10); plot_individual_home(usekW_H10,10,selected_day,no_days,interval,fontsize)

%% plot homes load profile at a given day
selected_day=1; %****
no_days=1;
interval=15; %min
f2 = figure;
set(f2,'name',sprintf('Homes load profile start_day %d stop_day %d',selected_day,selected_day+no_days-1),'numbertitle','off');
subplot(2,5,1); plot_individual_home(usekW_H1,1,selected_day,no_days,interval,fontsize) % plot_individual_home(H_usekW,homeNo,selected_day,no_days,interval,fontsize)
subplot(2,5,2); plot_individual_home(usekW_H2,2,selected_day,no_days,interval,fontsize)
subplot(2,5,3); plot_individual_home(usekW_H3,3,selected_day,no_days,interval,fontsize)
subplot(2,5,4); plot_individual_home(usekW_H4,4,selected_day,no_days,interval,fontsize)
subplot(2,5,5); plot_individual_home(usekW_H5,5,selected_day,no_days,interval,fontsize)
subplot(2,5,6); plot_individual_home(usekW_H6,6,selected_day,no_days,interval,fontsize)
subplot(2,5,7); plot_individual_home(usekW_H7,7,selected_day,no_days,interval,fontsize)
subplot(2,5,8); plot_individual_home(usekW_H8,8,selected_day,no_days,interval,fontsize)
subplot(2,5,9); plot_individual_home(usekW_H9,9,selected_day,no_days,interval,fontsize)
subplot(2,5,10); plot_individual_home(usekW_H10,10,selected_day,no_days,interval,fontsize)


%% plot homes load profile at a given day
selected_day=2; %****
no_days=3;
interval=15; %min
f3 = figure;
set(f3,'name',sprintf('Homes load profile start_day %d stop_day %d',selected_day,selected_day+no_days-1),'numbertitle','off');
subplot(2,5,1); plot_individual_home(usekW_H1,1,selected_day,no_days,interval,fontsize) % plot_individual_home(H_usekW,homeNo,selected_day,no_days,interval,fontsize)
subplot(2,5,2); plot_individual_home(usekW_H2,2,selected_day,no_days,interval,fontsize)
subplot(2,5,3); plot_individual_home(usekW_H3,3,selected_day,no_days,interval,fontsize)
subplot(2,5,4); plot_individual_home(usekW_H4,4,selected_day,no_days,interval,fontsize)
subplot(2,5,5); plot_individual_home(usekW_H5,5,selected_day,no_days,interval,fontsize)
subplot(2,5,6); plot_individual_home(usekW_H6,6,selected_day,no_days,interval,fontsize)
subplot(2,5,7); plot_individual_home(usekW_H7,7,selected_day,no_days,interval,fontsize)
subplot(2,5,8); plot_individual_home(usekW_H8,8,selected_day,no_days,interval,fontsize)
subplot(2,5,9); plot_individual_home(usekW_H9,9,selected_day,no_days,interval,fontsize)
subplot(2,5,10); plot_individual_home(usekW_H10,10,selected_day,no_days,interval,fontsize)