import tkinter
from tkinter import *
root=Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

tasklist=[]
def addtask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open("taskfile.txt",'a')as taskfile:
            taskfile.write(f"\n{task}")
        tasklist.append(task)
        listbox.insert(END,task)
def opentaskfile():
    try:
        global tasklist
        with open("taskfile.txt","r") as task_file:
           tasks=task_file.readlines()
        for task in tasks:
            if(task !='\n'):
                tasklist.append(task)
                listbox.insert(END,task)
    except:
        file=open("taskfile.txt","w")
        file.close()
def deletetask():  
    global tasklist
    task=str(listbox.get(ANCHOR))
    if task in tasklist:
        tasklist.remove(task)
        with open("taskfile.txt",'w') as taskfie:
            for task in tasklist:
                taskfie.write(task+"\n")
        listbox.delete(ANCHOR)
#icons
icon_image=PhotoImage(file="images/task.png")
root.iconphoto(False,icon_image)
#topbar
topbar=PhotoImage(file="images/topbar.png")
Label(root,image=topbar).pack()
#docimage
docimage=PhotoImage(file="images/dock.png")
Label(root,image=docimage,bg="#32405b").place(x=30,y=25)
noteimage=PhotoImage(file="images/task1.png")
Label(root,image=noteimage,bg="#32405b").place(x=340,y=25)
heading=Label(root,text="ALL TASK",font="arial 24 bold",fg="black",bg="#32405b")
heading.place(x=130,y=20)
#main
frame=Frame(root,width="400",height="50",bg="white")
frame.place(x=0,y=180)
task=StringVar()
task_entry=Entry(frame,width="18",font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()
button=Button(frame,text="ADD",font="arial 20 bold",width="6",bg="red",fg="black",bd=0,command=addtask)
button.place(x=300,y=0)
#listbox
frame1=Frame(root,width=700,height=280,bd=3,bg="#32405b")
frame1.pack(pady=(160,0))
listbox=Listbox(frame1,width=40,height=16,font=("arial",12),bg="#32405b",fg="white",cursor="hand2",selectbackground="black")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
#delete
delete_icon=PhotoImage(file="images/delete.png")
Button(root,image=delete_icon,bd=0,command=deletetask).pack(side=BOTTOM,pady=13)
opentaskfile()




root.mainloop()