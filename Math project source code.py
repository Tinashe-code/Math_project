from tkinter import *

root = Tk()
root.title("Orthographic projection")
root.configure(bg="green")
#root.geometry

frame = Frame(root,pady=5,padx=5,width=150, height=150,bg="indigo")
frame.place(x=2,y=0)

def calculate_matrix():
    solution = Toplevel()
    #rt = (r.get())
    #lt = (l.get())
    #print(int(rt))
    x11 = 2/(int(r.get())-int(l.get()))
    print(x11)
    x12 = 0
    x13 = 0
    x14 = -((int(r.get())+int(l.get()))/(int(r.get())-int(l.get())))
    print(x14)
    x21 = 0
    x22 = 2/(eval(t.get())-eval(b.get()))
    x23 = 0
    x24 = -((int(t.get())+int(b.get()))/(int(t.get())-int(b.get())))
    x31 = 0
    x32 = 0
    x33 = -2/(int(f.get())-int(n.get()))
    x34 = (int(f.get())+int(n.get()))/(int(f.get())-int(n.get()))
    x41 = 0
    x42 = 0
    x43 = 0
    x44 = 1
    global y_coordinate
    global x_coordinate
    x_coordinate = x11*int(x.get())
    y_coordinate = x22*int(y.get())
    x_display = Label(solution, text='x coordinate= ' + str(x_coordinate))
    x_display.pack()
    y_display = Label(solution, text='y coordinate= '+str(y_coordinate))
    y_display.pack()
    btn = Button(solution, text='Back',width=20,height=1,bg='indigo',fg='yellow',activebackground='yellow',activeforeground='indigo',font=('Arial Black',10),command=solution.destroy)
    btn.pack()

    #def back():

    #close = Button(solution, text='Previous',command=back)



#inputing the screen cortinates
l = Entry(root, text="enter Left screen cordinate", width=50)
r = Entry(root, text="enter Right screen cordinate", width=50)
t = Entry(root, text="enter Top screen cordinate", width=50)
b= Entry(root, text="enter Bottom screen cordinate", width=50)
f = Entry(root, text="enter Far screen cordinate", width=50)
n = Entry(root, text="enter Near screen cordinate", width=50)
x = Entry(root, text="enter 'X' coordinate of 3D object", width=50)
y = Entry(root, text="enter 'Y' coordinate of 3D object", width=50)
z = Entry(root, text="enter 'Z' coordinate of 3D object", width=50)
#l = Entry(root, text="enter screen cordinate", width=50)
#l = Entry(root, text="enter screen cordinate", width=50)
#l = Entry(root, text="enter screen cordinate", width=50)






#labels
_3dcord = Label(root, text="Input 3D object coordinates in space", bg="green",fg="white",font=('Arial Black',20))
screen = Label(root, text="Input screen coordinates", bg="green",font=('Arial Black',20),fg='yellow')
l_label = Label(root, text="enter Left screen cordinate", width=50, bg="green",font=('Arial Black',15))
r_label = Label(root, text="enter Right screen cordinate", width=50,bg="green",font=('Arial Black',15))
t_label = Label(root, text="enter Top screen cordinate", width=50,bg="green",font=('Arial Black',15))
b_label = Label(root, text="enter Bottom screen cordinate", width=50,bg="green",font=('Arial Black',15))
f_label = Label(root, text="enter Far screen cordinate", width=50,bg="green",font=('Arial Black',15))
n_label = Label(root, text="enter Near screen cordinate", width=50,bg="green",font=('Arial Black',15))
x_label = Label(root, text="enter 'X' coordinate of 3D object", width=50,bg="green",font=('Arial Black',15))
y_label = Label(root, text="enter 'Y' coordinate of 3D object", width=50,bg="green",font=('Arial Black',15))
z_label = Label(root, text="enter 'Z' coordinate of 3D object", width=50,bg="green",font=('Arial Black',15))


#buttons
caluculate = Button(root,text='Image Coordinates',width=20,height=1,bg='indigo',fg='yellow',activebackground='yellow',activeforeground='indigo',font=('Arial Black',10),command=calculate_matrix)
#show_trans_matrix = Button(root,text='Show Transition Matrix',width=20,height=1,bg='indigo',fg='yellow',activebackground='yellow',activeforeground='indigo',font=('Arial Black',10))


#displaying onto screen
screen.grid(row=0,column=0,columnspan=2)
l_label.grid(row=1, column=0)
r_label.grid(row=2, column=0)
t_label.grid(row=3, column=0)
b_label.grid(row=4,column=0)
f_label.grid(row=5, column=0)
n_label.grid(row=6, column=0)
_3dcord.grid(row=7,column=0)
x_label.grid(row=8, column=0)
y_label.grid(row=9, column=0)
z_label.grid(row=10, column=0)

caluculate.grid(row=12,column=0)
frame.grid(row=12,column=1)

#show_trans_matrix.grid(row=13,column=0)


#l_label.grid(row=1, column=0)
#l_label.grid(row=1, column=0)

l.grid(row=1, column=1,padx=5,pady=10,ipady=10)
r.grid(row=2, column=1,padx=5,pady=10,ipady=10)
t.grid(row=3, column=1,padx=5,pady=10,ipady=10)
b.grid(row=4,column=1,padx=5,pady=10,ipady=10)
f.grid(row=5, column=1,padx=5,pady=10,ipady=10)
n.grid(row=6, column=1,padx=5,pady=10,ipady=10)
x.grid(row=8, column=1,padx=5,pady=10,ipady=10)
y.grid(row=9, column=1,padx=5,pady=10,ipady=10)
z.grid(row=10, column=1,padx=5,pady=10,ipady=10)


root.mainloop()




