import os
import requests
import bs4


def create_directory_if_needed(path):
    if not os.path.exists(path):
        os.makedirs(path)
    return None


def produce_path(path,directory):
    return os.path.join(path,directory)


def get_webpage(url):
    _imported_web_page = requests.get(url)
    _imported_web_page.encoding='utf-8'
    return _imported_web_page


def make_soup_with_webpage(input_webpage, webpage_type):
    _imported_web_page_in_soup=bs4.BeautifulSoup(input_webpage.text, webpage_type+'.parser')
    return _imported_web_page_in_soup


def get_list_of_tags_with_specified_atributes(soup, tag_name, spec_dict):
    _all_spec_headers = soup.find_all(name=tag_name, attrs={spec_dict['name']: spec_dict['attribute']})
    return _all_spec_headers


def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename