import os
import requests

TOKEN = os.environ['TOKEN']
CHAT_ID = os.environ['CHAT_ID']

response = requests.get("https://zenquotes.io/api/random")
data = response.json()[0]
quote = f"\"{data['q']}\" — {data['a']}"

requests.get(
    f"https://api.telegram.org/bot{TOKEN}/sendMessage",
    params={"chat_id": CHAT_ID, "text": quote}
)
