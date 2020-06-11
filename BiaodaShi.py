from tkinter import Label, Entry, StringVar, Button, N, RIGHT, W, E, messagebox, Menu,Tk
from math import sin, cos


class Biaodashi:
    def __init__(self, root):
        self.root = root
        self.root.title('计算器')
        self.center_window(self.root, 320, 240)
        self.root.minsize(500, 100)
        self.root.maxsize(600, 100)

        self.type = 1

        self.label1 = Label(root, text='请输入表达式：').grid(row=0, column=0)
        self.e = Entry(root,width=40)
        self.e.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.var = StringVar()
        self.var.set('')
        self.label2 = Label(root, textvariable=self.var)
        self.label2.grid(row=2, column=1, sticky=W)
        self.button = Button(self.root, text='确定', width=10, command=lambda: self.show(event=None)).grid(row=2, column=0, padx=10, pady=5)
        self.root.bind('<Return>',  self.show)
        # Button(self.root, text="返回", width=10, command=self.quittype).grid(row=2, column=1, padx=10, pady=5, sticky=E)


    # 计算核心代码
    def varset(self, ev):
        self.var.set(ev)

    def show(self, event):
        mes = self.e.get()
        try:
            ev = eval(mes)
        except (SyntaxError, UnboundLocalError, NameError):
            self.varset('请输入正确的表达式')
            self.errorwin()
        else:
            self.varset(round(ev, 20))

    # 窗口居中
    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

    # 小型弹窗
    def errorwin(self):
        self.errorw = messagebox.showinfo(title='Error', message='请输入正确的表达式')
'''
tk= Tk()
e=Biaodashi(tk)
e.root.mainloop()
'''