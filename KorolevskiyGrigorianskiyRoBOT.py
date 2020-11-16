from datetime import date, datetime, time, timedelta
import time as wait
from tkinter import *
import requests


class fck_bobch():

    def __init__(self):
        self.login = str('')
        self.pwd = str('')
        self.cookies = None
        self.school_first = self.first_pair_timing()
        self.school_second = self.second_pair_timing()
        self.school_third = self.third_pair_timing()
        self.school_fourth = self.fourth_pair_timing()
        self.school_fifth = self.fifth_pair_timing()
        self.start_lession()

    def first_pair_timing(self):
        start_pair = time(9, 00)
        end_pair = time(10, 35)
        pair_timelist = []
        while start_pair != end_pair:
            pair_timelist.append(str(start_pair))
            start_pair = datetime.combine(date.today(), start_pair) + timedelta(minutes=1)
            start_pair = start_pair.time()
        return pair_timelist

    def second_pair_timing(self):
        start_pair = time(10, 45)
        end_pair = time(12, 20)
        pair_timelist = []
        while start_pair != end_pair:
            pair_timelist.append(str(start_pair))
            start_pair = datetime.combine(date.today(), start_pair) + timedelta(minutes=1)
            start_pair = start_pair.time()
        return pair_timelist

    def third_pair_timing(self):
        start_pair = time(13, 00)
        end_pair = time(14, 35)
        pair_timelist = []
        while start_pair != end_pair:
            pair_timelist.append(str(start_pair))
            start_pair = datetime.combine(date.today(), start_pair) + timedelta(minutes=1)
            start_pair = start_pair.time()
        return pair_timelist

    def fourth_pair_timing(self):
        start_pair = time(14, 45)
        end_pair = time(16, 20)
        pair_timelist = []
        while start_pair != end_pair:
            pair_timelist.append(str(start_pair))
            start_pair = datetime.combine(date.today(), start_pair) + timedelta(minutes=1)
            start_pair = start_pair.time()
        return pair_timelist

    def fifth_pair_timing(self):
        start_pair = time(16, 30)
        end_pair = time(18, 5)
        pair_timelist = []
        while start_pair != end_pair:
            pair_timelist.append(str(start_pair))
            start_pair = datetime.combine(date.today(), start_pair) + timedelta(minutes=1)
            start_pair = start_pair.time()
        return pair_timelist

    def login_to_lk(self):
        response = requests.get(url='https://lk.sut.ru/cabinet/')
        self.cookies = response.cookies
        response = requests.post(url='https://lk.sut.ru/cabinet/lib/autentificationok.php',
                                 data={'users': self.login, 'parole': self.pwd},
                                 cookies=self.cookies)
        if '0' in response.text:
            raise Exception('Неверный логин или пароль! Проверьте введенные данные!')

    def start_lession(self):
        while True:
            now = datetime.now()
            if now.strftime('%H:%M:00') in self.school_first:
                self.on_tha_hood(self.school_second[0])
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_second:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_second:
                self.on_tha_hood()
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_third:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_third:
                self.on_tha_hood()
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_fourth:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_fourth:
                self.on_tha_hood()
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_fifth:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_fifth:
                self.on_tha_hood()
                break

    def on_tha_hood(self):
        self.login_to_lk()
        iterator = 0
        while iterator < 10:
            response = requests.get(url='https://lk.sut.ru/cabinet//project/cabinet/forms/raspisanie_bak.php',
                                    cookies=self.cookies)
            week_number = re.search('Полное расписание занятий на неделю №(\d*?) ', str(response.text)).group(1)
            try:
                id_of_start_lessiion = re.search('<span id=\"knop(\d*?)\">', str(response.text)).group(1)
            except AttributeError:
                iterator = iterator + 1
                wait.sleep(600)
            else:
                response = requests.post(url='https://lk.sut.ru/cabinet//project/cabinet/forms/raspisanie_bak.php',
                                         data={'open': '1', 'rasp': str(id_of_start_lessiion), 'week': str(week_number)},
                                         cookies=self.cookies)
                print('Я отметился! Ееее, рок!')
                break

start_fck = fck_bobch()
