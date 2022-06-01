import requests
from bs4 import BeautifulSoup


def get_links_all_state(headers, url):
    with open(file='list.txt', encoding="utf-8") as file:
        src = file.read().split('\n')

    for i in range(52):
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        state = src[i][src[i].find('=') + 1:] + '.txt'
        n = len(soup.find_all('a'))
        for i in range(n):
            if soup.find_all('a')[i].get('href')[:9] == '/library/':
                with open(file=state, mode='a') as file:
                    file.write('https://librarytechnology.org' + soup.find_all('a')[i].get('href') + '\n')
              
                                        

