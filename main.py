from PIL.ImageOps import grayscale

import os
import sys
import time

import pyautogui
import pygetwindow
from PIL import Image


def main():
    print('====START BOT BOMB====')
    Image.open(im_path("hero.png")).convert("RGB").save("hero.png")
    win = pygetwindow.getWindowsWithTitle('Bombcrypto')[0]
    win.resizeTo(640, 500)
    win.moveTo(0, 0)
    win.activate()

    input_time = input('COUNT DOWN SETUP HERO (min): ')
    hero_amount = input('HERO AMOUNT (number): ')
    reset_position_time = input('RESET POSITION (min): ')

    input_time = int(input_time)
    hero_amount = int(hero_amount)
    reset_position_time = int(reset_position_time)

    sec = 60
    count_down = input_time * sec
    init_time = input_time * sec

    if reset_position_time > input_time:
        sys.exit('reset position time must not be more than count down')

    reset_position_time = reset_position_time * sec
    time_back = cal_time_click_back(reset_position_time, count_down)
    # start_game()

    while True:
        print('countdown sec: ', count_down)
        count_down -= 1

        connect_wallet_button = set_connect_wallet_button()
        if connect_wallet_button is not None:
            start_game()

        if count_down > 1:
            close_hunt_button = pyautogui.locateOnScreen(
                im_path('back-main.png'), grayscale=True, confidence=.8)

            new_map()
            error_page()

            # start new round
            if close_hunt_button is None:
                hero_work(hero_amount)
                treasure_hunt()

            # back to main menu edit bug
            if count_down == time_back:
                close_treasure_hunt()
                treasure_hunt()
                time_back = cal_time_click_back(reset_position_time, count_down)

        if count_down <= 1:
            close_treasure_hunt()
            count_down = init_time

        time.sleep(1)


def im_path(filename):
    return os.path.join('images', filename)


def cal_time_click_back(input_time, countdown_time):
    return countdown_time - input_time


def set_connect_wallet_button():
    # Point(x=320, y=379)
    connect_wallet_button = pyautogui.locateOnScreen(
        im_path('connect-wallet.png'), grayscale=True, confidence=.8)

    return connect_wallet_button


def start_game():
    print('===connect wallet===')
    # Point(x=340, y=300)
    connect_wallet_button = set_connect_wallet_button()

    if connect_wallet_button is None:
        sys.exit("connect wallet button not found")

    pyautogui.moveTo(connect_wallet_button, duration=0.5)
    pyautogui.click(connect_wallet_button)

    time.sleep(2)

    print('===connect metamask===')
    metamask = pyautogui.locateOnScreen(
        im_path('metamask.png'), grayscale=True, confidence=.95)

    if metamask is None:
        sys.exit("metamask button not found")

    pyautogui.moveTo(metamask, duration=0.5)
    pyautogui.click(metamask)

    time.sleep(3)

    print('sing metamask')
    sing = pyautogui.locateOnScreen(
        im_path('sing.png'), grayscale=True, confidence=.95)

    # print(sing)
    if sing is None:
        sys.exit("sing button not found")

    pyautogui.moveTo(sing, duration=0.5)
    pyautogui.click(sing)

    # loop wait for loading
    while True:
        start_hunt = pyautogui.locateOnScreen(
            im_path('start-game.png'), grayscale=True, confidence=.95)

        if start_hunt is not None:
            break

        time.sleep(1)
        print("wait for loading")


def hero_work(hero_amount):
    time.sleep(2)
    print('====start hero to work====')

    # Point(x=528, y=410)
    hero_button = pyautogui.locateOnScreen(
        im_path('hero.png'), grayscale=True, confidence=.95)

    # print(hero_button)
    if hero_button is None:
        sys.exit("hero button not found")

    pyautogui.moveTo(hero_button, duration=0.5)
    pyautogui.click(hero_button)
    time.sleep(2)

    # Point(x=283, y=242) work button first line
    # Point(x=285, y=398) work button last line
    while True:
        work_button = pyautogui.locateOnScreen(
            im_path('work-non-active.png'), grayscale=True, confidence=.95)

        work_button_active = pyautogui.locateOnScreen(
            im_path('work-active.png'), grayscale=True, confidence=.95)

        if work_button is not None:
            pyautogui.moveTo(work_button, duration=0.5)
            pyautogui.drag(0, -500, duration=0.2)
            time.sleep(1)
            break

        elif work_button_active:
            pyautogui.moveTo(work_button_active, duration=0.5)
            pyautogui.drag(0, -500, duration=0.2)
            time.sleep(1)
            break

    work = None
    for work in pyautogui.locateAllOnScreen(im_path('work-non-active.png'), grayscale=True, confidence=.95):
        print('work not active')

    time.sleep(1)

    if work is not None:
        for clickWork in range(hero_amount + 1):
            pyautogui.click(work)
            print("click hero not active: ", clickWork)
            time.sleep(1)
            over_load = pyautogui.locateOnScreen(im_path('server-overload.png'), grayscale=True, confidence=.95)
            if over_load is not None:
                click_close_button()
                time.sleep(5)

    click_close_button()
    time.sleep(1.5)


def click_close_button():
    close_button_hero = set_close_button()

    if close_button_hero is None:
        sys.exit("close hero button not found")

    pyautogui.moveTo(close_button_hero, duration=0.5)
    pyautogui.click(close_button_hero)


def set_close_button():
    # Point(x=103, y=165)
    close_button_hero = pyautogui.locateOnScreen(
        im_path('close.png'), grayscale=True, confidence=.8)

    return close_button_hero


def treasure_hunt():
    print('===start treasure hunt===')
    time.sleep(2)
    start_hunt = pyautogui.locateOnScreen(
        im_path('start-game.png'), grayscale=True, confidence=.95)

    if start_hunt is None:
        sys.exit("treasure hunt button not found")

    pyautogui.moveTo(start_hunt, duration=0.5)
    pyautogui.click(start_hunt)


def close_treasure_hunt():
    print('===close treasure hunt===')
    close_hunt_button = pyautogui.locateOnScreen(
        im_path('back-main.png'), grayscale=True, confidence=.95)

    if close_hunt_button is None:
        sys.exit("back to main menu button not found")

    pyautogui.moveTo(close_hunt_button, duration=0.5)
    pyautogui.click(close_hunt_button)
    time.sleep(1.5)


def new_map():
    # Point(x=324, y=390)
    print('===check new map button===')
    new_map_button = pyautogui.locateOnScreen(
        im_path('new-map.png'), grayscale=True, confidence=.95)

    if new_map_button is not None:
        pyautogui.moveTo(new_map_button, duration=0.5)
        pyautogui.click(new_map_button)
        time.sleep(2)


def set_ok_button():
    ok_button = pyautogui.locateOnScreen(
        im_path('ok.png'), grayscale=True, confidence=.95)

    return ok_button


def error_page():
    print("===check unknown error===")
    unknown_error = pyautogui.locateOnScreen(
        im_path('unknown.png'), grayscale=True, confidence=.95)

    if unknown_error is not None:
        ok_button = set_ok_button()
        pyautogui.moveTo(ok_button, duration=0.5)
        pyautogui.click(ok_button)
        time.sleep(10)


if __name__ == '__main__':
    main()
