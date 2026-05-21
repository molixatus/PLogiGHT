#jacob megablaster 240725 ptx PLogiGHT
#====================================================================
from playwright.sync_api import Playwright, sync_playwright
import random
import sys
from datetime import datetime
import time
from pystray import Icon as icon, Menu as menu, MenuItem as item
import PIL.Image
import multiprocessing
import os

roy = 'roy.png'
trayicon = 'mol.png'
_wait = 60
threadedran = False
state = True
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def on_clicked(icon, item):
    global state
    global pool
    global threadedran
    if str(item) == '1. Roy':
        print('::RAN::      One Shot Function: Running on main program thread \n')
        with sync_playwright() as playwright:
            runROY(playwright)
    elif str(item) == 'EXIT':
        print('::CALLED::   EXIT Function \n')
        time.sleep(0.5)
        if threadedran:
            pool.terminate()
        icon.stop()
    elif str(item) == '2. Run Script':
        print('::RUNNING::  Function Running in child process \n')
        threadedran = True
        state = not item.enabled
        pool = multiprocessing.Pool(processes=1)
        pool.apply_async(doinout, ())   
    elif str(item) == '3. Stop Script':
        print('::STOPPED::  Function Running in child process \n')
        state = not state
        pool.terminate()

def runROY(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #page.goto("file:///C:/Users/Jacob.SYNERGIEUK/Pictures/Screenshots/Screenshot%202025-04-04%20105945.png")
    cwd = os.getcwd()
    page.goto(f"file:///{cwd}/{roy}")
    time.sleep(1)

def runin(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://synergie_uk-dc/SynergieUK/default/user/login")
    page.get_by_label("E-mail").click()
    page.get_by_label("E-mail").fill("jacobcooke@synergie-cad.co.uk")
    page.get_by_label("E-mail").press("Tab")
    page.get_by_label("Password").fill("159753456")
    page.get_by_label("Password").press("Enter")
    page.get_by_role("button", name="Sign In").click(button="left")
    time.sleep(1)
    context.close()
    browser.close()

def runout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://synergie_uk-dc/SynergieUK/default/user/login")
    page.get_by_label("E-mail").click()
    page.get_by_label("E-mail").fill("jacobcooke@synergie-cad.co.uk")
    page.get_by_label("E-mail").press("Tab")
    page.get_by_label("Password").fill("159753456")
    page.get_by_label("Password").press("Enter")
    page.get_by_role("button", name="Sign Out").click(button="left")
    time.sleep(1)
    context.close()
    browser.close()

def doinout():
    while True:
        
        hour = int(datetime.now().strftime('%H'))   ##############  GET gettimes##############
        minute = int(datetime.now().strftime('%M'))
        hourin, minutein, hourout, minuteout = 8, 23, 16, 55    #hour = 8   #minute = 27

        if not ((hour == hourout and minute == minuteout) or (hour == hourin and minute == minutein)):
            time.sleep(_wait)
            continue
        randiff = random.randint(1, 3)
        time.sleep(_wait * randiff)
        with sync_playwright() as playwright:
            if hour == hourout and minute == minuteout:
                runout(playwright)
            elif hour == hourin and minute == minutein:
                runin(playwright)


def main():
    
    image = PIL.Image.open(trayicon)
    
    icon('test', image, menu=menu(
        item('1. Roy',on_clicked,),
        item('2. Run Script',on_clicked,enabled=lambda item: state),
        item('3. Stop Script',on_clicked,enabled=lambda item: not state),
        item('EXIT',on_clicked,)
        )).run()

if __name__ == "__main__":
    main()
    
    