# PassFuzzer

PassFuzzer is a brute-force tool for testing login forms on websites using Selenium and password lists.

## Command Line Arguments

```
-h, --help            Show this help message and exit
-l, --username        Username to brute-force
-u, --usernamesel     Username input field selector (name attribute)
-p, --passsel         Password input field selector (name attribute)
-b, --loginsel        Login button selector (name attribute)
-P, --passlist        Path to password list file
-w, --website         Target website URL
-d, --driver          Path to browser WebDriver executable
-B, --browser         Browser to use (edge/chrome/firefox)
```

## Installation

```sh
git clone https://github.com/NikunjVashishtha/PassFuzzer
cd PassFuzzer-main
pip install selenium requests
```

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [Requests](https://pypi.org/project/requests/)
- A supported browser (Edge, Chrome, Firefox, etc.) and its matching WebDriver

## Usage

1. Find the login page URL of the target website.
2. Inspect the login form to get the `name` attributes for the username, password, and login button fields.
3. Prepare a username and a password list file.
4. Download the appropriate WebDriver for your browser and note its path.
5. Run PassFuzzer with the required arguments, for example:

   ```sh
   python main.py -l myuser -u username_field -p password_field -b login_button -P passwords.txt -w https://example.com/login -d /path/to/webdriver -B chrome
   ```

   Or, run without arguments and follow the interactive prompts:

   ```sh
   python main.py
   ```

## Notes

- This tool is for educational and authorized testing purposes only.
- Make sure your WebDriver version matches your browser version.
- Works on Linux, macOS, and Windows (with correct driver path).

---
**Author:** Sparky99
