import requests

bot_token = "7716430771:AAHqCZNoDACm3qlaue4G_hTJkyrxDRV9uxo"
chat_id = "6487259893"
message = "🔔 Test message from MEXC bot!"

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
payload = {"chat_id": chat_id, "text": message}

response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)
