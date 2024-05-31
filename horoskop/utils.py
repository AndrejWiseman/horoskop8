import requests
from bs4 import BeautifulSoup


def get_horoscope(sign, type):
    url = f"https://horoskopius.com/{type}-horoskop/{sign}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Accept-Language": "sr-YU"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    horoscope_text = soup.select_one(selector=".article-details").getText().strip()

    return horoscope_text


def dnevni_horoskop(sign):
    return get_horoscope(sign, "dnevni")


def nedeljni_horoskop(sign):
    return get_horoscope(sign, "nedeljni")


def mesecni_horoskop(sign):
    return get_horoscope(sign, "mesecni")


def godisnji_horoskop(sign):
    return get_horoscope(sign, "godisnji")
