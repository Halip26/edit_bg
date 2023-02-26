# Install semua dependencies-nya
# dibutuhkan "requests" & "datetime" untuk diinstall (lihat python-requests.org)
import requests
from datetime import datetime
from api import API_TOKEN_KEY


def edit_bg(img, bg_color):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img, 'rb')},
        data={'size': 'auto', 'bg_color': bg_color},
        headers={'X-Api-Key': API_TOKEN_KEY},
    )
    if response.status_code == requests.codes.ok:
        with open('output/hasilnya-%s.png'%datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


# warna merah #FF0000, warna biru #0000FF, warna kuning #FFFF00
edit_bg(img='images/IMG_1114.jpg', bg_color='0000FF')
