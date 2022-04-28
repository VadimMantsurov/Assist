from datetime import datetime
#from playsound import playsound

def validate_time(time_alarm):
    if len(time_alarm) != 8:
        return "Неверный формат, попробуйте снова"
    else:
        if int(time_alarm[0: 2]) > 23:
            return "Неверный формат часов"
        elif int(time_alarm[3: 5]) > 59:
            return "Неверный формат минут"
        elif int(time_alarm[6: 8]) > 59:
            return "Неверный формат секунд"
        else:
            return "хорошо"


while True:
    time_alarm = input("Ввести время будильника в формате 'ЧЧ:ММ:СС' \n Время будильника: ")

    validate = validate_time(time_alarm)
    if validate != "хорошо":
        print(validate)
    else:
        print("Будильник установлен на время:", time_alarm)
        break

alarm_hour = int(time_alarm[0:2])
alarm_min = int(time_alarm[3:5])
alarm_sec = int(time_alarm[6:8])

while True:
    now = datetime.now()
    '''Получение текущей даты'''

    current_hour = now.hour
    '''Получение текущего часа'''
    current_min = now.minute
    '''Получение текущей минуты'''
    current_sec = now.second
    '''Получение текущей секунды'''

    if alarm_hour == current_hour: '''Проверка введенных данных, с текущем временем'''
    if alarm_min == current_min:
        if alarm_sec == current_sec:
            print("Подъем!")
            #playsound('C:/PycharmProjects/pythonProject8/1.mp3')
            #''' Здесь вводите свой адрес,где у вас имеется ваша запись'''
            break
