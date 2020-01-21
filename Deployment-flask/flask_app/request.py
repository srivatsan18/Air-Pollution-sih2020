import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'SO2':2, 'NO2':9, 'rpm':6 , 'spm':6})

print(r.json())
