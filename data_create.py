# encoding: utf-8

import pandas as pd

data = pd.read_csv('Data_Corona19_Seoul.csv')
info = pd.read_csv('Station_Info.csv')

# for i in range(len(info)):
#     for j in range(len(data)):
#         print(
#             data['Date'][j],
#             info['Station name(district)'][i],
#             data[info['Station name(district)'][i]][j],
#             info['Latitude'][i],
#             info['Longitude'][i]
#         )

Date = []
St_Name = []
St_Val = []
St_Lati = []
St_Long = []

for i in range(len(info)):
    for j in range(len(data)):
        Date.append(data['Date'][j])
        St_Name.append(info['Station name(district)'][i])
        St_Val.append(data[info['Station name(district)'][i]][j])
        St_Lati.append(info['Latitude'][i])
        St_Long.append(info['Longitude'][i])

Result = pd.DataFrame({
    '날짜': Date,
    '자치구': St_Name,
    '확진자': St_Val,
    '위도': St_Lati,
    '경도': St_Long
})

Result.to_csv('Result.csv')
