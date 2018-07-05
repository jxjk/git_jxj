from tkinter import *


def rtnkey(event=None):
    print(e.get())
    entry.delete(0,END)


root = Tk()
e = StringVar()
entry = Entry(root, validate='key', textvariable=e, width=50)
entry.pack()
entry.bind('<Return>', rtnkey)
root.title('测试回车获取文本框内容')
root.mainloop()