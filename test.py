import requests

response = requests.get('https://emojipedia.org/taco/')

print(response.json())