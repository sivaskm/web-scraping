import requests

URL = "https://realpython.com/beautiful-soup-web-scraper-python/"
page = requests.get(URL)

print(page.text)