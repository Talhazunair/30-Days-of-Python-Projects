# Keylogger

A simple Python keylogger script that records keypresses and sends periodic email reports.

## Prerequisites

Make sure you have the following installed before running the script:

- Python 3.x
- `pynput` library: You can install it using `pip install pynput`

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/keylogger.git
   ```

2. Navigate to the project directory:

   ```bash
   cd keylogger
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Open the `keylogger.py` file and replace the placeholder values with your Gmail ID and password:

   ```python
   Keylogger = Keylogger(30, "Your Gmail ID", "Your Password")
   ```

5. Save the changes.

6. Run the script:

   ```bash
   python keylogger.py
   ```

**Note**: Make sure to use this script responsibly and only on systems where you have the explicit consent of the user.

## Disclaimer

This script is for educational purposes only. The misuse of this script to access unauthorized systems is strictly prohibited.

## Features

- Records keypresses.
- Sends periodic email reports with system information.
- Automatically captures a screenshot when the keylogger starts.

## Contributing

Feel free to contribute to the development of this script by opening issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
