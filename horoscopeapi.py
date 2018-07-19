import requests
from datetime import datetime
import json


# Function that takes month and a day and calcuates Zodiac sign
def zodiac_sign(month, day):
    sign = 'N/A'

    if month == 12:
        sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 1:
        sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 2:
        sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 3:
        sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 4:
        sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 5:
        sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 6:
        sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 7:
        sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 8:
        sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 9:
        sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 10:
        sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 11:
        sign = 'Scorpio' if (day < 22) else 'sagittarius'
    print("Your Astrological sign is :", sign)
    return sign


# call rest API to get horoscope for a given zodiac sign
def get_horoscope(sign):
    params = (
        ('sign', sign),
        ('day', 'today'),
    )

    # aztro provide free API to get horoscope for a sign -
    # API takes two param 1.sign (example values cancer, leo etc)  2. day possible values today, tomorrow etc
    response = requests.post('https://aztro.herokuapp.com/', params=params)

    print
    response.url
    print
    response.status_code
    print
    response.headers["content-type"]
    json_data = response.json()
    # json is raw data which contains all the data from the api response
    return json_data
