from tkinter import *    # 1
import datetime       #22

# print(datetime.datetime.now())   #23
def date_time():                   #24
    time = datetime.datetime.now()   #25
    hr = time.strftime('%I')         #26
    mi = time.strftime("%M")         #27
    sec = time.strftime("%S")        #28
    am = time.strftime("%p")          #29
    date = time.strftime("%d")        #52
    month = time.strftime("%m")       #53
    year = time.strftime("%y")        # 54
    day  =  time.strftime("%a")       #55




    lab_hr.config(text=hr)            #30
    lab_min.config(text=mi)          #31
    lab_sec.config(text=sec)        #32
    lab_am.config(text=am)              #33
    lab_date.config(text=date)          #56
    lab_mo.config(text = month)         #57
    lab_year.config(text=year)          #58
    lab_day.config(text= day)           #59

    lab_hr.after(200,date_time)         #34   .after means data change after mili sec so put 200



clock = Tk()     #2
clock.title( "  *** Digital Clock ***  ")     #4
clock.geometry('1000x500')   #4
clock.config(bg='Yellow')    #5  background color


# for creating box name
#  first portion of time

lab_hr = Label(clock,text="00",font= ('Time New Roman',60,'bold'),
               bg='red',fg='White')    #6
lab_hr.place(x=120,y=50,height= 110, width= 100)     #7
lab_hr_txt = Label(clock,text="Hour",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #14
lab_hr_txt.place(x=120,y=190,height= 40, width= 100)     #15



lab_min = Label(clock,text="00",font= ('Time New Roman',60,'bold'),
               bg='red',fg='White')    #8
lab_min.place(x=340,y=50,height= 110, width= 100)     #9
lab_min_txt = Label(clock,text="Min.",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #16
lab_min_txt.place(x=340,y=190,height= 40, width= 100)     #17




lab_sec = Label(clock,text="00",font= ('Time New Roman',60,'bold'),
               bg='red',fg='White')    #10
lab_sec.place(x=560,y=50,height= 110, width= 100)     #11
lab_sec_txt = Label(clock,text="Sec.",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #18
lab_sec_txt.place(x=560,y=190,height= 40, width= 100)     #19






lab_am = Label(clock,text="00",font= ('Time New Roman',50,'bold'),
               bg='red',fg='White')    #12
lab_am.place(x=780,y=50,height= 110, width= 100)     #13
lab_am_txt = Label(clock,text="AM/PM",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #20
lab_am_txt.place(x=780,y=190,height= 40, width= 100)     #21



# second portion date_annual  section
 
lab_date = Label(clock,text="00",font= ('Time New Roman',60,'bold'),
               bg='red',fg='White')    #36
lab_date.place(x=120,y=270,height= 110, width= 100)     #37
lab_date_txt = Label(clock,text="Date",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #38
lab_date_txt.place(x=120,y=410,height= 40, width= 100)     #39






lab_mo = Label(clock,text="00",font= ('Time New Roman',60,'bold'),
               bg='red',fg='White')    #40
lab_mo.place(x=340,y=270,height= 110, width= 100)     #41
lab_mo_txt = Label(clock,text="Month",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #42
lab_mo_txt.place(x=340,y=410,height= 40, width= 100)     #43





lab_year = Label(clock,text="00",font= ('Time New Roman',60,'bold'),
               bg='red',fg='White')    #44
lab_year.place(x=560,y=270,height= 110, width= 100)     #45
lab_year_txt = Label(clock,text="Year",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #46
lab_year_txt.place(x=560,y=410,height= 40, width= 100)     #47




lab_day = Label(clock,text="00",font= ('Time New Roman',35,'bold'),
               bg='red',fg='White')    #48
lab_day.place(x=780,y=270,height= 110, width= 100)     #49
lab_day_txt = Label(clock,text="Day",font= ('Time New Roman',20,'bold'),
               bg='red',fg='White')    #50
lab_day_txt.place(x=780,y=410,height= 40, width= 100)     #51





date_time()                #35


clock.mainloop()     #3
