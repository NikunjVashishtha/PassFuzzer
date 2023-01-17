# PassFuzzer
PassFuzzer is a brute force tool that can be used to brute force most of the websites.<br>
Based on Hatch [By: MetaChar]

## Commands

```
-h, --help            show this help message and exit<br>
-u, --username        Choose the username<br>
--usernamese          Choose the username selector<br>
--passsel             Choose the password selector<br>
--loginsel            Choose the login button selector<br>
--passlist            Enter the password list directory<br>
--website             Choose a website<br>
```

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
<b>⚠️<u> Important: Browser and its driver are required</u></b>

You can download it from the browser's official page.
For this fork, create a folder in your C drive called 'webdrivers' and place the executable file inside. If you want to use a different directory, simply change the CHROME_DVR_DIR variable inside the python file.

## How to use it?
1) Find the website URL with the login page.<br>
2) Inspect element to find the Selector of the username, password field and login button.<br>
3) Put in the username to brute force.<br>
4) Add file of list of passwords
5) Watch the action
