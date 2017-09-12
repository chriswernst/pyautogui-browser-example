#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 20:54:02 2017

@author: ChrisErnst

This is an overview of how GUI automation works

The basis of this is taken from 'Automate the Boring Stuff with Python' by Sweigart

"""

# Verify dependencies are installed with:
    sudo pip3 install pyobjc-framework-Quartz, sudo pip3 install pyobjc-core
    # then
    sudo pip3 install pyobjc

# If the GUI automation gets out of hand, use:

    # command-shift-option-q 
    
# To pause the program:

import time
import pyautogui as pag
pag.PAUSE = 1 
# sets the pause to 1 sec between commands
pag.FAILSAFE = True  
#Enables the failsafe feature




# Moving the Mouse:
    
    # Upper left corner is 0,0
    
pag.size()  
# gets the display size

width, height = pag.size() 
# sets the width and height

pag.moveTo(100,100, duration=0.25)  
# moves the mouse to 100,100, and takes 1/4 sec

pag.moveTo(width, height)
# moves mouse instantaneously

pag.moveRel(0,-200)
# moves the mouse up relatively from where it is now

pag.position()
#outputs the current position of the mouse

pag.scroll(200)
# scrolls up

pag.screenshot()
#returns a screenshot in idle, might want to use command shift 3






# Clicking the Mouse

pag.click()
#clicks the left button of the mouse

pag.click(100,200, button='right')
# clicks the right button at x=100, y=200

pag.mouseDown()
pag.mouseUp()
# clicks up and down

pag.doubleClick()
# double clicks the left mouse





# Typing from the keyboard

pag.typewrite('message')
# types this out

pag.KEYBOARD_KEYS
# lists the keyboard keys

pag.keyDown('shift')
pag.press('4')
pag.keyUp('shift')
# Will type a dollar sign

pag.hotkey('a', 'shift', '4')
# types these and releases them in order

pag








