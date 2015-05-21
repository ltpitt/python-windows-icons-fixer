#!/usr/bin/python
__author__ = 'Davide Nastri'
__appname__ = "Windows icons fixer"
__version__ = "0.1beta"
__license__ = "MIT"
'''
This script will fix your badly visualized icons and the delay on creating folders on Windows Vista, 7, 8.
'''

import os
import sys
import time
import easygui

def kill_explorer():
    '''
    Kills explorer.exe
    '''


    try:
        os.system('taskkill /im explorer.exe /f')

    except Exception,e:
        pop_msgbox(e, title="Arrrgh! That's an error! Contact http://www.twitter.com/pitto")
        print str(e)

def start_explorer():
    '''
    Kills explorer.exe
    '''


    try:
        os.system('%systemroot%\sysnative\cmd.exe /c start /B explorer.exe')

    except Exception,e:
        pop_msgbox(e, title="Arrrgh! That's an error! Contact http://www.twitter.com/pitto")
        print str(e)

def delete_iconcache():
    '''
    Deletes IconCache.db into user folder
    '''


    try:
        os.system('DEL %userprofile%\AppData\Local\IconCache.db /a')

    except Exception,e:
        pop_msgbox(e, title="Arrrgh! That's an error! Contact http://www.twitter.com/pitto")
        print str(e)



def pop_msgbox(msgbox_message, msgbox_title):
    easygui.msgbox(msgbox_message, title=msgbox_title)

def main():
    '''
    Executes all the tasks in the correct order to achieve IconCache.db deletion
    '''


    kill_explorer()
    delete_iconcache()
    time.sleep(1)
    start_explorer()
    pop_msgbox("All done!\nEnjoy your beautiful icons and the new speedy folder creation :)\n\nIf you have any problems contact me:\n\nhttp://religioneinformatica.blogspot.com or http://www.twitter.com/pitto", "IconCache.db deletion completed")
    sys.exit()


if __name__ == "__main__":
    main()
