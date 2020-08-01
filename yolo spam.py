from selenium import webdriver
import tkinter as tk
from tkinter import filedialog, Text
import os
from os import system, name 
import time
import random


def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
            
for y in range(0, 183):         
    messages = ["your a fuckin loser", "go fuck yourself bud", "quit ur shit you fucking junkie", "mirrors can't talk. Lucky for you, they cant laugh either.", "if I had a face like yours, I'd sue my parents.", "If I said anything to offend you it was purely intentional.", "If I throw a stick, will you go away? fucking dog", "You started at the bottom and it's been downhill ever since", "your a fucking degenerate", "your retarded"]
    print("We're on time %d" % (y))
    url = 'URL TO USERS YOLO HERE'

    driver = webdriver.Chrome("PATH TO CHROME DRIVER HERE")

    driver.get(url)
    clear()
    driver.find_element_by_id('text').send_keys(random.choice(messages))
    driver.find_element_by_id('send-button').click()
    print("Sent successfully on time %d" % (y))
    time.sleep(2)
    driver.close()
