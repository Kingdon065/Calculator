#! python3
# _*_ coding:utf-8 _*_

"""
@Project: 简易计算器
@Author: masiyuan
@Time: 2019-11-04
"""

from tkinter import *


class Calculator:
    def __init__(self):
        root = Tk()
        root.title('计算器')
        root.iconbitmap('icon/calc.ico')
        self.window_center(root, 760, 385)
        root.resizable(0, 0)
        root.attributes('-alpha', 0.92)      # 设置不透明度
        root.attributes('-topmost', 1)      # 窗口顶置

        self.exp = StringVar()
        self.exp.set('0')

        frame = Frame(root)
        frame.grid(row=0, column=0, pady=10, padx=5, columnspan=5, sticky=W + E)

        self.contentLabel = Label(frame, textvariable=self.exp, font=('Arial', 22), anchor=SE,
                                  height=2, relief=RAISED, bd=2, bg='#E6E6FA', justify=RIGHT,
                                  width=44, wraplength=750)
        # 清除键和删除键
        btnClear = Button(root, text='C', command=self.clear)
        btnDel = Button(root, text='DEL', command=self.backspace)
        # 运算符+ - * /
        btnP = Button(root, text='﹢', command=lambda: self.enter('+'))
        btnS = Button(root, text='-', command=lambda: self.enter('-'))
        btnM = Button(root, text='*', command=lambda: self.enter('*'))
        btnDiv = Button(root, text='/', command=lambda: self.enter('/'))
        # 数字键
        btn0 = Button(root, text='0', command=lambda: self.enter('0'))
        btn1 = Button(root, text='1', command=lambda: self.enter('1'))
        btn2 = Button(root, text='2', command=lambda: self.enter('2'))
        btn3 = Button(root, text='3', command=lambda: self.enter('3'))
        btn4 = Button(root, text='4', command=lambda: self.enter('4'))
        btn5 = Button(root, text='5', command=lambda: self.enter('5'))
        btn6 = Button(root, text='6', command=lambda: self.enter('6'))
        btn7 = Button(root, text='7', command=lambda: self.enter('7'))
        btn8 = Button(root, text='8', command=lambda: self.enter('8'))
        btn9 = Button(root, text='9', command=lambda: self.enter('9'))
        # . % ^ 和 =
        btnD = Button(root, text='.', command=lambda: self.enter('.'))
        btnPer = Button(root, text='%', command=lambda: self.enter('%'))
        btnExp = Button(root, text='x^y', command=lambda: self.enter('^'))
        btnE = Button(root, text='=', command=self.equal, bg='#F0E68C')

        btns = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9,
                btnD, btnP, btnDel, btnClear, btnM, btnS, btnE, btnDiv, btnPer, btnExp]

        for btn in btns:
            self.add_configures(btn)


        self.contentLabel.pack()

        btn7.grid(row=1, column=0, padx=5, pady=5)
        btn8.grid(row=1, column=1, padx=5, pady=5)
        btn9.grid(row=1, column=2, padx=5, pady=5)
        btnP.grid(row=1, column=3, padx=5, pady=5)
        btnClear.grid(row=1, column=4, padx=5, pady=5)

        btn4.grid(row=2, column=0, padx=5, pady=5)
        btn5.grid(row=2, column=1, padx=5, pady=5)
        btn6.grid(row=2, column=2, padx=5, pady=5)
        btnS.grid(row=2, column=3, padx=5, pady=5)
        btnDel.grid(row=2, column=4, padx=5, pady=5)

        btn1.grid(row=3, column=0, padx=5, pady=5)
        btn2.grid(row=3, column=1, padx=5, pady=5)
        btn3.grid(row=3, column=2, padx=5, pady=5)
        btnM.grid(row=3, column=3, padx=5, pady=5)
        btnExp.grid(row=3, column=4, padx=5, pady=5)

        btn0.grid(row=4, column=0, padx=5, pady=5)
        btnPer.grid(row=4, column=1, padx=5, pady=5)
        btnD.grid(row=4, column=2, padx=5, pady=5)
        btnDiv.grid(row=4, column=3, padx=5, pady=5)
        btnE.grid(row=4, column=4, padx=5, pady=5)

        root.mainloop()

    def window_center(self, window, width, height):
        # 窗口居中
        win_width = window.winfo_screenwidth()
        win_height = window.winfo_screenheight()
        x = int((win_width - width) / 2)
        y = int((win_height - height) / 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

    def add_configures(self, btn):
        # 添加配置
        btn.config(font=('Times', 14, 'bold'))
        btn.config(width=12, height=2)
        btn.config(bd=2)

    def enter(self, char):
        # 键入字符
        content= self.exp.get()
        # 如果内容中有=号, 继续键入时只保留其结果
        if '=' in content:
            content = content.split('=')[1]
        if content == '\n0' or content == '0':
            content = ''
        if content == 'Error':
            content = ''
        self.exp.set(content + char)

    def clear(self):
        # 清空文本框, 并重置为0
        self.exp.set('0')

    def backspace(self):
        # 每次删除最后一个字符
        content = self.exp.get()
        if '=' in content:
            return
        if content == '\n0':
            self.clear()
        if len(content) == 1:
            self.clear()
        else:
            self.exp.set(content[:-1])

    def equal(self):
        content = self.exp.get()
        if '=' in content or content == '0':
            return
        # 计算结果
        try:
            result = eval(content.replace(',', '').replace('^', '**'))
            self.exp.set(f'{content}=\n{result:,}')
        except:
            self.clear()
            self.exp.set('Error')


if __name__ == '__main__':
    Calculator()