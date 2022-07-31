# Install semua dependencies-nya
# dibutuhkan "requests" untuk diinstall (lihat python-requests.org)
import requests
from api import API_KEY_RM_BG


def edit_bg(img, bg_color):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img, 'rb')},
        data={'size': 'auto', 'bg_color': bg_color},
        headers={'X-Api-Key': API_KEY_RM_BG},
    )
    if response.status_code == requests.codes.ok:
        with open('output/edit_bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


# warna merah #FF0000, warna biru #0000FF, warna kuning #FFFF00
edit_bg(img='images/emily.png', bg_color='0000FF')
