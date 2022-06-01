import os
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


def get_info_page(path, headers, all_files):
    for n in range(len(all_files)):         
        f = str(path + "\\" + all_files[n])
        sheet_name = os.path.basename(f)
        with open(file=f, encoding='UTF-8', mode='r') as file:
            links = file.read().split('\n')
        
        wb = Workbook()
        ws = wb.active
        ws.title = "Data"
        ws.append(['Name', 'NCES FSCSKEY', 'Population Servied', 'City', 'State', 'Country', 'County', 
                'Mailing address line', 'Mailing Zip', 'Website link', 'Phone', 'libraries.org ID', 
                'NCES LIBID', 'Online catalog link', 'Collection size', 'Annual circulation', 'Permalink', 'Other Info'])
        
        for i in range(len(links) -1):
            url = links[i]
            response = requests.get(url=url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "xml")
                
                permalink = url
                name = soup('h2')[1].get_text().strip()
                if soup.find(string='NCES FSCSKEY') != None:
                    nces_fsckey = str(soup.find(string='NCES FSCSKEY').find_next('td').find('a').get('href'))[-6:]
                else:
                    nces_fsckey = 'None'
                if soup.find(string=' Service Population ') != None:
                    population = str(soup.find(string=' Service Population ').find_next('td')).strip('</td>')
                else:
                    population = 'None'
                city = soup.find_all('div', class_='librarydetails')[0].find('a').get_text().strip()
                state = str(soup.find('div', itemprop='address').find_all('a')[1].get_text()).strip()
                country = str(soup.find('div', itemprop='address').find(itemprop='addressCountry').get_text()).strip()
                county = str(soup.find('div', itemprop='address').find_all('a')[-2].get_text())
                if soup.find(string='Address: ').find_next(itemprop='streetAddress') != None:
                    address = soup.find(string='Address: ').find_next(itemprop='streetAddress').get_text().strip()
                else:
                    address = 'None'
                if soup.find('div', itemprop='address').find(itemprop='postalCode') != None:
                    zip_code = soup.find('div', itemprop='address').find(itemprop='postalCode').get_text().strip()
                else:
                    zip_code = 'None'
                if soup.find(string='Connect to: ') != None:
                    website_link = soup.find(string='Connect to: ').find_next('a').get('href')
                    online_catalog = soup.find(string='Connect to: ').find_next('a').find_next('a').get('href')
                else:
                    website_link = 'None'
                    online_catalog = 'None'
                libraries_org_ID = str(soup.find(string='libraries.org ID').find_next('td')).strip('</td>')
                if soup.find(string='NCES LIBID') != None:
                    nces_libid = str(soup.find(string='NCES LIBID').find_next('td')).strip('</td>')
                else:
                    nces_libid = 'None'
                if soup.find(string='Collection size') != None:
                    collection_size = str(soup.find(string='Collection size').find_next('td')).strip('</td>')
                else:
                    collection_size = 'None'
                if soup.find(string='Annual Circulation') != None:
                    annual_circulation = str(soup.find(string='Annual Circulation').find_next('td')).strip('</td>')
                else:
                    annual_circulation = 'None'
                if soup.find(string='OtherInfo:') != None:
                    other_info = soup.find(string='OtherInfo:').find_parent('p').get_text()
                else:
                    other_info = 'None'
                phone = str(soup.find(itemprop="telephone")).replace('<span itemprop="telephone">', '').strip('</span>').strip()
                
                ws.append([name, nces_fsckey, population, city, state, country, county, address, zip_code, 
                            website_link, phone, libraries_org_ID, nces_libid, online_catalog, collection_size, annual_circulation, 
                            permalink, other_info])
                
            wb.save(sheet_name.replace('.txt', '') + '.xlsx')
    

















  
        

    
    

    
    