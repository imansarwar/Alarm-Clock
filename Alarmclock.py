# Clock Initiliser

from tkinter import *
import datetime
import time
import winsound
duration = 1000
freq= 440
winsound.Beep (freq,duration)


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.Beep(500,1000)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)
clock = Tk()

clock.title("Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Please Enter time in 24 hours format!", fg="white",bg="#cd5d7d",font="Arial").place(x=65,y=120)
addTime = Label(clock,text = "Hour    Min    Sec",font=60).place(x = 150)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",8,"bold")).place(x=10, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=150,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=190,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=240,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =250,y=70)

clock.mainloop()
#Execution of the window.
