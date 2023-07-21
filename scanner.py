import time
import sys
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from datetime import datetime
import requests
import json

HEB_WORDS = {"phone1": "ןופלט", "age": "ליג", "city": "ריע", "name": "םשׂ"}
DUMPER_FILEPATH = 'data.txt'

# Load default font.
eng_font = ImageFont.load_default()

# Support in hebrew font
heb_font = ImageFont.truetype('Noto.ttf', 9)

# initialize RPi with OLED
def init_oled_get_disp():
    # Raspberry Pi pin configuration:
    RST = None     # on the PiOLED this pin isnt used
    # Note the following are only used with SPI:
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0

    # 128x32 display with hardware I2C:
    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

    # Initialize library.
    disp.begin()

    # Clear display.
    disp.clear()
    disp.display()

    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    return disp

def display_initial_waiting_dog(disp):
    # image of my <3
    image = Image.open('tutin.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

    # Display image.
    disp.image(image)
    disp.display()

def display_chip_not_found(disp):
    # 2nd image of my <3
    image = Image.open('tutin-error.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')

    # Display image.
    disp.image(image)
    disp.display()

# details is a list of the following keys: name, phone1, phone2, birth_date, city
def display_dog_details(disp, details):
    start = 50
    top = 0
    # Create blank image for drawing.
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
    # censoring my own phone & city for the PoC
    details_text = details['age'] + " : " + HEB_WORDS['age'] + "      |    " +  details['name'] + " : " + HEB_WORDS['name'] + '\n'  \
    + "XXXX" + " : " + HEB_WORDS['city'] \
    + "  |  " + details['phone1'][0:2]+"X"*(len(details['phone1'])-2) + " : " + HEB_WORDS['phone1']
    
    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.multiline_text((0,0),details_text, spacing=5, font=heb_font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()

# Sends HTTP request to animal RFID national DB and returns details list
def animal_RFID_to_details(disp, animal_rfid):
    url = 'https://dogsearch.moag.gov.il/api/GetAnimalDetails'
    headers = {
        'authority': 'dogsearch.moag.gov.il',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en,he-IL;q=0.9,he;q=0.8,en-US;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://dogsearch.moag.gov.il',
        'referer': 'https://dogsearch.moag.gov.il/',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    print("TAG: " + animal_rfid)
    data = {
      "SearchParam": animal_rfid,
      "top": 10,
      "skip": 0
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), cookies=requests.utils.dict_from_cookiejar(requests.get(url).cookies))
    response_json = response.json()
    # display wrong chip screen when the RFID isn't found in DB
    if response_json['Count'] == 0:
        print("Couldn't find chip")
        display_chip_not_found(disp)
        return
    print("response:: " + str(response_json))
    phone1 =  response_json["AnimalDetails"][0]["Phone"]
    birth_date =  response_json["AnimalDetails"][0]["BrithDate"]

    # Calculate the age from birth date of format MM/YYYY - #quickmafs!
    date = datetime.strptime(birth_date, '%m/%Y')
    now = datetime.now()
    age = str(now.year - date.year - ((now.month, now.day) < (date.month, date.day)))

    city = response_json["AnimalDetails"][0]["City"]
    name = response_json["AnimalDetails"][0]["AnimalName"][::-1]

    details = {'phone1': phone1, 'age': age, 'city': city, 'name': name}
    print("details from CURL !  "+ str(details))

    # also write all the data to RPi so we can look at it later
    with open(DUMPER_FILEPATH, "a") as f:
        json.dump(response_json, f, ensure_ascii=False)
        f.write('\n')
    return details
    

def main():
    disp = init_oled_get_disp()
    while True:
        display_initial_waiting_dog(disp)
        RFID = input("Enter Animal RFID: ")
        details = animal_RFID_to_details(disp, RFID)
        if details:
            display_dog_details(disp,details) 
        time.sleep(5)
        
    
if __name__ == "__main__":
        main()
