from tkinter import *

window=Tk()

def convert_result(): #단위를 바꾸는 함수
    kg_input=float(e1_value.get())
    grams=kg_input*1000
    pounds=kg_input*2.20462
    ounces=kg_input*35.274
    result_grams.insert(END, grams)
    result_pounds.insert(END, pounds)
    result_ounces.insert(END, ounces)

text_kg=Label(window, text="Kg", height=1, width=10)
text_kg.grid(row=0, column=0) #단순히 kg 문자 표시

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value, width=10)
e1.grid(row=0, column=1) #숫자를 입력 받을 칸

b1=Button(window, text="Convert", command=convert_result)
b1.grid(row=0, column=2) #버튼

text_grams=Label(window, text="Label", height=1, width=10)
text_grams.grid(row=1, column=0) #단순히 Grams 문자열 표시
result_grams=Text(window, height=1, width=10)
result_grams.grid(row=2, column=0) #gram 결과값 표시할 Text

text_pounds=Label(window, text="Pounds", height=1, width=10)
text_pounds.grid(row=1, column=1) #단순히 Pounds 문자열 표시
result_pounds=Text(window, height=1, width=10)
result_pounds.grid(row=2, column=1) #pound 결과값 표시할 Text

text_ounces=Label(window, text="Ounces", height=1, width=10)
text_ounces.grid(row=1, column=2) #단순히 Ounces 문자열 표시
result_ounces=Text(window, height=1, width=10)
result_ounces.grid(row=2, column=2) #ounce 결과값 표시할 Text

window.mainloop()
