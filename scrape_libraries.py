import os
import scrape_first_page
import scrape_second_page
import scrape_libraries_info

URL = 'https://librarytechnology.org/libraries/uspublic'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
           }
path = r"D:\Python\project\scrape\state_links"

all_files = []
for files in os.listdir(path):
    all_files.append(files)

def main():
    # scrape_first_page.get_link_all_states(url=URL)
    # scrape_first_page.write_index_link_file()
    # scrape_second_page.get_links_all_state(headers=headers, url=URL)
    scrape_libraries_info.get_info_page(path=path, headers=headers, all_files=all_files)

if __name__ == '__main__':
    main()
