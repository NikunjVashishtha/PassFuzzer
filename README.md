# PassFuzzer
PassFuzzer is a brute force tool that can be used to brute force most of the websites.
Based on Hatch [By: MetaChar]

## Commands
<br>
  -h, --help            show this help message and exit<br>
  -u USERNAME, --username = USERNAME Choose the username<br>
  --usernamesel=USERNAMESEL Choose the username selector<br>
  --passsel=PASSSEL     Choose the password selector<br>
  --loginsel=LOGINSEL   Choose the login button selector<br>
  --passlist=PASSLIST   Enter the password list directory<br>
  --website=WEBSITE     choose a website<br>
## Installation Instructions
```
git clone https://github.com/NikunjVashishtha/PassFuzzer
python main.py
```

## Requirements
```
pip install selenium
pip install requests
```
Browser and its driver are required

You can download it from the browser's official page.
For this fork, create a folder in your C drive called 'webdrivers' and place the executable file inside. If you want to use a different directory, simply change the CHROME_DVR_DIR variable inside the python file.

<br>
## How to use (text)
1). Find a website with a login page<br>
2). Inspect element to find the Selector of the username form<br>
3). Do the same for the password field<br>
4). The the login form <br>
5). When Asked put in the username to brute force<br>
6). Watch it go!