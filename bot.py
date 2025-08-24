import requests
import os

TOKEN = os.getenv("8359549328:AAEOIyIPuwl3eE_qhHZR_qWjC5tmKEEtcZs")
CHAT_ID = os.getenv("@faratechinc")

def get_quote():
    try:
        r = requests.get("https://zenquotes.io/api/random")
        data = r.json()
        return f"{data[0]['q']} — {data[0]['a']}"
    except Exception:
        return "Keep pushing forward 💪"

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    quote = get_quote()
    send_message(quote)
    print("Sent:", quote)

