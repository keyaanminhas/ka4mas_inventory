import requests
import json
import base64
import random
from datetime import date
from datetime import datetime
import os
from time import sleep
import ssl
ssl._create_default_https_context = ssl._create_unverified_context




def main():
    with open('config2.txt', 'r') as f:
        x = f.readlines()
        user = x[1].strip()
        password = x[2].strip()
        category = x[3].strip()
        template = x[4].strip()
        url = x[0].strip()
    titles = os.listdir('ALL_TITLES/')

    with open('config.txt', 'r') as f:
        y = f.readlines()
    gap = y[4].strip()
    time1, time2 = gap.split('-')
    for title in titles:
        mins = random.randint(int(time1), int(time2))
        print("[!] UPLOAD AFTER: " + str(mins))
        #sleep(mins * 60)
        create(user, password, category, template, url, title[:-4])
    input("DONE")

    



def create(user, password, category, template, url_half, title):
    with open(f'ALL_TITLES/{title}.txt', 'r', encoding="utf8") as f:
        data = f.read()
    paras = []
    with open('config.txt', 'r') as f:
        x = f.readlines()
        snippet = x[3].strip()
    rem =data.splitlines()
    for para in rem:
        fullstops = para.count('.')
        exclaimation_marks = para.count('!')
        question_marks = para.count('?')
        if fullstops + exclaimation_marks + question_marks < 2 and len(para) > 1 and len(para) < 60:
            #data = data.replace(para, '<h4>' + para + '</h4>')
            paras.append(para)
    #data = data.replace('<h4>' + paras[-2] + '</h4>', snippet + '\n\n\n' + '<h4>' +'\n' + paras[-2] + '</h4>')
    #data = data.replace('\n', f'\n\n{snippet}\n\n', 1)
    #data = data + f'\n\n{snippet}'
    today = date.today()
    Time = datetime.now()
    Current_Time = Time.strftime("%H:%M:%S")
    d1 = today.strftime("%Y-%m-%d")
    url = f"{url_half}/wp-json/wp/v2"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    if template == 'None' or '<wordpress_template>':
        post = {
     'title'    : title,
     'content'  : data,
     'date'   : f'{d1}T{Current_Time}',
     'categories' :   category,
     'status'   : 'publish'
    }
    else:
        post = {
     'title'    : title,
     'content'  : data,
     'date'   : f'{d1}T{Current_Time}',
     'categories' :   category,
     'status'   : 'publish',
     'template' :   template
    }

    response = requests.post(url+ '/posts' , headers=header, json=post)
    print(response.text, title, "DONE")


main()