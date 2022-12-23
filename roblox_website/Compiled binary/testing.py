
with open(f'ALL_TITLES/Warrior Cats Ultimate Edition.txt', 'r') as f:
    data = f.read()
data =data.splitlines()
for para in data:
    fullstops = para.count('.')
    exclaimation_marks = para.count('!')
    question_marks = para.count('!')
    if fullstops + exclaimation_marks + question_marks < 2 and len(para) > 1:
        print(para)