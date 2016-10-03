import utils
from definitions import ROOT_DIR, WEBPAGE_TYPE, ROOT_URL
ARTICLE_CLASS_DICT={"class":"box-reference-information"}


def _parse_root(root_url):
    req_page = utils.get_webpage(root_url)
    soup = utils.make_soup_with_webpage(req_page, WEBPAGE_TYPE)
    a=soup.find_all('div', attrs=ARTICLE_CLASS_DICT)
    print(a[0].a)

_parse_root(ROOT_URL)