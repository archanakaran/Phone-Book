import tkinter
from tkinter import *
window=Tk()
window.title('python')
window.minsize(100,100)
window.maxsize(600,600)
window.geometry('500x500')
e1=Entry(window,text='entry')
e1.grid(ipadx=50,ipady=10,row=0,column=0)
frame1=Frame(window,width=10,height=10)
frame1.grid(row=1,column=0,ipadx=0)
frame2=Frame(window,width=10,height=10)
frame2.grid(row=2,column=0,ipadx=0)
operation=0
def but1():
        e1.insert(END,'7')
        print(7)
        print(type(7))

        print(e1)
def but2():
        e1.insert(END,'8')
        print(8)
        print(e1)
def but3():
        e1.insert(END,'9')
        print(e1)
        print(e1)
def but5():
        e1.insert(END,'4')
        print(e1)
def but6():
        e1.insert(END,'5')
        print(e1)
def but7():
        e1.insert(END,'6')
        print(e1)
        print(e1)
def but9():
        e1.insert(END,'1')
        print(e1)
def but10():
        e1.insert(END,'2')
        print(e1)
def but11():
        e1.insert(END,'3')
        print(e1)

def but13():
        e1.insert(END,'c')
        print(e1)
        e1.delete(0,END)



def but14():
        x=(e1.get())
        if x!='0':
         e1.insert(END,'0')
         print(e1)

def but4():
        global operation
        x=(e1.get())
        print(type(x))
        if x[-1]==operation:
            # e1.insert(END,'+')
            e1.delete(len(e1.get())-1,END)
            # e1.delete(len(e1.get())-1,END)
            e1.insert(END,'+')
            
        else:
            e1.insert(END,'+')
        operation='+'
        

def but8():
        global operation
        x=(e1.get())
        print(type(x))
        if x[-1]==operation:
            e1.delete(len(e1.get())-1,END)
            # e1.delete(len(e1.get())-1,END)
            e1.insert(END,'-')
        else:
            e1.insert(END,'-')
        operation='-'

def but12():
        global operation
        x=(e1.get())
        print(type(x))
        if x[-1]==operation:
        # e1.delete(len(e1.get())-1,END)
            e1.delete(len(e1.get())-1,END)
            e1.insert(END,'*')
            print(e1)
        else:
              e1.insert(END,'*')
        print(e1)
        operation='*'

def but16():
        global operation
        global x
        x=e1.get()
        if x[-1]==operation:
            e1.delete(len(e1.get())-1,END)
            # e1.delete(len(e1.get())-1,END)
            e1.insert(END,'/')
            print(e1)
        else:
            e1.insert(END,'/')
        print(e1)
        operation='/'

def but17():
        e1.delete(len(e1.get())-1,END)
        
        
def but18():
        e1.insert(END,'.')

def but15():
        if operation=='+':
            sec=eval(e1.get())
            print(type(sec))
        #     res=x+sec
        #     print(type(res))
            e1.delete(0,END)
        #     print(res)
            e1.insert(END,sec)
            e1.insert(END+1,'=')
            print(e1)
        if operation=='-':
            sec=eval(e1.get())
        #     res=sec-x
            print(sec)
            e1.delete(0,END)
            e1.insert(END,sec)
        if operation=='*':
            sec=eval(e1.get())
            # res=x*sec
            e1.delete(0,END)
            e1.insert(END,sec)
        if operation=='/':
            sec=eval(e1.get())
            e1.delete(0,END)
            e1.insert(END,sec)
but1=Button(frame1,bg='pink',width=6,height=3,text='7',command=but1)
but1.grid(row=0,column=0,ipadx=0)
but2=Button(frame1,bg='pink',width=6,height=3,text='8',command=but2)
but2.grid(row=0,column=1)
but3=Button(frame1,bg='pink',width=6,height=3,text='9',command=but3)
but3.grid(row=0,column=2)
but4=Button(frame1,bg='pink',width=6,height=3,text='+',command=but4)
but4.grid(row=0,column=3)
but5=Button(frame1,bg='pink',width=6,height=3,text='4',command=but5)
but5.grid(row=1,column=0)
but6=Button(frame1,bg='pink',width=6,height=3,text='5',command=but6)
but6.grid(row=1,column=1)
but7=Button(frame1,bg='pink',width=6,height=3,text='6',command=but7)
but7.grid(row=1,column=2)
but8=Button(frame1,bg='pink',width=6,height=3,text='-',command=but8)
but8.grid(row=1,column=3)
but9=Button(frame1,bg='pink',width=6,height=3,text='1',command=but9)
but9.grid(row=2,column=0)
but10=Button(frame1,bg='pink',width=6,height=3,text='2',command=but10)
but10.grid(row=2,column=1)
but11=Button(frame1,bg='pink',width=6,height=3,text='3',command=but11)
but11.grid(row=2,column=2)
but12=Button(frame1,bg='pink',width=6,height=3,text='*',command=but12)
but12.grid(row=2,column=3)
but13=Button(frame1,bg='pink',width=6,height=3,text='c',command=but13)
but13.grid(row=3,column=0)
but14=Button(frame1,bg='pink',width=6,height=3,text='0',command=but14)
but14.grid(row=3,column=1)
but15=Button(frame1,bg='pink',width=6,height=3,text='=',command=but15)
but15.grid(row=3,column=2)
but16=Button(frame1,bg='pink',width=6,height=3,text='/',command=but16)
but16.grid(row=3,column=3)
but17=Button(frame2,bg='pink',width=21,height=3,text='<-',command=but17)
but17.grid(row=4,column=0)
but18=Button(frame2,bg='pink',width=6,height=3,text='.',command=but18)
but18.grid(row=4,column=1)
e1=Entry(window,text='entry')
e1.grid(ipadx=50,ipady=10,row=0,column=0)

    
mainloop()



