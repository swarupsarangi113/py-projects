
import os

'''
This is a script to automate parsing and renaming of my 'Python3 Tutorial' Playlist in my local machine and
arrange them by assigning number by order it should be watched so that they are sorted in the right order in my machine
'''

os.chdir('E:\\Python3 Tutorial')

with open('contents.txt', 'r') as rf:
    with open('new_contents.txt', 'r+') as wf:

        f_contents = rf.read()

        contents = f_contents.split('sentdex')
        for content in contents:
            content = content.split('\n')

            num, title = content[1], content[-2]
            new_title = '{}-{}.mp4'.format(num, title)
            # wf.write(new_title + '\n')

            title += '.mp4'

            if title in os.listdir():
                os.rename(title, new_title)
