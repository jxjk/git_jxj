import tkinter
import random
     
def suijishu(a, b):
    t.delete(1.0, 'end')
    t.insert('end', random.randint(a, b))
    t.after(500, suijishu, a, b)
 

def test():
	print('test')


top = tkinter.Tk()
 
t = tkinter.Text(top)
t.pack(expand=1, fill='both')
suijishu(51, 100)
ent_shuru = tkinter.Entry(top ,validate = 'focusout',validatecommand = test)
ent_shuru.pack(padx =5,pady =5)


top.mainloop()
