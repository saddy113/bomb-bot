import os
import pyautogui


def im_path(filename):
    return os.path.join('images', filename)


def im_path_err(filename):
    return os.path.join('img_err', filename)


def move_click(button):
    pyautogui.moveTo(button, duration=0.5)
    pyautogui.click(button)