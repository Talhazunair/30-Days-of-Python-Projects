# Selenium Facebook Login Automation

## Introduction
This Python script utilizes the Selenium library to automate the login process on Facebook. By providing your Facebook email and password in the script, it navigates to the Facebook login page, enters the credentials, and clicks the login button.

## Prerequisites
- Python installed on your machine
- Selenium library installed (`pip install selenium`)
- GeckoDriver executable downloaded and added to the system path. You can download it [here](https://github.com/mozilla/geckodriver/releases).

## Usage
1. Clone this repository to your local machine.
   ```bash
   git clone https://github.com/your-username/selenium-facebook-login.git
   ```

2. Navigate to the project directory.
   ```bash
   cd selenium-facebook-login
   ```

3. Open the script (`facebook_login.py`) in a text editor of your choice.

4. Replace the placeholder text with your Facebook email and password.
   ```python
   email_input.send_keys("your_facebook_email")
   password_input.send_keys("your_facebook_password")
   ```

5. Save the changes to the script.

6. Run the script.
   ```bash
   python facebook_login.py
   ```

7. Watch the magic happen as the script automates the Facebook login process!

## Notes
- Make sure to keep your Facebook credentials secure and do not share them with others.
- The script uses the Firefox browser. Ensure that you have the GeckoDriver executable in your system path.

## Disclaimer
This script is for educational purposes only. Use it responsibly and in accordance with Facebook's terms of service.

Happy automating! 🤖
