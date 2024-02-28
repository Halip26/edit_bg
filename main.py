# Install all dependecies

import requests
from api import API_TOKEN_KEY
from datetime import datetime
import sys


# create bg_changer function
def bg_changer(img, bg_color):
    response = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        files={"image_file": open(img, "rb")},
        data={"size": "auto", "bg_color": bg_color},
        headers={"X-Api-Key": API_TOKEN_KEY},
    )
    if response.status_code == requests.codes.ok:
        with open(
            "output/hasil-%s.png" % datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), "wb"
        ) as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)


# image path `python.exe .\main.py .\gambar_aku.jpg`
path_image = sys.argv[1]

# user can input the hex color name
color_name = str(input("Enter the color name: "))

bg_changer(path_image, color_name)