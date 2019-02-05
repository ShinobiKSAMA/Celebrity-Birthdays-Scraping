from bs4 import BeautifulSoup
import requests
import re

def BDayRe(month, day):
	url = "https://www.imdb.com/search/name?birth_monthday="+month+"-"+day+"&refine=birth_monthday&ref_=nv_cel_brn"
	imdb = requests.get(url)
	soup2 = BeautifulSoup(imdb.text, 'html.parser')
	imlinks = soup2.findAll('h3', class_='lister-item-header', limit=25)
	i = []
	for Bday in imlinks:
		i.append(re.sub(re.compile('<.*?>'), '', str(Bday)).replace('\n', ' '))
	for p in i:
		print(p)

print('\n')
month = input("Enter the Month Number : ")
day = input("Enter the Date : ")
print('\n')
BDayRe(month, day)
