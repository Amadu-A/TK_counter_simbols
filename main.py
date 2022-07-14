from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os.path


root = Tk()


def browse_file():
    try:
        file = filedialog.askopenfile()
        current_dir = os.getcwd()
        path = file.name
        if not path.endswith('.txt'):
            messagebox.showerror(title='Ошибка', message='Выберите файл с расширением .txt')
            raise Exception('Ошибка выбора')
    except Exception:
        pass
    else:
        if '\\' in file.name:
            path = ''.join(list(map(lambda x: '/' if x == '\\' else x, list(file.name))))
        if '/' in path:
            browse_dir = path[:path.rfind('/')]
        os.chdir(browse_dir)
        file_name = path[path.rfind('/') + 1:]
        cnt_symbols(file_name)
        os.chdir(current_dir)


def cnt_symbols(file_name):
    rate = dict()
    with open(file_name, 'r') as file:
        total_cnt_symbols = 0
        for i_line in file:
            total_cnt_symbols += len(i_line)
            line_lst = list(i_line)
            for symbol in line_lst:
                if symbol not in rate:
                    rate[symbol] = 0
                rate[symbol] += 1
    rate = dict(sorted(rate.items(), key=lambda x: x[0]))
    scroll = Scrollbar(root)
    scroll.pack(side=RIGHT, fill=Y)
    listbox = Listbox(frame_bottom, width=200, height=250, bg='#ffb700', font=40, yscrollcommand=scroll.set)

    for symbol, count in rate.items():
        listbox.insert(END, f'{symbol}: {round(count / total_cnt_symbols * 100, 2)}%')
    listbox.pack(side=LEFT)
    scroll.config(command=listbox.yview)


root['bg'] = '#fafafa'
root.title('Счетчик символов')
root.wm_attributes('-alpha', 0.7)
root.geometry('300x400')
root.resizable(width=False, height=True)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.10)
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.20, relwidth=0.7, relheight=0.7)

btn = Button(frame_top, text='Выбрать файл', command=browse_file)
btn.pack()

if __name__ == '__main__':
    root.mainloop()
