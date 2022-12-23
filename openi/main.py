import os
from datetime import date
from github import Github
import requests
import random
from datetime import date
import io
import datetime
from datetime import timedelta

with open('config.txt', 'r') as f:

	x = f.readlines()
	z = [y.strip() for y in x if y.strip()!='']

github_token = z[1]
paracount = int(z[3])
code_snippet = z[5]
paranum = z[7]
waitbwposts = int(z[9])
repository = z[11]
linebreak = int(z[13])


print('GITHUB TOKEN: ', github_token)
print('PARAGRAPHS: ', paracount)
print('CODE SNIPPET: ', code_snippet)
print('CODE SNIPPET ADDED AFTER PARA: ', paranum)
print('TIME BETWEEN SCHEDULING: ', waitbwposts)
print("GITHUB REPOSITORY", repository)
print("PARAGRAPH BREAK AFTER", linebreak)


input("PRESS ENTER TO START.")
print('STARTED!')
url = "https://smodin.io/smodin-service/write"



def instance(content1, REPOSITORY, token, title):
	try:
		repo = g.get_user().get_repo(REPOSITORY)
		all_files = []
		contents = repo.get_contents("")
		while contents:
			file_content = contents.pop(0)
			if file_content.type == "dir":
				contents.extend(repo.get_contents(file_content.path))
			else:
				file = file_content
				all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
		content = content1
		git_prefix = '_posts/'

		git_file = git_prefix + title
		if git_file in all_files:
			contents = repo.get_contents(git_file)
			repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
			print(git_file + ' UPDATED')
		else:
			repo.create_file(git_file, "committing files", content, branch="main")
			print(git_file + ' CREATED')
	except:
		g = Github(token)
		repo = g.get_user().get_repo(REPOSITORY)
		all_files = []
		contents = repo.get_contents("")
		while contents:
			file_content = contents.pop(0)
			if file_content.type == "dir":
				contents.extend(repo.get_contents(file_content.path))
			else:
				file = file_content
				all_files.append(str(file).replace('ContentFile(path="','').replace('")',''))
		content = content1
		git_prefix = '_posts/'

		git_file = git_prefix + title
		if git_file in all_files:
			contents = repo.get_contents(git_file)
			repo.update_file(contents.path, "committing files", content, contents.sha, branch="main")
			print(git_file + ' UPDATED')
		else:
			repo.create_file(git_file, "committing files", content, branch="main")
			print(git_file + ' CREATED')



def article_gen(title, paracount, paranum, current_time, repository, github_token):	
	paracount = str(paracount)
	e = datetime.datetime.now()
	paranum = int(paranum)
	try:
		url = "https://smodin.io/smodin-service/write"
		cookies = {
			"_fbp": "fb.1.1660474605557.1252883365",
			"_gid": "GA1.2.1457450624.1660474606",
			"_tt_enable_cookie": "1",
			"_ttp": "54b13f5a-b637-4399-81b7-2a61f4d866f8",
			"_hjFirstSeen": "1",
			"_hjIncludedInSessionSample": "1",
			"_hjSession_3037897": "eyJpZCI6IjkxMmU3ZWVhLTQwMzUtNGE4OC04MDc3LWViOGM4M2IxY2VmMCIsImNyZWF0ZWQiOjE2NjA0NzQ2MDYwNjIsImluU2FtcGxlIjp0cnVlfQ==",
			"_hjIncludedInPageviewSample": "1",
			"_hjAbsoluteSessionInProgress": "0",
			"__gads": "ID=d97662bebc79a7c6-22dde49cbdd400c9:T=1660474608:RT=1660474608:S=ALNI_MZbSiOLC1nbehLuAdhLlzCl_w0CYQ",
			"__gpi": "UID=00000a82472ba6fe:T=1660474608:RT=1660474608:S=ALNI_MZr2Vg6XxniIW5Jwy23C3IDA-3uWQ",
			"_hjSessionUser_3037897": "eyJpZCI6IjhlMjI0ZTVlLWFiYmQtNTg5Ni1hOTU2LWIyYjJkNDUzNTY5ZCIsImNyZWF0ZWQiOjE2NjA0NzQ2MDYwNDcsImV4aXN0aW5nIjp0cnVlfQ==",
			"_gat_gtag_UA_119340507_5": "1",
			"_ga_0W23F1LBQH": "GS1.1.1660474606.1.1.1660475865.60",
			"_ga": "GA1.1.981250739.1660474606",
		}

		headers = {
			"authority": "smodin.io",
			"accept": "application/json, text/plain, */*",
			"accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
			"content-type": "application/json;charset=UTF-8",
			# Requests sorts cookies= alphabetically
			# 'cookie': '_fbp=fb.1.1660474605557.1252883365; _gid=GA1.2.1457450624.1660474606; _tt_enable_cookie=1; _ttp=54b13f5a-b637-4399-81b7-2a61f4d866f8; _hjFirstSeen=1; _hjIncludedInSessionSample=1; _hjSession_3037897=eyJpZCI6IjkxMmU3ZWVhLTQwMzUtNGE4OC04MDc3LWViOGM4M2IxY2VmMCIsImNyZWF0ZWQiOjE2NjA0NzQ2MDYwNjIsImluU2FtcGxlIjp0cnVlfQ==; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0; __gads=ID=d97662bebc79a7c6-22dde49cbdd400c9:T=1660474608:RT=1660474608:S=ALNI_MZbSiOLC1nbehLuAdhLlzCl_w0CYQ; __gpi=UID=00000a82472ba6fe:T=1660474608:RT=1660474608:S=ALNI_MZr2Vg6XxniIW5Jwy23C3IDA-3uWQ; _hjSessionUser_3037897=eyJpZCI6IjhlMjI0ZTVlLWFiYmQtNTg5Ni1hOTU2LWIyYjJkNDUzNTY5ZCIsImNyZWF0ZWQiOjE2NjA0NzQ2MDYwNDcsImV4aXN0aW5nIjp0cnVlfQ==; _gat_gtag_UA_119340507_5=1; _ga_0W23F1LBQH=GS1.1.1660474606.1.1.1660475865.60; _ga=GA1.1.981250739.1660474606',
			"origin": "https://smodin.io",
			"referer": "https://smodin.io/writer",
			"sec-ch-ua": '"Chromium";v="104", " Not A;Brand";v="99", "Microsoft Edge";v="104"',
			"sec-ch-ua-mobile": "?0",
			"sec-ch-ua-platform": '"Windows"',
			"sec-fetch-dest": "empty",
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin",
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
			"x-json-ip": f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}",
		}
		json_data = {
			"title": title,
			"language": "en",
			"writingReqType": "article",
			"paragraphCount": paracount,
			"outlineCount": 2,
			"essayType": "descriptive",
			"sectionCount": 2,
			"argumentCount": 2,
			"recaptcha": "03ANYolquqEgW5H6pz--TsXFIR5huom91fvpG2nCNTW0st8Eout_wo0jAcJMMBRLvt9q3de6QZOEFLTj8HRAwk7kvY87R96E7GDG3X4xCA4R0kW6g-iKnP7bMFB0_RwctqCEipCHRHhazOAsIeBTWASpZLpmrhj8HHC4JlBQOABa2vp-PpW07z0LusyfmXWN2ffQcPVsIL7MxivFh74WEwkEkGaL3pZR7HWpsgXV7WlpyxyqSbHSTjte6BIRpMHHYioytN2makzpXz90YWlaGY9aXf7oyQJk0lltNMf30A6_GFLulJUNJySEvSzBJj7VkBmuRRGaSFEy13nrqeeImdCvmo0OwmdAL3LYVNJJVi-fxzviUOriv41-b7AL385m8brGUKUE3rkXWxcsE-aUem1SxG4n4lwjYbLupYzR-cpwXY2xaAJ0PdmI7esRujz1bw1PRfd0z3-KPypg9SMjDT1T2wczNRKrixtZh-8hmNBH-tdyj-iGgNerTTX9Y5FXTbDv-clZIgcLJ6",
			"detectLang": True,
		}

		response = requests.post(
			"https://smodin.io/smodin-service/write",
			cookies=cookies,
			headers=headers,
			json=json_data,
		)

		data = response.json()
		data = data['outputs']
		paras = []
		content = ''
		data = list(data)

		for i in range(0, len(data) -1):
			proc = data[i]
			if proc['textType'] == 'body':
				if int(len(proc['value'].split('.'))) > int(linebreak):
					graph = proc['value']
					full_stop_count = 0
					for r in range(0,len(graph)-1):
						i = graph[r]
						if i == '.' or i == '?' or i == '!':
							full_stop_count +=1
							if full_stop_count % linebreak == 0:
								graph = graph[:r] + '.\n\n' + graph[r+1:]
								content += graph + '\n'
								paras.append(graph)
				else:
					content += proc['value'] + '\n\n'
					paras.append(proc['value'])


			elif proc['textType'] == 'headline':
				content += '\n## ' + proc['value'] + '\n\n'
		today = date.today()
		d1 = today.strftime("%Y-%m-%d")
		title = title.replace(' ', '-')
		defaults = f'''---
title: "{title.replace('-', ' ')}"
---
'''
		with io.open(f'READY/{d1}-{title}.md', 'w', encoding='utf8') as f:
			f.write(content)
		try:
			content = content.replace(paras[0], f'{paras[0]}\n\n{code_snippet}\n\n')
		except:
			pass
		try:
			content = content.replace(paras[paranum], f'{paras[paranum]}\n\n{code_snippet}\n\n')
		except:
			pass
		try:
			content = defaults + content + f'\n\n{code_snippet}'
		except:
			pass
		with open('words.txt', 'r') as b:
			lines = b.readlines()
		for line in lines:
			line = line.strip()
			content = content.replace(line.split('-')[0], line.split('-')[1]) 
		title1 = f'{d1}-{title}.md'
		instance(content, repository, github_token, title1)

		print(f'READY/{d1}-{title}.md')

	except Exception as e:
		print("DID NOT WORK FOR SOME REASON: \n" , e)



def run(current_time, waitbwposts):
	with open('titles.txt', 'r') as f:
		x = f.readlines()
		z = [y.strip() for y in x if y.strip() != '']

	for i in z:	
		article_gen(i, paracount, paranum, current_time, repository, github_token)
		current_time = current_time + timedelta(minutes=waitbwposts)


e = datetime.datetime.now()
run(e, waitbwposts)