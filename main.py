from tkinter import *
from tkinter import filedialog

import os.path

root = Tk()

def browse_file():
    file = filedialog.askopenfile()
    print(file.name)
    current_dir = os.getcwd()
    file_name = file.name
    if '\\' in file.name:
        file_name = list(map(lambda x: '/' if x == '\\' else x, list(file.name)))
    browse_dir = file_name[:file_name.rfind('/')]
    os.chdir(browse_dir)



root['bg'] = '#fafafa'
root.title('Счетчик символов')
root.wm_attributes('-alpha', 0.7)
root.geometry('300x250')
root.resizable(width=False, height=True)

frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

# cityField = Entry(frame_top, bg='white', font=30)
# cityField.pack()

btn = Button(frame_top, text='Выбрать файл', command=browse_file)
btn.pack()

info = Label(frame_bottom, text='Частота символов', bg='#ffb700', font=40)
info.pack()

if __name__ == '__main__':
    root.mainloop()
