# Improting from all libaries that will be needed#
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk 
from tkinter import messagebox

#------- Config -------#
root = tk.Tk() #jsut making the window fancy and usable
root.title('Plantify')
root.geometry('392x850+2100+50') #needs to be changed to 50+50 not 2100 if not pls change does not work on every device
root.resizable(0, 0) #just lokking the resizablite is better just makes it work somoter
root.attributes('-topmost', 1) #for showcase and making it easier to work with
root.iconbitmap('icons/Plantify_logo.ico') #logo Icon for fancy
root.configure(bg="white") # background color because withe is clean

#------- Colors -------#

Dark_green = "#669C35"
Dark_light_green = "#96D35F"
Light_dark_green = "#B1DD8C"
Light_green = "#CCE8B5"

Grey = "#606060"

Dark_blue = "#004099"
Dark_light_blue = "#0059AE"
Light_dark_blue = "#0075C0"
Light_blue = "#3F8ACC"
#------- Images -------#

logo = tk.PhotoImage(file='images/Plantify_logo.png')
Home_icon = tk.PhotoImage(file='Icons\Homebutton.png')
CurrentTask_icon = tk.PhotoImage(file='Icons\CurrrentTaskbutton.png')
Profile_icon = tk.PhotoImage(file='Icons\Profilbutton.png')
Menu_icon = tk.PhotoImage(file='Icons\Menubutton.png')
Close_icon = tk.PhotoImage(file='Icons\closebutton.png')
log_icon = tk.PhotoImage(file='Icons\logbutton.png')
save_icon  = tk.PhotoImage(file='Icons\Savebutton.png')

taskcompletion_nr= tk.StringVar()
taskcompletion_nr.set(0)# there has to be a value here that can be modifed 
taskcompletionmax_nr = tk.StringVar()
taskcompletionmax_nr.set(0) # same thing here if there is not a value here then it doesn't work
Precential_completion = tk.StringVar()

#------- defenitions -------#
def menu():
    # i was not able to figure this out this line of code and ask chat gpt for help 
    for widget in root.winfo_children():
        widget.destroy()

    img = Image.open('images/Greenhouse_greenhouse_menu_workfile.png')
    img = img.resize((392, 850), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(img)


    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Home = tk.Button(root,
                     image= Home_icon,
                     cursor="circle",
                     bg=Light_green,
                     bd=0, 
                     highlightthickness=0,
                     command= homescreen_def
                        )
    Home.place(x= 15,y= 136) 
    #wanted to use pack put for this alligment wasnt it really usefull,grid had some more promise but was not fitting asewll

    current_task = tk.Button(root,
                     image= CurrentTask_icon,
                     cursor="circle",
                     bg=Light_green,
                     bd=0, 
                     highlightthickness=0,
                     command= Currenttask,
                      
                        )
    current_task.place(x=15, y=214)

    profile = tk.Button(root,
                     image= Profile_icon,
                     cursor="circle",
                     bg=Light_green,
                     bd=0, 
                     highlightthickness=0,
                     command=Account
                        )
    profile.place(x=15, y=292)

    goaway_button = tk.Button(root,
        cursor="circle",
        image=Close_icon,
        bg=Light_green,bd=0,
        highlightthickness=0,
        command=root.destroy )
    goaway_button.pack(side=tk.BOTTOM,padx=15,pady=15,anchor=tk.SE)

    taskcompletion_label=tk.Label(textvariable=taskcompletion_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletion_label.place(x=165,y=790,)

    taskcompletionmax_label=tk.Label(textvariable=taskcompletionmax_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletionmax_label.place(x=195,y=790,)


    root.configure(bg='0')

    root.mainloop()
def homescreen_def():
     # homescreen ui

     # home or plant sceern was seen first as a way to enter the app but now be see the secondary screen 

    img = Image.open('images\Greenhouse_homescreen_concept.png')  
    img = img.resize((392, 850), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(img)

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #all labels together

    taskcompletion_label=tk.Label(textvariable=taskcompletion_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletion_label.place(x=165,y=790,)

    taskcompletionmax_label=tk.Label(textvariable=taskcompletionmax_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletionmax_label.place(x=195,y=790,)

    Precential_completion_display= tk.Label(textvariable=Precential_completion,
                                            font=('Helvetica', 35, 'bold'),
                                            fg=Dark_blue,
                                            bg=Light_blue,

                                            )
    Precential_completion_display.pack(pady=350,padx=50)

    #all buttons with place to make it easier there is no reszing so thats not a problem

    didtaskplus_botton = tk.Button(root,
        text='+',
        font=('Helvetica', 18, 'bold'),
        cursor="circle",
        fg=Dark_blue,
        bg=Light_blue,
        bd=0,
        highlightthickness=0,
        command=lambda: [
        taskcompletion_nr.set(min(int(taskcompletion_nr.get()) + 1, int(taskcompletionmax_nr.get()))),
        update_completion_percentage()]) 
        # adds 1 and makes sure that the value does not go above the max amount of taks and does an update
    didtaskplus_botton.place(x=180,y=150)

    didtaskminus_botton = tk.Button(root,
        text='-',
        font=('Helvetica', 24, 'bold'),
        cursor="circle",
        fg=Dark_blue,
        bg=Light_blue,
        bd=0,
        highlightthickness=0,
        command=lambda:[ taskcompletion_nr.set(max(int(taskcompletion_nr.get()) - 1, 0))
        ,update_completion_percentage()])#subs 1 and limits it at the same time  and does the update thing by calling the other defintion
    didtaskminus_botton.place(x=180,y=500)

    # menu botton
    menu_botton = tk.Button(root,
        image=Menu_icon,
        cursor="circle",
        bg=Light_green,
        bd=0,
        highlightthickness=0,
        command=menu)
    menu_botton.place(x=15,y=15)

    # close botton 
    exit_button = tk.Button(root,
        image=Close_icon,
        cursor="circle",
        bg=Light_green,bd=0,
        highlightthickness=0,
        command=root.destroy )
    exit_button.place(x=360, y=820)

    root.mainloop()
def Currenttask():
    img = Image.open('images\Greenhouse_Current_Tasks workfile.png')
    img = img.resize((392, 850), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(img)
    
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    not_well_bt=tk.Button(root,
                        text='not well',
                        bg=Dark_light_green,
                        fg='white',
                        bd=0,
                        highlightthickness=0,
                        cursor="circle",
                        command=lambda: 
                        mood.set(max(int(mood.get() or -100) - 50, -100)))# subs 50 and limits the value to a max of-100
    not_well_bt.place(x=25,y=199)

    less_well_bt=tk.Button(root,
                        text='less well',
                        bg=Light_dark_green,
                        fg='white',
                        bd=0,
                        highlightthickness=0,
                        cursor="circle",
                        command=lambda: 
                        mood.set(max(int(mood.get() or -100) - 25, -100)))# subs 25 and limits the value to a max of-100
    less_well_bt.place(x=100,y=199)

    okay_bt=tk.Button(root,
                        text='okay',
                        bg='white',
                        fg=Dark_green,
                        bd=0,
                        highlightthickness=0,
                        cursor="circle",
                        command=lambda: 
                        mood.set(0)) # just resets the value it simpler then compreing the value and then adding or removing something and could become really difcult and more complex then needed
    okay_bt.place(x=180,y=199)

    well_bt=tk.Button(root,
                        text='well',
                        bg=Light_blue,
                        fg='white',
                        bd=0,
                        highlightthickness=0,
                        cursor="circle",
                        command=lambda: 
                        mood.set(min(int(mood.get() or 0) + 25, 100)))# add 25 and limits the value to a max of 100 
    well_bt.place(x=260,y=199)

    very_well_bt=tk.Button(root,
                        text='very well',
                        bg=Light_dark_blue,
                        fg='white',
                        bd=0,
                        highlightthickness=0,
                        cursor="circle",
                        command=lambda: 
                        mood.set(min(int(mood.get() or 0) + 50, 100))) # ad 50 and limits the value to a max of 100
    very_well_bt.place(x=320,y=199) # math is stupid 

    #ok it works i dont know how i dont know where i got it from currently its just math magic but manly i limit the value that can be achied on the coreseponding button 

    add_task_max = tk.Button(root,
                             fg=Dark_green,
                             bg=Light_green,
                             bd=0,
                             font='15',
                             highlightthickness=0,
                             cursor="circle",
                             text='+',
                             command=lambda: [
                             taskcompletionmax_nr.set(min(int(taskcompletionmax_nr.get() or 0) + 1, 100)),
                             update_completion_percentage()
                             ])
    add_task_max.place(x=80,y=380)

    minus_task_max = tk.Button(root,
                             fg=Dark_green,
                             bg=Light_green,
                             bd=0,
                             font='15',
                             highlightthickness=0,
                             cursor="circle",
                             text='-',
                             command=lambda: [
                             taskcompletionmax_nr.set(max(int(taskcompletionmax_nr.get() or 0) - 1, 0)),
                             update_completion_percentage()
                             ])
    minus_task_max.place(x=280,y=380)

    taskcompletion_label=tk.Label(textvariable=taskcompletion_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletion_label.place(x=165,y=790,) #acvied  markers like waht has been done 

    taskcompletionmax_label=tk.Label(textvariable=taskcompletionmax_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletionmax_label.place(x=195,y=790,) # max markers 

    # menu botton
    menu_botton = tk.Button(root,
        image=Menu_icon,
        cursor="circle",
        bg=Light_green,
        bd=0,
        highlightthickness=0,
        command=menu)
    menu_botton.place(x=15,y=15)

    # close botton 
    exit_button = tk.Button(root,
        image=Close_icon,
        cursor="circle",
        bg=Light_green,bd=0,
        highlightthickness=0,
        command=root.destroy )
    exit_button.place(x=360, y=820)

    root.configure(bg='0')

    root.mainloop()
def Account():
    img = Image.open('images/Greenhouse_Profile_concept.png')
    img = img.resize((392, 850), Image.LANCZOS)
    background_image = ImageTk.PhotoImage(img)
    

    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    Name_display=tk.Label(root,textvariable=name,
                          fg='White',
                          font='35',
                          background=Light_dark_green)
    Name_display.place(x=50,y=500)

    Age_display=tk.Label(root,textvariable=age,
                         fg='white',
                         bg=Light_dark_green,
                         font='35',)
    Age_display.place(x=270,y=530)

    Mood_display=tk.Label(root,textvariable=mood,
                          fg='white',
                          font='35',
                          bg=Light_dark_green)
    Mood_display.place(x=260,y=575)

    # Logout botton
    logout_button = tk.Button(root,
        image=log_icon,
        cursor="circle",
        bg=Light_green,bd=0,
        highlightthickness=0,
        command=root.destroy )
    logout_button.place(x=110, y=670)

    # menu botton
    menu_botton = tk.Button(root,
        image=Menu_icon,
        cursor="circle",
        bg=Light_green,
        bd=0,
        highlightthickness=0,
        command=menu)
    menu_botton.place(x=15,y=15)

    # close botton 
    exit_button = tk.Button(root,
        image=Close_icon,
        cursor="circle",
        bg=Light_green,bd=0,
        highlightthickness=0,
        command=root.destroy )
    exit_button.place(x=360, y=820)

    taskcompletion_label=tk.Label(textvariable=taskcompletion_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletion_label.place(x=165,y=790,)

    taskcompletionmax_label=tk.Label(textvariable=taskcompletionmax_nr,
                                  font=('Helvetica', 18, 'bold'),
                                  background=Light_green,
                                  foreground=Dark_green
                                  )
    taskcompletionmax_label.place(x=195,y=790,)

    save_button= tk.Button(image=save_icon,
                            cursor="circle",
                            bg=Light_green,bd=0,
                            highlightthickness=0,
                            command=save_user_data)
    save_button.place(x=110,y=620)

    root.configure(bg='0')
    
    root.mainloop()

def update_completion_percentage():

    max_completion = int(taskcompletionmax_nr.get())

    #if the number drops below zero we stop it here otherwise there is going to be an error
    if max_completion == 0:
        Precential_completion.set("0%")
        return
    
    # math section turnig vales into precentails and stuff
    percentage_completion = int(taskcompletion_nr.get()) / int(taskcompletionmax_nr.get()) * 100

    # Update after math
    Precential_completion.set(f"{percentage_completion:.0f}%") #its a defition but htis could be used outside for creating more stuff
    
    if percentage_completion == 100: #this is so simple and easy i love it 
        messagebox.showinfo("Congratulations!", "You have completed all tasks!") # happy you have done it this is really cool 

#------- Variables -------#

age = tk.StringVar()
name = tk.StringVar()
mood = tk.StringVar()
Tasks = tk.StringVar()
#------- Start padge sectoin 1 -------#

image_label = ttk.Label(root,
                        image=logo,
                        text= 'Please hand in your infraomtion ',
                        font='25',
                        background="white",
                        compound='top')
image_label.pack(side=tk.TOP,pady=10)

#------- name  -------#
Name_label = ttk.Label(text="Name",
                        font='10',
                        background="white")
Name_label.pack()

name_entry = ttk.Entry(textvariable=name)
name_entry.pack()

#------- age  -------#
age_label = ttk.Label(text="Age:",
                           font='10',
                           background="white")
age_label.pack()


age_entry = ttk.Spinbox(root,
                        from_=13,
                        to=99,
                        textvariable=age)
age_entry.pack()


# data save and load defnitions 

def save_user_data():

    #get the data into the defintion i used for this scetion some help of chat gpt I have marked the postions with GPT
    name_save = name.get()
    age_save = age.get()
    mood_score_save = mood.get()
    completed_tasks_save = taskcompletion_nr.get()
    completed_max_save = taskcompletionmax_nr.get()

    # Read all existing data from the file
    existing_data = []
    try: 
        with open("user_data.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                existing_data.append(data)
    except FileNotFoundError:
        pass

    # Check if an entry with the same name and age already exists
    for i, data in enumerate(existing_data):
        if data[0] == name_save and data[1] == age_save:
            # Overwrite existing entry with new data
            existing_data[i] = [name_save, age_save, mood_score_save, completed_tasks_save,completed_max_save]
            break
    else:
        # Appends the user data coulded get it to wrok at first GPT
        existing_data.append([name_save, age_save, mood_score_save, completed_tasks_save, completed_max_save])

    # Write all data (existing + new) back to the file
    with open("user_data.txt", "w") as file:
        for data in existing_data:
            file.write(",".join(data) + "\n")

    # Show success message
    messagebox.showinfo("Success", "Your data has been saved.")
def load_user_data():
    # Retrieve data from entry widgets
    name_load = name.get()
    age_load = age.get()

    # Read all existing data from the file
    try:
        with open("user_data.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == name_load and data[1] == age_load:
                    # Update variables with loaded values
                    name.set(data[0])
                    age.set(data[1])
                    mood.set(data[2])
                    taskcompletion_nr.set(data[3])
                    taskcompletionmax_nr.set(data[4])
                    # Notify the user that the data has been loaded
                    messagebox.showinfo("User Data", "Data loaded successfully.")
                    # Navigate to the menu screen
                    menu()
                    return
            else:
            # If no matching entry is found
             messagebox.showinfo("User Data", "No existing data found.")
    except FileNotFoundError:
        # If the file doesn't exist
        messagebox.showinfo("User Data", "No existing data found.")

#buttons for leaving on the main screen 
exit_button = tk.Button(text="close",
                        bg=Dark_green,
                        fg=Light_green,
                        command=root.destroy )
exit_button.pack(side=tk.BOTTOM, pady=20)

start_button = tk.Button(text="Continue",
                        bg= Dark_green,
                        fg= Light_green,
                        command=menu,)
start_button.pack(side=tk.TOP, pady=5)

save_button= tk.Button(text='load',
                       command=load_user_data)
save_button.pack(side=tk.BOTTOM,pady=20)


root.mainloop()
# I just read some of my commnets and i wold like to say that i hope this is something to laugh at.