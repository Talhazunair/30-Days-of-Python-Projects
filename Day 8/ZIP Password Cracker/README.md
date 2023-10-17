# Zip Password Cracker

## Overview

This is a simple GUI-based Zip Password Cracker implemented in Python using the `tkinter` library. The program allows users to select a zip file and a wordlist file to attempt to crack the password of the zip file.

## Prerequisites

Make sure you have the following libraries installed:

- `tkinter`
- `pyzipper`
- `threading`
- `tqdm`

You can install the required libraries using the following command:

```bash
pip install tkinter pyzipper tqdm
```

## How to Run

Run the script using Python:

```bash
python your_script_name.py
```

## Features

- **Browse Button**: Allows the user to select a zip file.
- **Wordlist Button**: Enables the user to choose a wordlist file.
- **Start Button**: Initiates the password cracking process using a threaded approach.
- **Text Boxes**: Displays the selected file paths and the progress of password tests.
- **Labels**: Provides information about the status of the password cracking process.
- **Progress Bar**: Indicates the progress of the password testing.

## Usage

1. Click the "Browse" button to select a zip file.
2. Click the "Wordlist" button to select a wordlist file containing potential passwords.
3. Click the "Start" button to begin the password cracking process.
4. Monitor the progress in the text boxes and progress bar.
5. The result will be displayed in the labeled area.

## Important Note

- This program utilizes the `pyzipper` library for handling encrypted zip files.
- Ensure that you have the necessary permissions to access and modify the selected files.

## Author

[Talha Zunair]

Feel free to customize and enhance the code based on your needs. If you encounter any issues or have suggestions, please create an issue or pull request.

Happy cracking!
