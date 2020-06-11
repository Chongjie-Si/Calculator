from tkinter import *
import operator

lists = []
# 设置一个变量 保存运算数字和符号的列表


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.frame = Frame
        self.master.geometry('320x450')
        self.master.resizable(0, 0)
        self.center_window(self.master, 320, 450)

        # 阻止Python GUI的大小调整
        self.createWidgets()

    def createWidgets(self):

        # 显示面板
        self.result = StringVar()
        self.result.set(0)  # 显示面板显示结果1，用于显示默认数字0
        self.result2 = StringVar()  # 显示面板显示结果2，用于显示计算过程
        self.result2.set('')
        # 显示面板设置
        self.label = Label(self.master, font=('微软雅黑', 20), bg='#FFFFFF', bd='0', fg='#828282', anchor='se',
                       textvariable=self.result2)
        self.label.place(width=320, height=130)
        self.label2 = Label(self.master, font=('微软雅黑', 25), bg='#FFFFFF', bd='0', fg='black', anchor='se',
                        textvariable=self.result)
        self.label2.place(y=130, width=320, height=70)

        # 键盘
        self.Button1 = Button(self.master, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0,
                              command=lambda: self.pressNum('7', event=None))
        self.Button1.place(x=0, y=250, width=80, height=50)

        self.Button2 = Button(self.master, text='8', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0,
                              command=lambda: self.pressNum('8', event=None))
        self.Button2.place(x=80, y=250, width=80, height=50)
        self.Button3 = Button(self.master, text='9', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0,
                              command=lambda: self.pressNum('9', event=None))
        self.Button3.place(x=160, y=250, width=80, height=50)
        self.Button4 = Button(self.master, text='4', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                              command=lambda: self.pressNum('4', event=None))
        self.Button4.place(x=0, y=300, width=80, height=50)
        self.Button5 = Button(self.master, text='5', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                              command=lambda: self.pressNum('5', event=None))
        self.Button5.place(x=80, y=300, width=80, height=50)
        self.Button6 = Button(self.master, text='6', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                              command=lambda: self.pressNum('6', event=None))
        self.Button6.place(x=160, y=300, width=80, height=50)
        self.Button7 = Button(self.master, text='1', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                              command=lambda: self.pressNum('1', event=None))
        self.Button7.place(x=0, y=350, width=80, height=50)
        self.Button8 = Button(self.master, text='2', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                              command=lambda: self.pressNum('2', event=None))
        self.Button8.place(x=80, y=350, width=80, height=50)
        self.Button9 = Button(self.master, text='3', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                              command=lambda: self.pressNum('3', event=None))
        self.Button9.place(x=160, y=350, width=80, height=50)
        self.Button10 = Button(self.master, text='.', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                               command=lambda: self.pressNum('.', event=None))
        self.Button10.place(x=0, y=400, width=80, height=50)
        self.Button11 = Button(self.master, text='0', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#FFFFF0'), bd=0.1,
                               command=lambda: self.pressNum('0', event=None))
        self.Button11.place(x=80, y=400, width=80, height=50)

# 运算
        self.Button12 = Button(self.master, text='=', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#EED8AE'), bd=0.1,
                               command=lambda: self.pressEqual(event=None))
        self.Button12.place(x=160, y=400, width=80, height=50)
        self.master.bind('<Return>', self.pressEqual)


        self.Button13 = Button(self.master, text='+', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#F5FFFA'), bd=0.1,
                               command=lambda: self.pressOperator('+', event=None))
        self.Button13.place(x=240, y=250, width=80, height=50)
        self.Button14 = Button(self.master, text='-', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#F5FFFA'), bd=0.1,
                               command=lambda: self.pressOperator('-', event=None))
        self.Button14.place(x=240, y=300, width=80, height=50)
        self.Button15 = Button(self.master, text='*', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#F5FFFA'), bd=0.1,
                               command=lambda: self.pressOperator('*', event=None))
        self.Button15.place(x=240, y=350, width=80, height=50)
        self.Button16 = Button(self.master, text='/', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#F5FFFA'), bd=0.1,
                               command=lambda: self.pressOperator('/', event=None))
        self.Button16.place(x=240, y=400, width=80, height=50)


        self.Button17 = Button(self.master, text='清零', font=('微软雅黑', 15), fg=('#4F4F4F'), bg=('#FFEC8B'), bd=0.1,
                               command=lambda: self.Clr(event=None))
        self.Button17.place(x=0, y=200, width=80, height=50)
        self.Button18 = Button(self.master, text='^2', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#F5FFFA'), bd=0.1,
                               command=lambda: self.Square(event=None))
        self.Button18.place(x=80, y=200, width=80, height=50)
        self.Button19 = Button(self.master, text='sqrt', font=('微软雅黑', 20), fg=('#4F4F4F'), bg=('#F5FFFA'), bd=0.1,
                               command=lambda: self.Sqrt(event=None))
        self.Button19.place(x=160, y=200, width=80, height=50)
        self.Button20 = Button(self.master, text='删除', font=('微软雅黑', 15), fg=('#4F4F4F'), bg=('#FFEC8B'), bd=0.1,
                               command=lambda: self.BackSp(event=None))
        self.Button20.place(x=240, y=200, width=80, height=50)

    # 数字键处理函数，属于selflication()类
    def pressNum(self, val, event):
        global lists
        lists.append(val)
        # 使用join()将列表转换成字符串，再显示到Label中
        self.result.set(''.join(lists))

    # 运算符号键处理函数，属于selflication()类
    def pressOperator(self, val, event):
        global lists
        if len(lists) > 0:
            if lists[-1] in ['+','-','*','/']:
                lists[-1] = val
            else:
                lists.append(val)
            self.result.set(''.join(lists))

    # 等号键处理函数
    def pressEqual(self, event):
        global lists
        if len(lists) > 0:
            if operator.eq(lists, ['1', '+']):
                lists.clear()
                self.result2.set('')
                self.result.set('Python')
            else:
                if lists[-1] in ['+', '-', '*', '/']:
                    del lists[-1]
                computrStr = ''.join(lists)  # 将列表内容用join命令将字符串链接起来
                endNum = eval(computrStr)  # 用eval命令运算字符串中的内容
                self.result.set(endNum)  # 将运算结果显示到屏幕1
                self.result2.set(computrStr)  # 将运算过程显示到屏幕2
                lists.clear()  # 清空列表内容
                lists.append(str(endNum))  # 将计算结果存到列表中，以便下一步计算

    # 清零键处理函数
    def Clr(self, event):
        self.result.set('0')  # 将运算结果显示到屏幕1
        self.result2.set('')  # 将运算过程显示到屏幕2
        lists.clear()  # 清空列表内容

    # 删除键处理函数
    def BackSp(self, event):
        del lists[-1]
        if len(lists) == 0:
            self.result.set('0')  # 将运算结果显示到屏幕1
        else:
            computrStr = ''.join(lists)  # 将列表内容用join命令将字符串链接起来
            self.result.set(computrStr)  # 将运算结果显示到屏幕1

    def Square(self, event):
        if len(lists) == 0:
            self.result.set('0')  # 讲运算结果显示到屏幕1
        else:
            if lists[-1] in ['+', '-', '*', '/']:
                del lists[-1]
            computrStr = ''.join(lists)  # 将列表内容用join命令将字符串链接起来
            endNum = eval(computrStr)
            endNum = endNum * endNum
            self.result.set(endNum)  # 将运算结果显示到屏幕1
            self.result2.set('(' + computrStr + ')^2')
            lists.clear()  # 清空列表内容
            lists.append(str(endNum))  # 将计算结果存到列表中，以便下一步计算

    def Sqrt(self, event):
        if len(lists) != 0:
            if lists[-1] in ['+', '-', '*', '/']:
                del lists[-1]
            computrStr = ''.join(lists)  # 将列表内容用join命令将字符串链接起来
            endNum = eval(computrStr)
            endNum = endNum ** 0.5
            self.result.set(endNum)  # 将运算结果显示到屏幕1
            self.result2.set('sqrt(' + computrStr + ')')
            lists.clear()  # 清空列表内容
            lists.append(str(endNum))  # 将计算结果存到列表中，以便下一步计算

    # 窗口居中
    def center_window(self, root, width, height):
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(size)


'''

app = Application()
# 设置窗口标题:
app.master.title('计算器')
# 主消息循环:
app.master.mainloop()
'''