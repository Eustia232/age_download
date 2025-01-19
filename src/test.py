import requests

url = "blob:https://43.240.156.118:8443/405545a7-b37d-4d0b-8425-896faa717e79"
response = requests.get(url)

with open('video.mp4', 'wb') as file:
    file.write(response.content)
