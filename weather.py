def WeatherPyOwn(place, country):

    import pyowm
    import os

    token_weather = os.environ.get('token_weather__')
    owm = pyowm.OWM(token_weather, language="ru")

    try:
        observation = owm.weather_at_place(place + ", " + country)
    except:
        return "Ошибка! Неизвестный город."

    w = observation.get_weather()

    d = w.get_reference_time(timeformat='date')
    date_ = d.strftime("%H:%M,%d/%m") + "\n"

    temp_ = "температура " + str(
        w.get_temperature(unit='celsius')['temp']) + "C" + "\n"  # 'temp', 'temp_max', 'temp_min'
    clouds_ = w.get_detailed_status() + "\n"
    wind_ = "ветер " + str(w.get_wind()['speed']) + "м/с" + "\n"
    # w.get_weather_icon_url()

    rain = w.get_rain()
    if rain == {}:
        rain_ = ""
    else:
        rain_ = "\nдождь " + str(rain)

    snow = w.get_snow()
    if snow == {}:
        snow_ = ""
    else:
        snow_ = "\nснег " + str(snow)

    return place.capitalize() + ", " + date_ + temp_ + clouds_ + wind_ + rain_ + snow_
