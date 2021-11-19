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
    input_display = input('How many screens are open : ')
    input_time = input('COUNT DOWN SETUP HERO (min): ')
    hero_amount = input('HERO AMOUNT (number): ')
    # reset_position_time = input('RESET POSITION (min): ')

    input_display = int(input_display)
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

    for i in range(input_display):
        win = pygetwindow.getWindowsWithTitle('Bombcrypto')[i]
        win.resizeTo(640, 500)

    while True:
        print('countdown sec: ', count_down)
        count_down -= 1

        # set button
        wallet_buttons = list(button.wallet())
        ok_buttons = list(button.ok())
        new_map_buttons = list(button.new_map())
        close_hunt_buttons = list(button.close_hunt())
        hero_buttons = list(button.hero())

        for wallet_button in wallet_buttons:
            # check is connect wallet button
            if wallet_button is not None:
                print('click wallet button')
                login(wallet_button)
                print('finish login')
                count_timeout += 1
                count_timeout = time_out(count_timeout, 'wallet')

        for ok_button in ok_buttons:
            # check is ok button
            if ok_button is not None:
                util.move_click(ok_button)
                time.sleep(2)
                refresh_page()

        for new_map_button in new_map_buttons:
            print("new map")
            # check is new map button
            if new_map_button is not None:
                util.move_click(new_map_button)

        for close_hunt_button in close_hunt_buttons:
            if close_hunt_button is not None:
                if count_down <= 1:
                    util.move_click(close_hunt_button)
                    if close_hunt_button == close_hunt_buttons[-1]:
                        count_down = init_time
                        count_timeout = 0
                else:
                    time.sleep(0.1)

        if count_down > 1:
            for hero_button in hero_buttons:
                if hero_button is not None:
                    print('=== new round setup hero===')
                    start_process(hero_amount, hero_button)
        else:
            print("connect system failed")
            count_timeout += 1
            count_timeout = time_out(count_timeout)


def login(wallet_button):
    time.sleep(1.5)

    util.move_click(wallet_button)
    count_finding = 0
    while True:
        print('find metamask button')
        metamask_button = button.metamask()
        # check is metamask button
        if metamask_button is not None:
            print('click metamask button')
            util.move_click(metamask_button)
            count_finding = 0
            break
        elif count_finding >= 10:
            print('find metamask failed')
            time_out(count_finding, 'metamask')
            count_finding = 0
            break
        else:
            count_finding += 1

        time.sleep(2)

    while True:
        print('find sign button')
        sign_button = button.sign()
        # check is metamask button
        if sign_button is not None:
            print('click sign button')
            util.move_click(sign_button)
            break
        elif count_finding >= 10:
            print('find sign failed')
            time_out(count_finding, 'sign')
            break
        else:
            count_finding += 1

        time.sleep(2)


def start_process(hero_amount, hero_button):
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


def time_out(count_timeout, name='not_name'):
    if count_timeout >= 10:
        time_str = time.strftime("%Y%m%d-%H%M%S")
        time_file_name = name + '-' + time_str + '.png'
        pyautogui.screenshot(util.im_path_err(time_file_name))
        refresh_page()
        count_timeout = 0

    return count_timeout


def refresh_page():
    pyautogui.press('f5')
    time.sleep(5)


if __name__ == '__main__':
    main()
