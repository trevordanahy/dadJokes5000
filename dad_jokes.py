from pyfiglet import figlet_format
from termcolor import colored
import requests
from random import randint


prgm_title = colored(figlet_format('Dad Jokes 5000'),color='cyan')
print(prgm_title)

topic = input('Let me tell you a joke.  What do you want to hear a joke about?  ')
dad_url = 'https://icanhazdadjoke.com/search'

response = requests.get(
	dad_url, 
	headers={'Accept':'application/json'},
	params={'term':topic}).json()

total_jokes = response['total_jokes']
joke_select = randint(1,total_jokes)


if total_jokes == 0:
	print(f'I don\'t know any jokes about {topic}, go clean your room.')
elif total_jokes == 1:
	print(f'I know 1 joke about {topic}.')
	print(response['results'][joke_select-1]['joke'])
else:
	print(f'I know {total_jokes} about {topic}. Here\'s one')
	print(response['results'][joke_select-1]['joke'])



