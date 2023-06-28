#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: evangelos
"""

#Import the required modules
import tkinter as tk
import random

#Create the main window
root = tk.Tk()

#Set the title of the window
root.title("Dice Roller")

#Set the size of the window
root.geometry("300x200")

#Create StringVars to hold the result of the dice rolls
dice_result1 = tk.StringVar()
dice_result2 = tk.StringVar()

#Create labels to display the result of the dice rolls
dice_label1 = tk.Label(root, textvariable=dice_result1, font=('times', 50, 'bold'))
dice_label2 = tk.Label(root, textvariable=dice_result2, font=('times', 50, 'bold'))

#Add the labels to the window
dice_label1.pack(side="left")
dice_label2.pack(side="right")

#Define a function to roll the dice
def roll_dice():
    # Generate random numbers between 1 and 6 for each dice
    result1 = random.randint(1, 6)
    result2 = random.randint(1, 6)
    
    # Update the dice_result variables with the results
    dice_result1.set(str(result1))
    dice_result2.set(str(result2))

#Create a button to roll the dice
roll_button = tk.Button(root, text="Roll", bg="red", fg="white", command=roll_dice)

#add the button to the window
roll_button.pack()

#Start the Tkinter event loop
root.mainloop()
