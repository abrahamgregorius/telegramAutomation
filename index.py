import uiautomator2 as u2
import os
import main

d = u2.connect('R9CT4000AAM')


def startApp():
    d.app_start('org.telegram.messenger')

def openChat():
    text = "hello"
    split = [*text.upper()]
    for i in split:
        os.system(f'cd ')
        os.system(f'python main.py press'+ i + '()')
openChat()