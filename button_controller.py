import pyautogui

import util


def wallet():
    connect_wallet_button = pyautogui.locateAllOnScreen(
        util.im_path('connect-wallet.png'), grayscale=True, confidence=.95)
    return connect_wallet_button


def sign():
    sign_button = pyautogui.locateOnScreen(
        util.im_path('sign.png'), grayscale=True, confidence=.95)
    return sign_button


def ok():
    ok_button = pyautogui.locateAllOnScreen(
        util.im_path('ok.png'), grayscale=True, confidence=.95)
    return ok_button


def new_map():
    new_map_button = pyautogui.locateAllOnScreen(
        util.im_path('new-map.png'), grayscale=True, confidence=.95)
    return new_map_button


def close_hunt():
    close_hunt_button = pyautogui.locateAllOnScreen(
        util.im_path('back-main.png'), grayscale=True, confidence=.95)
    return close_hunt_button


def hero():
    hero_button = pyautogui.locateAllOnScreen(
        util.im_path('hero.png'), grayscale=True, confidence=.95)
    return hero_button


def work_not_active():
    work_not_active_button = pyautogui.locateOnScreen(
        util.im_path('work-non-active.png'), grayscale=True, confidence=.95)
    return work_not_active_button


def work_active():
    work_active_button = pyautogui.locateOnScreen(
        util.im_path('work-active.png'), grayscale=True, confidence=.95)
    return work_active_button


def close():
    close_button = pyautogui.locateOnScreen(
        util.im_path('close.png'), grayscale=True, confidence=.95)
    return close_button


def treasure_hunt():
    treasure_hunt_button = pyautogui.locateOnScreen(
        util.im_path('start-game.png'), grayscale=True, confidence=.95)
    return treasure_hunt_button


def loading_bar():
    load_bar = pyautogui.locateAllOnScreen(
        util.im_path('loading-bar.png'), grayscale=True, confidence=.95)
    return load_bar
