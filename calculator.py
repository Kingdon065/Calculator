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
        self.window_center(root, 640, 305)
        root.resizable(0, 0)
        root.attributes('-alpha', 0.9)      # 设置不透明度
        root.attributes('-topmost', 1)      # 窗口顶置

        self.expression = Entry(root, justify='right', font=('宋体', 22), bd=2)
        # 清除键和删除键
        btnClear = Button(root, text='C', command=self.clear)
        btnDel = Button(root, text='Del', command=self.delete)
        # 运算符+ - * /
        btnP = Button(root, text='+', command=lambda: self.enter('+'))
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
        # 句点 . 和 =
        btnD = Button(root, text='.', command=lambda: self.enter('.'))
        btnE = Button(root, text='=', command=self.equal)

        btns = [btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9,
                btnD, btnP, btnDel, btnClear, btnM, btnS, btnE, btnDiv]

        for btn in btns:
            self.add_configures(btn)

        self.expression.grid(row=0, column=0, columnspan=5, pady=10, padx=5, sticky=W+E)

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
        btnE.grid(row=3, column=4, padx=5, pady=5, rowspan=2, sticky=N+S)

        btn0.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky=W+E)
        btnD.grid(row=4, column=2, padx=5, pady=5)
        btnDiv.grid(row=4, column=3, padx=5, pady=5)

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
        btn.config(font=('Times', 12, 'bold'))
        btn.config(width=12, height=2)
        btn.config(bd=2)

    def enter(self, char):
        # 键入字符
        if self.expression.get() == 'Error':
            self.clear()
        self.expression.insert(END, char)   # 从末尾添加字符

    def clear(self):
        # 清空文本框
        self.expression.delete(0, END)

    def delete(self):
        # 每次删除最后一个字符
        tmp = self.expression.get()
        self.clear()
        self.enter(tmp[:-1])

    def equal(self):
        # 计算结果
        try:
            result = eval(self.expression.get().replace(',', ''))
            self.clear()
            self.enter(f'{result:,}')
        except:
            self.clear()
            self.enter('Error')


if __name__ == '__main__':
    Calculator()