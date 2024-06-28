from bs4 import BeautifulSoup
import requests

year = str(input("Please, enter year of top songs YYYY: "))
month = str(input("Please, enter month of top songs MM: "))
day = str(input("Please, enter day of top songs DD: "))

date = f"{year}-{month}-{day}"
url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=url).text
soup = BeautifulSoup(response, "html.parser")
song_names = []

songs = soup.select("li ul li h3")
for i in songs:
    i.getText()
    song_names.append(i.getText().strip())

print(song_names)
