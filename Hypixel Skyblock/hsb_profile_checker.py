# -*- coding: utf-8 -*-
"""
Filename: hsb_profile_checker.py
Date created: Wed Nov 25 16:19:56 2020
@author: Julio Hong
Purpose: Search the selected name to find profile on sky.lea.moe
Maybe scrape important data in future
https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/#creating-the-script
Steps:
0. Copy the selected username
(Or link to Ctrl-C to read from the clipboard)
1. Set up a custom hotkey
2. Copy selected username into clipboard?
3. Pass username to sky.lea.moe
"""

from pynput import keyboard
import pyperclip
from selenium import webdriver
# For background (headless) Chromium window
from selenium.webdriver.chrome.options import Options

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          chrome_options=chrome_options
                         )
driver.get("https://www.google.com")
driver.get_screenshot_as_file("capture.png")
driver.close()

# The key combination to check
# Use 'S' for 'Search'
COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(char='s')},
    {keyboard.Key.shift, keyboard.KeyCode(char='S')}
]

# The currently active modifiers
current = set()

def execute():
    print ("Do Something")

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
#    if any([key in COMBO for COMBO in COMBINATIONS]) and not key in current:
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()
            
def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    



