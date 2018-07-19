from tkinter import *
import backend

def add():
    backend.insert(Title.get(),
                    Author.get(),
                    Year.get(), 
                    ISBN.get())
    List_L.delete(0,END)
    List_L.insert(END,Title.get(),Author.get(),Year.get(),ISBN.get())

def view():
    List_L.delete(0,END)
    for row in backend.view():
        List_L.insert(END,row)

def delete():

    backend.delete(selected[0])

def update():

    backend.update(selected[0], 
                Title.get(), 
                Author.get(), 
                Year.get(), 
                ISBN.get())

def search():
    List_L.delete(0, END)
    for row in backend.search(Title.get(), 
                          Author.get(), 
                          Year.get(), 
                          ISBN.get()):
        List_L.insert(END, row)

def selected_row(event):

    global selected
    index = List_L.curselection()[0]
    selected= List_L.get(index)

    E1.delete(0, END)
    E1.insert(END, selected[1])

    E2.delete(0, END)
    E2.insert(END, selected[2])

    E3.delete(0, END)
    E3.insert(END, selected[3])

    E4.delete(0, END)
    E4.insert(END, selected[4])

   
Root=Tk()
Root.title("Book Directory")
Root.geometry('400x300')

#Labels
L1=Label(Root,text="Title")
L1.place(x=0, y=10)

L2=Label(Root,text="Author")
L2.place(x=200, y=10)

L3=Label(Root,text="Year")
L3.place(x=0, y=30)

L4=Label(Root,text="ISBN")
L4.place(x=200, y=30)

#Entries
Title=StringVar()
E1=Entry(Root,textvariable=Title)
E1.place(x=50, y=10)

Author=StringVar()
E2=Entry(Root,textvariable=Author)
E2.place(x=250, y=10)

Year=StringVar()
E3=Entry(Root,textvariable=Year)
E3.place(x=50, y=30)

ISBN=StringVar()
E4=Entry(Root,textvariable=ISBN)
E4.place(x=250, y=30)

#Listing
List_L=Listbox(Root,height = 6, width = 35)
List_L.place(x = 10, y = 60, height = 170, width = 240)

#Scrollbar
scroll=Scrollbar(Root)
scroll.place(x = 260, y = 120, width = 15)

scrolll=Scrollbar(Root)
scrolll.place(x = 150, y = 250, width = 50)

List_L.configure(yscrollcommand = scroll.set)
List_L.configure(xscrollcommand = scroll.set)

scroll.configure(command = List_L.yview)
scrolll.configure(command = List_L.xview, orient = HORIZONTAL)

List_L.bind('<<ListboxSelect>>', selected_row)

#Buttons
B1=Button(Root,
          text="View All",
          width=12,
          command=view)
B1.place(x=280, y=60)
B2=Button(Root,
          text="Search Entry",
          width=12,
          command=search)
B2.place(x=280,y=90)

B3=Button(Root,
          text="Add Entry",
          width=12,
          command=add)
B3.place(x=280,y=120)

B4=Button(Root,
          text="Delete Selected",
          width=12,
          command=delete)
B4.place(x=280,y=150)

B5=Button(Root,
          text="Update Selected",
          width=12,
          command=update)
B5.place(x=280,y=180)

B6=Button(Root,
          text="Close",
          width=12,
          command=Root.destroy)
B6.place(x=280,y=210)

Root.mainloop()
