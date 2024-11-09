import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

load_dotenv()
api_key = os.getenv("OPEN_API_KEY")
client = OpenAI()



url = 'https://www.webmd.com/first-aid/ss/slideshow-when-call-911'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

main = soup.find('div')

