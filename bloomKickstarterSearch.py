#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:35:30 2017

The following is a very simple example of how the pyautogui library works and is intended for use Mac OSX and Chrome
(due to using featuring such as spotlight)

For a full list of keyboard strings pyautogui will accept, use pyautogui.KEYBOARD_KEYS

For documentation, visit: http://pyautogui.readthedocs.io/

@author: ChrisErnst
"""

import time
import pyautogui as pag
pag.PAUSE = 1 
# sets the pause to 1 sec between commands
pag.FAILSAFE = True  
#Enables the failsafe feature



pag.hotkey('command', 'space')
# Opens OSX Spotlight

pag.typewrite('chrome')
# Types Chrome
time.sleep(1)

pag.press('enter')
# selects chrome
time.sleep(1)

for i in range(1):
    
    pag.hotkey('command', 't')
    
    pag.typewrite('kickstarter.com')
    
    pag.press('enter')
    time.sleep(4)
    
    pag.click(1223,151)
    time.sleep(1)
    
    pag.typewrite('Bloom Air Quality')
    
    pag.moveTo(345,294, duration=0.25)
    
    pag.click()
    time.sleep(6)
    
    pag.hotkey('command', 'w')
    time.sleep(1)


