# `Weather forecast` API testing homework by Billy Lam

## Setup

Please run the poetry command to install the package:

```shell
poetry install
```
## Input the information you want in method test_forecast()

test_get_forecast_data.py
```python
from get_data import find_weather_for, data_output
def test_forecast():
    #You can choose "today", "tmr", "the date after tomorrow"
    date = "tmr"
    # You can choose "wind", "temperature", "relative humidity" or "PSR"
    info = "relative humidity"
    weather_data = find_weather_for(date)
    result = data_output(weather_data, info)
    print(date + " : " + result) 
```
The method allows you to get the weather forecast of today, tomorrow and the day after tomorrow. 
And you can input the weather information you desire of that day. 
If you choose temperature or relative humidity, it will output in format min - max.

*If it is after 12pm, please do not call "today", the HK observatory will remove the data of that day. You can only access the next day's information
## Run the file
```shell
poetry run pytest test_get_forecast_data.py -vs
```
You will get the correct result
```output
API is connected successfully
tmr : The relative humidity is: 60 - 90%
```
However, if the API does not return successfully, you will get
```output
API is failed
```
And if the info is input wrong, you will get
```output
Please enter a correct value
```