from dataclasses import dataclass
from utils import Utils


@dataclass
class WeatherInfo:
    forecastDate: str
    week: str
    forecastWind: str
    forecastWeather: str
    forecastMaxtemp: int
    forecastMintemp: int
    forecastMaxrh: int
    forecastMinrh: int
    PSR: str


def find_weather_for(date: str) -> WeatherInfo:
    forecast_date = ""
    utils = Utils()
    today = utils.get_today()
    today = int(today)
    data = utils.get_data()
    if date == "today":
        forecast_date = str(today)
    elif date == "tmr":
        forecast_date = str(today + 1)
    elif date == "the date after tmr":
        forecast_date = str(today + 2)
    else:
        print("date is wrong. please input <today>, <tmr> or <the date after tmr>")

    for forecast in data["weatherForecast"]:
        if forecast["forecastDate"] == forecast_date:
            weather_info = WeatherInfo(
                forecastDate=forecast["forecastDate"],
                week=forecast["week"],
                forecastWind=forecast["forecastWind"],
                forecastWeather=forecast["forecastWeather"],
                forecastMintemp=forecast["forecastMintemp"]["value"],
                forecastMaxtemp=forecast["forecastMaxtemp"]["value"],
                forecastMinrh=forecast["forecastMinrh"]["value"],
                forecastMaxrh=forecast["forecastMaxrh"]["value"],
                PSR=forecast["PSR"]
            )

    return weather_info


def data_output(data: WeatherInfo, desired):
    if desired == "wind":
        return data.forecastWind
    elif desired == "temperature":
        min_temp = str(data.forecastMintemp)
        max_temp = str(data.forecastMaxtemp)
        result = f"The temperature is: {min_temp} - {max_temp}"
        return result
    elif desired == "relative humidity":
        min_rh = str(data.forecastMinrh)
        max_rh = str(data.forecastMaxrh)
        result = f"The relative humidity is: {min_rh} - {max_rh}%"
        return result
    elif desired == "PSR":
        return data.PSR
    else:
        return "Please enter a correct value: <wind>, <temperature>, <relative humidity> or <PSR>"

