import os
import pyautogui
import subprocess
import time

person = input("The Person Whome You Wanna Send The Message : ")

msg = input("Message : ")

try:
    subprocess.Popen("C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2228.14.0_x64__cv1g1gvanyjgm\\app\\WhatsApp.exe")
    time.sleep(15)
    currentMouseX, currentMouseY = pyautogui.position()
    print(currentMouseX, currentMouseY)
    pyautogui.click(169,100)

    pyautogui.write(person, interval=0.25)
    time.sleep(.5)
    pyautogui.click(162,210)
    pyautogui.write(msg, interval=0.01)
    pyautogui.click(1328,681)
except:
    print("Error")
