from bs4 import BeautifulSoup
import urllib.request
import requests
import random
import string
import time

win = int()
def link():
    global adress
    adress = str()
    for i in range(6):
        flip = random.randint(0,1)
        if flip == 0:
            temp = random.choice(string.ascii_letters)
            adress = adress+temp
        if flip == 1:
            temp = str(random.randint(1,9))
            adress = adress+temp
    print(adress)

def puller():
    tradress = (adress+".png")
    test = ("https://prnt.sc/")
    url = (test+adress)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    global win

    soup = BeautifulSoup(response.content, "html.parser")

    images = soup.find_all("img", attrs={"alt":"Lightshot screenshot"})

    number = 0
    for image in images:
        photo = str(image["src"])

    try:
        urllib.request.urlretrieve(photo, tradress)
        print("Success!")
        win = win+1
        
    except:
        print("image removed :(")

amount = int(input("How many links would you like to test: "))

for i in range(amount):
    print((i+1),"/",amount)
    link()
    puller()

print(win, "/",amount," successful")
time.sleep(4)
