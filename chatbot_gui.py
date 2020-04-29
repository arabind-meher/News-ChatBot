from tkinter import *
from tkinter import ttk


class ChatBot:
    def __init__(self):
        master = Tk()

        master.title('News Bot')
        master.geometry('500x600')
        master.resizable(0, 0)

        label = Label(
            master,
            font=('Times New Roman', 25, 'bold'),
            text='News Bot'
        )

        text = Text(
            master,
            state='disabled',
            font=('Times New Roman', 15),
            height=20,
            width=45
        )

        reply = StringVar()
        entry = Entry(
            master,
            textvariable=reply,
            font=('Times New Roman', 15),
            width=25
        )

        def send_reply():
            text.configure(state=NORMAL)
            text.insert(END, '---]  ' + reply.get() + '\n')
            text.configure(state='disabled')

        button = Button(
            master,
            text='Enter',
            command=send_reply,
            font=('Times New Roman', 20)
        )

        label.pack(fill=X)
        text.pack()
        entry.pack(pady=10)
        button.pack()

        master.mainloop()


if __name__ == '__main__':
    ChatBot()
