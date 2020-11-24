#!/usr/bin/python3

from utility import *

class presence_marker():

    def __init__(self, login_str: str, passwd: str):
        self.login_m = login_str
        self.pwd_m = passwd
        self.cookies_m = None
        self.school_first_m = self.pair_timing(9, 00, 10, 35)
        self.school_second_m = self.pair_timing(10, 45, 12, 20)
        self.school_third_m = self.pair_timing(13, 00, 14, 35)
        self.school_fourth_m = self.pair_timing(14, 45, 16, 20)
        self.school_fifth_m = self.pair_timing(16, 30, 18, 5)
        self.start_lession()

    def pair_timing(self, h_start: int, min_start: int, h_stop: int, min_stop: int) -> list:
        file_log_info("Setting time for lessons")
        start_pair = time(h_start, min_start)
        end_pair = time(h_stop, min_stop)

        pair_timelist = list()
        while start_pair != end_pair:
            pair_timelist.append(str(start_pair))
            start_pair = datetime.combine(date.today(), start_pair) + timedelta(minutes=1)
            start_pair = start_pair.time()
        return pair_timelist

    def login_to_lk(self):
        file_log_info("Trying to log in")
        response = requests.get(url= TARGET_URL)
        self.cookies_m = response.cookies

        if self.cookies_m == None:
            file_log_error("Unable to get cookies")
            exit(COOKIE_ERROR)
        response = requests.post(url=AUTH_URL,
                                 data={'users': self.login_m, 'parole': self.pwd_m},
                                 cookies=self.cookies_m)
        if '0' in response.text:
            file_log_error("Wrong respose")
            exit(RESPONSE_ERROR)
        file_log_info("Access granted")
        

    def start_lession(self):
        while True:
            now = datetime.now()
            if now.strftime('%H:%M:00') in self.school_first_m:
                self.set_presence(self.school_first_m)
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_second_m:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_second_m:
                self.set_presence(self.school_second_m)
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_third_m:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_third_m:
                self.set_presence(self.school_third_m)
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_fourth_m:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_fourth_m:
                self.set_presence(self.school_fourth_m)
                while True:
                    now = datetime.now()
                    if now.strftime('%H:%M:00') in self.school_fifth_m:
                        break
                    else:
                        wait.sleep(60)

            if now.strftime('%H:%M:00') in self.school_fifth_m:
                self.set_presence(self.school_fifth_m)
                break

    def set_presence(self, time_of_lession :list):
        file_log_info("Trying to set presence")
        self.login_to_lk()
        try_it = 0

        while try_it < NUM_OF_TRIES and datetime.now().strftime('%H:%M:00') != time_of_lession[-1]:
            response = requests.get(url=SCHEDULE_URL,
                                    cookies=self.cookies_m)
            week_number = re.search('Полное расписание занятий на неделю №(\d*?) ', str(response.text)).group(1)
            try:
                id_of_start_lessiion = re.search(BUTTON_ID_STR, str(response.text)).group(1)
            except AttributeError:
                try_it+=1
                wait.sleep(600)
            else:
                response = requests.post(url=SCHEDULE_URL,
                                         data={'open': '1', 'rasp': str(id_of_start_lessiion), 'week': str(week_number)},
                                         cookies=self.cookies_m)
                file_log_info('Presence successfully set')
                break

if __name__ == "__main__":
    if len(sys.argv) < 3:
        con_log_error("Wrong usage! Try {} <login> <password>".format(sys.argv[0]))
        exit(BAD_USAGE)
    if len(sys.argv) == 4 and sys.argv[3] == "-d":
        with daemon.DaemonContext():
            file_log_info("Start as a daemon")
            presence_marker(sys.argv[1], sys.argv[2])
            file_log_info("Goodbye from daemon")
            exit(SUCCESS)

    con_log_info("Start as an application")
    presence_marker(sys.argv[1], sys.argv[2])
    con_log_info("Goodbye from application")
    exit(SUCCESS)


    

