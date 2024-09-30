import requests
import json

webhook_url = '' # Discord Webhook URL's
data = {
    'content': 'This is a test message!'
}

response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

if response.status_code == 204:
    print('Message successfully sent!')
else:
    print(f'Error sending message: {response.status_code}')
