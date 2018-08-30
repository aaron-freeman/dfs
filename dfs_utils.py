from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import pandas as pd

import time


def dk_contest_select(user, password, contest):
    """
    A function that signs into DraftKings, and selects a 'Featured' contest.
    :param user:  DraftKings username
    :param password: DraftKings password (use getpass to supply this)
    :param contest: Name of the contest of interest
    :return:
    """
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.draftkings.com/")

    time.sleep(1)

    # DraftKings login
    r = driver.find_element_by_xpath('//*[@id="sign-in-link"]')
    r.click()

    username = driver.find_element_by_xpath('/html/body/div[9]/div/div/section/section/div[2]/div[3]/div/input')
    username.send_keys(user)

    pword = driver.find_element_by_xpath('/html/body/div[9]/div/div/section/section/div[2]/div[4]/div/input')
    pword.send_keys(password)

    login = driver.find_element_by_xpath('/html/body/div[9]/div/div/section/section/div[3]/button/span')
    login.click()

    time.sleep(5)

    # Select a contest
    contest = driver.find_element_by_link_text(contest)
    contest.click()
    time.sleep(1)

    # Click Draft Team button
    draft_team = driver.find_element_by_xpath('//*[@id="contest-details-enter"]')
    draft_team.click()

    return driver

