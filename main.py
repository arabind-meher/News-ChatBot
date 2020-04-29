from newsbot_gui import NewsBot

if __name__ == '__main__':
    # Default Introduction Message
    message = 'Hii! I am your NewsBot.\nIf you type any query I will provide you with the information\n\n'
    message += 'Note that I am not a regular ChatBot.\nSo, please type query that you want to search for.\n\n'

    message += 'Query Result:\n'
    message += '---) Title (English)\n'
    message += '---) Title (Hindi)\n'
    message += '---) Author\n'
    message += '---) Source\n'
    message += '---) URL\n'
    message += '---)Polarity & Subjectivity\n\n'

    message += 'Please type your query in Entry field.\n\n'

    # Call the newsbot function
    NewsBot(message)
