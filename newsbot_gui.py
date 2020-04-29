from tkinter import *

from news_api import NewsApi


class NewsBot:
    def __init__(self, message):
        master = Tk()

        master.title('News Bot')
        master.geometry('500x600')
        master.resizable(0, 0)

        # Heading for NewsBot
        label = Label(
            master,
            text='News Bot',
            font=('Times New Roman', 25, 'bold')
        )

        # Body of NewsBot
        text = Text(
            master,
            state='disabled',
            borderwidth=5,
            font=('Arial', 12),
            height=25,
            width=60,
        )
        text.configure(state=NORMAL)
        text.insert(END, message)
        text.configure(state='disabled')

        reply = StringVar()
        # Entry for manual input
        entry = Entry(
            master,
            textvariable=reply,
            font=('Times New Roman', 15),
            width=25
        )

        # Sending the query for processing
        def send_reply():
            text.configure(state=NORMAL)
            text.insert(END, '---]  ' + reply.get() + '\n')
            text.configure(state='disabled')

            news = NewsApi.get_news(query=reply.get())

            if news == 'Error':
                text.configure(state=NORMAL)
                text.insert(END, news + '\n')
                text.configure(state='disabled')
            else:
                print_news(news)

        # NewsBot reply
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

        # Button for submitting reply
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
