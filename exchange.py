import requests

exchange_data = requests.get("https://openexchangerates.org/api/latest.json?app_id=adc9d1bb77ee400ca2782ae70c69d152")
data = exchange_data.json()
result = ("1 " ,data['base'] ,"= " ,data['rates']['NPR']," NPR")
token = "bot6909218594:AAFooxPnhko3u2Y9w6mocDIYZC7oCiYPdO8"
params = (
    {
        "chat_id":"-1002088588600",
        "text": str(result)
    }
)
r = requests.post(
    f'https://api.telegram.org/{token}/sendMessage', params=params
)
r.json()