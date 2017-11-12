from tkinter import *

def inputing():
    team1_name.set(entry_team1_name.get())
    team2_name.set(entry_team2_name.get())
    
    Label(window,textvariable = team1_name)
    Label(window,textvariable = team2_name)
def resting():
    pass;

#window
window = Tk()
window.title('Auto Referee')
window.geometry('450x300')

#user input table
Label(window,text='Team 1 Name : ').place(x=50,y=50)
Label(window,text='Team 2 Name : ').place(x=50,y=100)

team1_name = StringVar()
team2_name = StringVar()

#Entrying team name
entry_team1_name = Entry(window,textvariable=team1_name)
entry_team1_name.place(x=160, y=50)
entry_team2_name = Entry(window,textvariable=team2_name)
entry_team2_name.place(x=160, y=100)

#Enter posisiton

#Button to next page 
btn_login = Button(window, text='Okay', command=inputing)
btn_login.place(x=170, y=150)


btn_reset = Button(window, text='Reset', command=inputing)
btn_reset.place(x=230, y=150)
#First page
window.mainloop()