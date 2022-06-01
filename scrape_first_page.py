import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'Accept': 'image/avif,image/webp,*/*'
           }


def get_link_all_states(url):
    response = requests.get(url=url, headers=headers)

    with open(file='index.html', mode='w') as file:
        file.write(response.text)


# Writing state links to a file
def write_index_link_file():
    with open(file='index.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    data_soup = soup.find_all('table')[1].find_all('a')
    for i in range(len(data_soup)):
        res = str(data_soup[i])
        link = res[9: res.find('" ', 9)].strip()

        with open(file='list.txt', mode='a') as file:
            file.write(link + '\n')
