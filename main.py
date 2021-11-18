# from PIL.ImageOps import grayscale

import sys
import time
import pyautogui
import pygetwindow
# from PIL import Image

import button_controller as button
import util


def main():
    print('====START BOT BOMB====')

    input_time = input('COUNT DOWN SETUP HERO (min): ')
    hero_amount = input('HERO AMOUNT (number): ')
    # reset_position_time = input('RESET POSITION (min): ')

    input_time = int(input_time)
    hero_amount = int(hero_amount)
    # reset_position_time = int(reset_position_time)

    count_timeout = 0
    sec = 60
    count_down = input_time * sec
    init_time = input_time * sec

    # if reset_position_time > input_time:
    #     sys.exit('reset position time must not be more than count down')

    # reset_position_time = reset_position_time * sec
    # time_back = cal_time_click_back(reset_position_time, count_down)

    win = pygetwindow.getWindowsWithTitle('Bombcrypto')[0]
    win.resizeTo(640, 500)
    win.moveTo(0, 0)

    while True:
        print('countdown sec: ', count_down)
        count_down -= 1

        # check is connect wallet button
        wallet_button = button.wallet()
        if wallet_button is not None:
            util.move_click(wallet_button)

        # check is metamask button
        metamask_button = button.metamask()
        if metamask_button is not None:
            util.move_click(metamask_button)

        # check is sign button
        sign_button = button.sign()
        if sign_button is not None:
            util.move_click(sign_button)

        # check is ok button
        ok_button = button.ok()
        if ok_button is not None:
            util.move_click(ok_button)
            time.sleep(2)
            pyautogui.press('f5')

        # check is new map button
        new_map_button = button.new_map()
        if new_map_button is not None:
            util.move_click(new_map_button)

        # check is close hunt button
        close_hunt_button = button.close_hunt()
        if close_hunt_button is not None:
            if count_down <= 1:
                util.move_click(close_hunt_button)
                count_down = init_time
            else:
                time.sleep(0.5)
        elif count_down > 1:
            hero_button = button.hero()
            if hero_button is not None:
                print('=== new round ===')
                start_process(hero_amount)
        else:
            print("connect system failed")
            count_timeout += 1
            if count_timeout == 30:
                pyautogui.press('f5')
                count_timeout = 0
                time.sleep(5)


def start_process(hero_amount):
    # set and click hero button
    hero_button = button.hero()
    util.move_click(hero_button)

    hero_work(hero_amount)
    treasure_hunt()


def cal_time_click_back(input_time, countdown_time):
    return countdown_time - input_time


def hero_work(hero_amount):
    time.sleep(2)

    work_not_active_button = button.work_not_active()
    work_active_button = button.work_active()

    # go to work button and drag to height
    is_not_button_status = True
    while is_not_button_status:
        if work_not_active_button is not None:
            pyautogui.moveTo(work_not_active_button, duration=0.5)
            is_not_button_status = False
        elif work_active_button is not None:
            pyautogui.moveTo(work_active_button, duration=0.5)
            is_not_button_status = False
        else:
            print('find not work button')
            click_close_button()
            time.sleep(1)

    # set drag display
    time.sleep(1.5)
    pyautogui.drag(0, -300, duration=0.2)
    time.sleep(4)

    # loop click hero to work!
    # but work not active is None will break loop
    for hero_count in range(hero_amount):
        work_not_active = button.work_not_active()
        work_active = button.work_active()

        if work_not_active is not None:
            util.move_click(work_not_active)
            print('click hero work: ', hero_count + 1)
            time.sleep(1)
        elif work_active is not None:
            print("stop click hero work")
            break
        elif hero_count < 0:
            print('long loop hero page error')
            break
        else:
            print('not found work button')
            time.sleep(5)
            click_close_button()
            hero_count -= 1

    click_close_button()
    time.sleep(1.5)


def click_close_button():
    close_button = button.close()
    if close_button is not None:
        util.move_click(close_button)


def treasure_hunt():
    print('===start treasure hunt===')
    time.sleep(2)
    start_hunt = button.treasure_hunt()

    if start_hunt is not None:
        util.move_click(start_hunt)


if __name__ == '__main__':
    main()
