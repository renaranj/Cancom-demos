import requests

bot_token = "your_bot_token"
chat_id = "your_chat_id"
message = "🔔 Test message from MEXC bot!"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {"chat_id": chat_id, "text": message}

response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)
