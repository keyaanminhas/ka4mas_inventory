import json


with open('article.txt', 'r') as f:
    x = f.read()

data = json.loads(x)
final = ''
all_chars = ' abcdefghijklmnopqrstuvwxyz,.:!?/()*1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
title = data['title']
paragraphs = data['paragraphs']
for para in paragraphs:
    x = para['text']
    text = "".join([y for y in x if y in all_chars])
    final = final + text +  '\n'

print(final)


