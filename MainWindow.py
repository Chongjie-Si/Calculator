# -*- coding: utf8 -*-
from tkinter import Tk, Label, LabelFrame, Radiobutton, Button, LEFT, RIGHT, TOP, IntVar, W, Toplevel, messagebox, Menu
from BiaodaShi import Biaodashi
from Xiaojianpan import Application


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title('计算器一代')
        self.center_window(self.root, 300, 240)
        self.root.maxsize(200, 200)
        self.root.minsize(200, 200)

        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)
        aboutMenu = Menu(self.menuBar, tearoff=0)
        # 创建一个下拉菜单‘功能’，这个菜单是挂在menubar（顶级菜单）上的
        FuncMenu = Menu(self.menuBar, tearoff=0)
        # 用add_cascade()将菜单添加到顶级菜单中，按添加顺序排列
        self.menuBar.add_cascade(label='功能', menu=FuncMenu)
        self.menuBar.add_cascade(label='帮助', menu=aboutMenu)
        # 下拉菜单的具体项目，使用add_command()方法
        aboutMenu.add_command(label='关于..', command=self.About)

        FuncMenu.add_command(label='小键盘计算', command=self.Fun2)
        FuncMenu.add_command(label='表达式计算', command=self.Fun1)

        self.label = Label(self.root, text='欢迎使用！', font=14).pack(side=TOP)
        self.group = LabelFrame(self.root, text='您想进行的操作是：', padx=5, pady=5)
        self.group.pack(padx=10, pady=10)
        self.Key = [('小键盘计算', 1), ('表达式计算', 2)]
        self.v = IntVar()
        self.v.set(1)
        for m, n in self.Key:
            b = Radiobutton(self.group, text=m, variable=self.v, value=n)
            b.pack(anchor=W)

        self.button1 = Button(self.root, text='确定', command=self.show, padx=10)
        self.button2 = Button(self.root, text='退出', command=self.root.quit, padx=10)
        self.button1.pack(side=RIGHT)
        self.button2.pack(side=LEFT)

        self.root.bind('<Return>', self.show)
    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)

    def show(self, event):
        if self.v.get() == 1:
            newwin = Toplevel()
            app = Application(newwin)
            # 设置窗口标题:
            app.master.title('计算器')
            # 主消息循环:
            app.master.mainloop()

        elif self.v.get() == 2:
            newwin = Toplevel()
            e = Biaodashi(newwin)
            e.root.mainloop()

    def About(self):
        messagebox.showinfo('关于', 'Ver 1.0 \n--------\nBy Mark\n')

    def Fun1(self):
        messagebox.showinfo('表达式计算', '输入计算的数学表达式即可\n• 请使用半角符号\n• 请注意乘方请以**表示')

    def Fun2(self):
        messagebox.showinfo('小键盘计算', '点击数字以及符号按键计算即可\n仅支持简单计算')

RtMain = Tk()
t = Main(RtMain)
RtMain.mainloop()
