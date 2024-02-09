import requests
from tabulate import tabulate

data = requests.get("https://www.nepsealpha.com/api/smx9841/investment_calander")
nepse_data = data.json()
result = [
    ['Company','Unit']
]
for ipo in nepse_data["ipo"]:
    data = [ipo['company_name'],ipo['units']]
    result.append(data)

table2 = tabulate(result)
params = {
    "chat_id": "@broadwaytest",
    "text": table2,
}
r = requests.post(
    "https://api.telegram.org/bot6954729845:AAGnWL0F_WaOuUqoergV2d9kjp0gFYVmzv8/sendMessage",
    params=params,
)
print(r.json())