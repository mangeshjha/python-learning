import requests
from tabulate import tabulate

data = requests.get("https://www.nepsealpha.com/api/smx9841/investment_calander")
nepse_data = data.json()
# nepse_data["ipo"]
# all_data = [["Roll Number","Student name","Marks"],
#             [1,"Sasha",34],
#             [2,"Richard",36],
#             [3,"Judy",20],
#             [4,"Lori",39],
#             [5,"Maggie",40]]
result = [
    ['Company','Unit']
]
for ipo in nepse_data["ipo"]:
    data = [ipo['company_name'],ipo['units']]
    result.append(data)
print(result)
print(result)
table1 = tabulate(result)
table2 = tabulate(result,headers='firstrow')
table2 = tabulate(result,headers='firstrow')
table2