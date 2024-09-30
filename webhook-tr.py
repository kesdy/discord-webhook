import requests
import json

webhook_url = '' # Discord Webhook URL's
data = {
    'content': 'Bu bir test mesajıdır!'
}

response = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

if response.status_code == 204:
    print('Mesaj başarıyla gönderildi!')
else:
    print(f'Mesaj gönderilirken hata alındı: {response.status_code}')


# readme.md'de geçiyor fakat Türk Geliştiricileri için daha fazla ayrıntılarla şuraya da yazayım. Bu proje yeni başlayanlar için kolay bir requests post gönderme örneği üzerinden yapılmış bir PYTHON kodudur.Modül olarak sadece "pip install requests" yazsanız yeterlidir.
