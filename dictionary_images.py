# ~ Hi everyone this is one of my projects which is one of the real world
# ~ problems. So when I learned English language of course there were a lot of
# ~ unknown words. What to do? In my opinion when you search some word there
# ~ must bew the meaning and the picture for visualizing it. If somebody say me
# ~ answer would be that how do you imagine 'important'(adjective) using some
# ~ picture --> we choose some picture which is you easly understand and also
# ~ give the precise explaining and of course its meaning. ***[version 1.0]***
# ~ author @eltacshikhsaidov created 12/2/2019


import webbrowser # we import it for opening links in web brwoser
import sys
import time

dictionary_of_words = {
    'cpu':'https://www.notebookcheck.net/fileadmin/Notebooks/\ # just add one or two words
News/_nc3/download37.png',
    'computer':'https://cdn.britannica.com/77/170477-050-1C747EE3\ # and also links
/Laptop-computer.jpg',
}

print('============================================')
print('Welcome to our dictionary ***version-1.0***')
print('============================================\n')

while True:
    # Search some word
    searched_word = input('\nSearch: ')

    # Special keyword 'look at words'
    # if we type it print() function will return all words in the dictionary
    if searched_word == 'look at the words':

        for keys in dictionary_of_words:
            print(keys)

    else:
        if searched_word in dictionary_of_words.keys():
            print('Please wait....')
            print('\nopening the picture of word...')

            # using this piece of code program automatically open link belong to searched word
            webbrowser.open(dictionary_of_words[searched_word])

            # Just adding a litte animation for fun
            for i in range(101):
                str = f'{i}' + '%'
                print(f'\r{str}',end = '')

        # If you want to you can improve dictionary
        else:
            print('The entered word has not in the dictionary\n\
do you want to add it? y\\n')

            answer_of_user = input('your answer: ')

            if answer_of_user == 'y':

                print('Please enter the link of picture\nmake sure that the link\'s\
address ends with \'.jpg\' or something like this')
                user_entered_picture_link = input('link -->')
                print('Are you sure that entered link is correct? y\\n')
                yes_or_no = input('answer is: ')

                if yes_or_no == 'y':

                    # You can write either first or second piece of code and it doesn't matter
                    # dictionary_of_words[searched_word] = user_entered_picture_link
                    dictionary_of_words.update({searched_word:user_entered_picture_link})
                    print('The word and it\'s picture is successfully added')
                    print('Thank you for adding new word to our dictionary')

                else:
                    print('Please enter correct link')
                    new_entered_link = input('new link --> ')
                    # This piece of code is the same as below piece of code
                    # dictionary_of_words[searched_word] = new_entered_link
                    dictionary_of_words.update({searched_word:user_entered_picture_link})
                    print('The word and it\'s picture is successfully added')
                    print('Thank you for adding new word to our dictionary')

            else:
                print('Do you want to search another word or just to exit?')
                print('exit\\continue')

                answer = input('answer is: ')
                if answer == 'exit':

                    animation = "|/-\\"
                    i = 20
                    print('exiting to program...')

                    # Again adding a little animation for fun
                    while i > 0:
                        print(animation[i % len(animation)], end="\r")
                        i = i - 1
                        time.sleep(0.1)
                    sys.exit(0)
                else:
                    continue
