import requests
from pprint import pprint


url = "https://sites.google.com/view/nivel1-desafios/condicionales"
proxies = {"36.67.206.187":"8080"}

res = requests.get(url, proxies=proxies)
# print(res.text)
for k, v in res.headers.items():
    print(f"{k} --> {v:1s}")

