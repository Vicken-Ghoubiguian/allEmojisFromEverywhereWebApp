import requests

response1 = requests.get('https://emojipedia.org/taco/')
response2 = requests.get('http://emojipedia.org/man-gesturing-no-light-skin-tone/')
response3 = requests.get('https://emojipedia.org/people/')

print(response3.text)