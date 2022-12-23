from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import random
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import undetected_chromedriver as uc
import ssl
import requests
from wolframalpha import *
from bs4 import BeautifulSoup 
import requests, string, random


app_id = '4KR66T-9RU9Q7T5EX'
cli = Client(app_id)


def scrape_and_clean():
    website = requests.get('https://www.goodreads.com/quotes/tag/unrequited-love')
    soup = BeautifulSoup(website.content, 'html.parser')
    my_classes = soup.find_all(class_ = 'quoteText')
    return random.choice(my_classes)







def sender(answer):
    for i in range(0, len(message)):
        location.send_keys(message[i])
        sleep(0.1)
        # sleep(0.2)





def help():
    x = '''               CHOOSE ANY ONE:
,quote
,anime
,joke
,poetry
,question
,unrequited
,help
:)'''
    return x





def joke():
    joke = requests.get('https://v2.jokeapi.dev/joke/Any?format=txt')
    return joke.text


def anime():
    anime = requests.get('https://animechan.vercel.app/api/random')
    fromm = json.loads(anime.text)["anime"]
    character = json.loads(anime.text)["character"]
    quote = json.loads(anime.text)["quote"]
    return (f"ANIME NAME :{fromm} \n '{quote}' ~ {character} ")


def poetry():
    done = False
    with open('writers.txt') as f:
        writers = f.read().splitlines()

    writer = random.choice(writers)

    r = requests.get(f'https://poetrydb.org/author/{writer}/title')

    data = r.json()
    while done != True:
        try:
            title = data[random.randint(0, len(data) - 1)]['title']

            response = requests.get(
                f'https://poetrydb.org/author,title/{writer};{title}')

            data = response.json()

            title = data[0]['title']
            author = data[0]['author']
            lines = data[0]['lines']
            x = ("\n".join(lines))
            return (title + 'by ' + author + '\n' + x)
            done = True
        except Exception as e:
            return (e)


def quote():

    response = requests.get(f'http://api.quotable.io/random')
    try:
        data = response.json()
        tags = data['tags']
        content = data['content']
        author = data['author']
        return (f'"{content}" ~{author}')
    except:
        return ("ERROR")


def question(message):
    print(message)
    try:
        junk, que = message.split(' ', 1)
        res = cli.query(que)
        text = ''

        for pod in res.pods:
            for sub in pod.subpods:
                text = text + sub.plaintext
        if text.strip() != '':
            return (text)
        else:
            return("Your question wasnt found")
    except:
        return ("Your question wasnt found")





def run(url):
    opt = uc.ChromeOptions()
    opt.add_argument(r"--user-data-dir=C:\Users\ka4ma\AppData\Local\Google\Chrome\User Data")
    opt.add_argument(r"--profile-directory=Profile 1")
    driver = uc.Chrome(options = opt)
    driver.get(url)


    GROUP = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div/div[2]')))
    sleep(1)
    GROUP.click()

    sleep(1)
    MESSAGE_LIST = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[4]/div/div[3]/div/div[2]/div[2]'))) 
    sleep(5)
    answer = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'))) 
    LAST_MESSAGE = ''
    while 1:

        MESSAGES = driver.find_elements(By.XPATH, ("//*[contains(text(),',')]"))
        message = MESSAGES[-3].text
        if message != LAST_MESSAGE and message.startswith(','):
            if message.find(',question') != -1:
                answer.send_keys(question(message))
                sleep(0.2)
                answer.send_keys(Keys.RETURN)
            elif message.find(',quote') != -1:
                answer.send_keys(quote())
                sleep(0.2)
                answer.send_keys(Keys.RETURN)
            elif message.find(',joke') != -1:
                answer.send_keys(joke())
                sleep(0.2)
                answer.send_keys(Keys.RETURN)
            elif message.find(',poetry') != -1:
                answer.send_keys(poetry())
                sleep(0.2)
                answer.send_keys(Keys.RETURN)
            elif message.find(',anime') != -1:
                answer.send_keys(anime())
                sleep(0.2)
                answer.send_keys(Keys.RETURN)
            elif message.find(',help') != -1:
                answer.send_keys(help())
                sleep(0.2)
                answer.send_keys(Keys.RETURN)
            elif message.find(',unrequited') != -1:
                answer.send_keys(str(scrape_and_clean().text))
                sleep(0.2)
                answer.send_keys(Keys.RETURN)

            LAST_MESSAGE= message











if __name__ == '__main__':
    url = 'https://web.whatsapp.com/'
    run(url)