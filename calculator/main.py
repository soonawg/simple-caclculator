#import tkinter as tk   # tkinter는 GUI 모듈을 제공하는 패키지이다.
from tkinter import Tk, Entry, Button, StringVar

# 계산기
# 1. 계산기 기능이 구현되어야 함
# 2. GUI

class Calculator:
    def __init__(self, window):
        window.title("Calculator 🎲")  # title() 윈도우 창의 제목을 정한다.
        window.geometry("357x420+0+0")  # geometry("가로x세로+x좌표+y좌표") 창의 크기를 정하고, 좌상단을 기준으로 창이 나오는 좌표값을 정한다.
        window.config(bg='gray')  # 계산기 배경 색 설정
        window.resizable(False, False)  # resizeable(False, False) 창 크기 변경 불가 (X, Y)

        self.equation = StringVar()
        self.entry_value=''
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)  # 입력창을 생성한다. 너비 17, 배경색 ccddff, 폰트 Arial Bond, textvariable 입력창에 표시할 문자

        Button(width=11, height=4, text='(', relief='flat', bg='white', command=lambda:self.show('(')).place(x=0, y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda:self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda:self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='white', command=lambda:self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='white', command=lambda:self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='white', command=lambda:self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='white', command=lambda:self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='white', command=lambda:self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='white', command=lambda:self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='white', command=lambda:self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='white', command=lambda:self.show(8)).place(x=90, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='white', command=lambda:self.show(9)).place(x=180, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='white', command=lambda:self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda:self.show('.')).place(x=180, y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white', command=lambda:self.show('+')).place(x=270, y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda:self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda:self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda:self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='=', relief='flat', bg='white', command=self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', command=self.clear).place(x=0, y=350)
    
    def show(self, value):  # 입력 기능 구현
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
    
    def clear(self):  # 계산기의 C 기능 구현
        self.entry_value = ''
        self.equation.set(self.entry_value)
    
    def solve(self):  # 계산 기능 구현 eval 함수 이용.
        result = eval(self.entry_value)
        self.equation.set(result)
    

window = Tk()  # tk.Tk()를 사용해서 객체를 생성한다.
calculator = Calculator(window)
window.mainloop()
