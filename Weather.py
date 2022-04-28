import requests

appid = "5bee683e9445c32e34a22d2b605b4adc"
def get_weather(city_name, appid):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={appid}&units=metric'
        )
        data = r.json()

        city_name = data["name"]
        cur_weather = data["main"]["temp"]
        cur_humidity = data["main"]["humidity"]


        print(f'Погода в городе: {city_name}\nТемпература: {cur_weather}\nВлажность: {cur_humidity}')
    except Exception as ex:
        #print(ex)
        print("Неверное название города ")




def Weather():
    city_name = input("Введите город: ")
    get_weather(city_name, appid)


while True:
    if Weather() != 0:
        Weather()