import tkinter

# 윈도우 창 설정
window = tkinter.Tk()
window.title("계산기")
window.geometry("400x500")
window.resizable(False, False)

# 전역변수 - 수식 저장용
current_expression = ""

# Entry 위젯 (입력창)
entry_field = tkinter.Entry(window, bd=10, font=('Arial', 24), justify='right')
entry_field.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=10, pady=10)

# 버튼 레이블 (4x4)
button_labels = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# 함수 정의

def clear_entry():
    global current_expression
    current_expression = ""
    entry_field.delete(0, 'end')

def calculate():
    global current_expression
    try:
        result = eval(entry_field.get())
        clear_entry()
        entry_field.insert(0, str(result))
        current_expression = str(result)
    except Exception as e:
        clear_entry()
        entry_field.insert(0, "Error")

def click_button(label):
    global current_expression
    if label == 'C':
        clear_entry()
    elif label == '=':
        calculate()
    else:
        current_expression += label
        entry_field.insert(tkinter.END, label)

# Grid 설정
# 행 (Entry + 버튼 4줄 = 총 5줄)
for r in range(5):
    window.grid_rowconfigure(r, weight=1, uniform="row")

# 열 (4열)
for c in range(4):
    window.grid_columnconfigure(c, weight=1, uniform="col")

# 버튼 배치
for r in range(4):
    for c in range(4):
        label = button_labels[r][c]
        button = tkinter.Button(
            window,
            text=label,
            font=('Arial', 20),
            bg='#f0f0f0',
            command=lambda l=label: click_button(l)
        )
        button.grid(row=r+1, column=c, sticky='nsew', padx=2, pady=2)

# 실행
window.mainloop()
