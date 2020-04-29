from tkinter import *

from news_api import NewsApi


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
            borderwidth=5,
            font=('Arial', 12),
            height=25,
            width=60,
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

            news = NewsApi.get_news(query=reply.get())

            if news == Exception:
                text.configure(state=NORMAL)
                text.insert(END, news + '\n')
            else:
                print_news(news)

        def print_news(news):
            text.configure(state=NORMAL)
            for i in range(5):
                text.insert(END, str(i + 1) + '.\n')
                text.insert(END, news[i][0] + '\n')
                text.insert(END, news[i][1] + '\n\n')
                text.insert(END, 'Author: ' + str(news[i][3]) + '\n')
                text.insert(END, 'Source: ' + str(news[i][4]) + '\n\n')
                text.insert(END, str(news[i][5]) + '\n\n')
                text.insert(END, 'Polarity=' + str(news[i][6]) + '\t' + 'Subjectivity=' + str(news[i][7]) + '\n')
                text.insert(END, '------------------------------------------------------------\n\n')

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
