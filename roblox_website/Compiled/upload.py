import undetected_chromedriver._compat as uc
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
import re
from datetime import date
from github import Github


def instance(title,g):
    repo = g.get_user().get_repo('robloxpaste.github.io')
    all_files = []
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            file = file_content
            all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
    with open(f'UPLOADABLE/{title}', 'r') as file:
        content = file.read()
    git_prefix = '_posts/'

    git_file = git_prefix + title
    if git_file in all_files:
        contents = repo.get_contents(git_file)
        repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
        print(git_file + ' UPDATED')
    else:
        repo.create_file(git_file, "committing files", content, branch="main")
        print(git_file + ' CREATED')

    




def sender(message, location):
    for i in range(0,len(message)):
        location.send_keys(message[i])
        sleep(0.05)
        # sleep(0.2)


def uploader():
    g = Github("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")



    files = os.listdir('UPLOADABLE/')

    for i in files:
        instance(i,g)
    input()




uploader()