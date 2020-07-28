import requests


url = 'http://web.juhe.cn:8080/environment/air/cityair'
para = {"city": "广州", "key": "c59b46478cbc1384016f1f57e6952a86"}
res = requests.get(url, params=para)
r = res.json()
print(r)
# r1 = res.text
# print(r1)
