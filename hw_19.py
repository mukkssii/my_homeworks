import schedule


def morning_alarm():
    print('Wake up!!!!!!')


def good_night():
    print('Good night, and have a sweet dreams')


def alarm_and_good_night():
    schedule.every().monday.at('07:00').do(morning_alarm)
    schedule.every().tuesday.at('07:00').do(morning_alarm)
    schedule.every().wednesday.at('07:00').do(morning_alarm)
    schedule.every().thursday.at('07:00').do(morning_alarm)
    schedule.every().friday.at('07:00').do(morning_alarm)
    schedule.every().day.at('14:47').do(good_night)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    alarm_and_good_night()
