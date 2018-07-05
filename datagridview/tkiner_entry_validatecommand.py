
"""

@Author: 舍名利

@Blog  : www.cnblogs.com/shemingli

@GitHub: github.com/GratefulHeartCoder

@Date  : 2018/4/2

"""

from tkinter import *

 

 

def main():

    def _test():

        if inputStr.get() != '舍名利':

            judge_res.set('输入的不是舍名利')

            return False

        else:

            judge_res.set('输入的是舍名利')

            return True

 

    root = Tk()

 

    content = StringVar()

    inputStr = Entry(root,

                     textvariable=content,  # 内容可变

                     validate="focusout",  # 失去焦点调用test函数

                     validatecommand=_test

                     )

    inputStr.grid(row=0, column=0, pady=10, padx=10)

 

    # 靠西

    Label(root, text="judge:").grid(row=1, column=0,

                                    sticky=W, pady=10, padx=10)

    judge_res = StringVar()

 

    Label(root, textvariable=judge_res).grid(row=1, column=1,

                                             pady=10, padx=10)

 

    mainloop()

 

 

if __name__ == '__main__':

    main()