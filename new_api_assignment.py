import requests
from tabulate import tabulate

data = requests.get("https://www.apple.com/shop/trade-in")
# apple_devices = data.json()
result = [
    ['Your device' , 'Estimated trade-in value footnote']
]
    
for series in apple_devices["series"]:
    data = [series['Your device'],series['Estimated trade-in value footnote']]
    result.append(data)

table2 = tabulate(result)
params = {
    "chat_id": "@broadwaytest",
    "text": table2,
}
r = requests.post(
    "https://api.telegram.org/bot6954729845:AAGnWL0F_WaOuUqoergV2d9kjp0gFYVmzv8/sendMessage",
    params=params)