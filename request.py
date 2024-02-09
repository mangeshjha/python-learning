import requests
from tabulate import tabulate
from datetime import datetime

data = requests.get( "https://www.nepsealpha.com/api/smx9841/investment_calander")
nepse_data = data.json ()
result =[
            ['company_name','units']
        ]
print(datetime.now())
for ipo in nepse_data['ipo']:
        data = [ipo['symbol'],ipo['units']]
        result.append(data)

table1 = tabulate(result)
table2 = tabulate(result)

print(table1)



for ipo in nepse_data['ipo']:
    print(ipo['company_name']   , ipo['id']     ,ipo['symbol'])

