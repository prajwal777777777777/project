import pyinputplus as pypi;
try:
    choice=pypi.inputYesNo(prompt="Do you want time in 12 hour format[Y/N]:").lower()
    if(choice=="yes" or choice=="y"):
        current_time=pypi.inputInt(prompt="Enter the current time in hours:",max=12);
    else:
        current_time=pypi.inputInt(prompt="Enter the current time in hours:",max=24);
    while True:
        am_pm=pypi.inputMenu(["AM","PM"]).lower();
        if((choice=="no" or choice=="n") and (current_time>=12) and (am_pm=="am")):
            print(f"{current_time} cannot be am in 24 hour format.");
            pass;
            #In 24 hour format time cannot be greater than 12 and am.(i.e 13 am is not possible) and continue the infinite loop.
        else:
            break;
            #if eveything is good it will break infinite loop.

    alarm=pypi.inputInt(prompt="Enter the time for alarm in hours:",max=100000);
    backup=am_pm
    #we assign a backup variable equals to am_pm variable which will need in future.

    days=alarm//24
    #if alarm greater than 24 hours it will count as day in whole number.
    if(days>0):
        days_new=days
        pass;
    else:
        days_new=0
    hours=alarm%24 #max value=23
    #hours will be the remainder of alarm.
    alarm_time=current_time+hours
    #we add our current_time with hours as alarm_time variable.


    def am_pm_function():#this function will change am to pm like if alarm greater than 12 it will change am to pm and if it is greater than 24 it will again change pm to am.
        alarm_list=[n for n in range(1,alarm+1)]
        #this will contain all number in list like if alarm is 12 hours it will contain 1-12 in list.
        
        conditioned_list=list(filter(lambda x:x%12==0,alarm_list));
        #we filterd list if the element of list gives remainder 0 when divided by 12(i.e it would only contain number divisible by 12.)
        
        for i in range(1,len(conditioned_list)+1):
            #it would iterate over the list from 1.

            global am_pm;
            global backup;
            #we use global variable am_pm and backup for our local use.

            if(alarm_list[-1]>conditioned_list[-1]): #little tricky
                #we are doing if alarm time less than 12 it would be am and if it is greater than 12 and less than 24 it would be pm.
                #e.g supose current_time is 7am and we set alarm after 23 hours then our condtion_list contain on 12[12] cuz till 23, 12 is only divisible by 12.
                #so our below odd even if else statment cannot change am to pm so if the alarm time is 23 hours so it is greater than 12 then it would change am_pm. 
                if(am_pm=="am"):
                    am_pm="pm";
                else:
                    am_pm=="am";
                #it would change am to pm(in nutshell it would change am to pm if condtion list contain single element.) .
            if(i%2!=0):
                #if len of condition_list element is greater than 1 for every odd element it would change am to pm and vice-versa.
                if(am_pm=="am"):
                    am_pm="pm";
                else:
                    am_pm="am";
            else:
                am_pm=backup;#if element of list is even it would be same like if current_time is 7am and i set alarm after 24 hours first it would change am to pm and again pm to am .
        am_pm_function.ext=am_pm
        #to use in local variable outside function
    am_pm_function()






    if(choice=="yes" or choice=="y"):
        def twelve_hour():
            if(alarm_time>=24): #alarm_time max=23+12=35
                remaing_time=alarm_time-24
                if(remaing_time>12):
                    remaing_time=remaing_time-12
                    print("Alarm will go off in "+str(days_new)+"days"+f" {str(hours)}hours"+" in "+str(remaing_time)+str(am_pm_function.ext));
                elif(remaing_time==0):
                    remaing_time=12
                    print("Alarm will go off in "+str(days_new)+"days"+f" {str(hours)}hours"+" in "+str(remaing_time)+str(am_pm_function.ext))
                else:
                    print("Alarm will go off in "+str(days_new)+"days"+f" {str(hours)}hours"+" in "+str(remaing_time)+str(am_pm_function.ext));
            elif(alarm_time>12 and alarm_time<24):
                remaing_time=alarm_time-12
                print("Alarm will go off in "+str(days_new)+"days"+f" {str(hours)}hours"+" in "+str(remaing_time)+str(am_pm_function.ext));
            else:
                print("Alarm will go off in "+str(days_new)+"days"+f" {str(hours)} hours"+" in"+str(alarm_time)+str(am_pm_function.ext));

        twelve_hour();
    else:
        def twenty_four():
            if(alarm_time>=24):
                twenty_four_remaing_time=alarm_time-24
                if(twenty_four_remaing_time>=12):
                    am_pm_function.ext="pm"
                if(twenty_four_remaing_time==0):
                    twenty_four_remaing_time=24
                    am_pm_function.ext="am"
                    print("Alarm will go off after "+str(days_new)+"days"+f"{str(hours)}hours"+" in "+str(twenty_four_remaing_time)+str(am_pm_function.ext));                
                else:
                    print("Alarm will go off in "+str(days_new)+"days"+f" {str(hours)}hours"+" in "+str(twenty_four_remaing_time)+str(am_pm_function.ext))
            else:
                print("Alarm will go off in "+str(days_new)+"days"+f" {str(hours)}hours"+" in "+str(alarm_time)+str(am_pm_function.ext));
        twenty_four()
except KeyboardInterrupt:
    print("\n\nBye.")
except:
    print("An unknown error has occured.");
    quit;
                                    #try yourself