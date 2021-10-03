# ~ # ~ # TrolledTooHard#1383 # ~ # ~ #

import os, requests, googletrans, json

# prerequisites # 

from colorama import *
from googletrans import Translator
translator = Translator()

init()

def tokenget(file):
	with open(file, 'r') as f:
		return(json.load(f))

configfile = tokenget('config.json')

token = configfile.get("token","")

headers = {
	"authorization" : token
	}

token_info = requests.get('https://discord.com/api/v9/users/@me', headers=headers)

token_stats = token_info.json()

username = token_stats['username']

discrim = token_stats['discriminator']

userid = token_stats['id']

userinputstyle = f'{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}]{Fore.WHITE}'

# Basic UI Design #

def asciibanner():
	print(f'''
{Fore.GREEN}▄▄▄▄▄▄▄▄        ▄▄▌  ▄▄▌  ▄▄▄ .·▄▄▄▄  ▄▄▄▄▄             ▄ .▄ ▄▄▄· ▄▄▄  ·▄▄▄▄  
{Fore.WHITE}•██  ▀▄ █·▪     ██•  ██•  ▀▄.▀·██▪ ██ •██  ▪     ▪     ██▪▐█▐█ ▀█ ▀▄ █·██▪ ██ 
{Fore.GREEN} ▐█.▪▐▀▀▄  ▄█▀▄ ██▪  ██▪  ▐▀▀▪▄▐█· ▐█▌ ▐█.▪ ▄█▀▄  ▄█▀▄ ██▀▐█▄█▀▀█ ▐▀▀▄ ▐█· ▐█▌
{Fore.WHITE} ▐█▌·▐█•█▌▐█▌.▐▌▐█▌▐▌▐█▌▐▌▐█▄▄▌██. ██  ▐█▌·▐█▌.▐▌▐█▌.▐▌██▌▐▀▐█ ▪▐▌▐█•█▌██. ██ 
{Fore.GREEN} ▀▀▀ .▀  ▀ ▀█▄▀▪.▀▀▀ .▀▀▀  ▀▀▀ ▀▀▀▀▀•  ▀▀▀  ▀█▄▀▪ ▀█▄▀▪▀▀▀ · ▀  ▀ .▀  ▀▀▀▀▀▀•''')
	print()
	print(f'{Fore.WHITE}Developed By: TrolledTooHard#1383')
	print()
	print(f'{Fore.GREEN}Signed In As: {username}#{discrim} [{userid}]')
	print(f'{Fore.WHITE}')
	print("Use: '~ChangeLang' to change language!")
	print(f'{Fore.GREEN}')

# Core Program # 

def translatesend():
	os.system('cls')
	channel_id = input(f'{userinputstyle} Channel ID: ')
	os.system('cls')
	print(f'{userinputstyle} 1 - Spanish')
	print(f'{userinputstyle} 2 - German')
	print(f'{userinputstyle} 3 - French')
	print()
	option = int(input())

	if option == 1:
		lang = 'es'

	if option == 2:
		lang = 'de'

	if option == 3:
		lang = 'fr'

	while True:
		os.system('cls')
		asciibanner()
		for i in range(10):
			userinput = input(f'{userinputstyle} {username}: ')
			if userinput == "~ChangeLang":
				translatesend()
			print()
			spantrans = (translator.translate(userinput, src='en', dest=lang).text)

			payload = {
				"content" : spantrans
			}

			requests.post('https://discord.com/api/v9/channels/{}/messages'.format(channel_id), headers=headers, json=payload)


if __name__ == "__main__":
	translatesend()


