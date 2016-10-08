import os
from templates import pm_article_name_template, simple_name_template


ARTICLE_TYPE = 'pop-mech-mag'
NAME_OF_NEWSPAPER='Популярная Механика'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WEBPAGE_TYPE = 'html'
ROOT_URL = 'http://www.popmech.ru/'
ARCHIVE_URL='http://www.popmech.ru/magazine/'
DEFAULT_MAG_ROOT=os.path.join(ROOT_DIR, NAME_OF_NEWSPAPER)
DEFAULT_PLAIN_TEXT=os.path.join(DEFAULT_MAG_ROOT, 'plain')
DEFAULT_MYSTEM_XML=os.path.join(DEFAULT_MAG_ROOT, 'mystem-xml')
DEFAULT_MYSTEM_PLAIN=os.path.join(DEFAULT_MAG_ROOT, 'mystem-plain')
DEFAULT_MYSTEM_PATH=os.path.join(ROOT_DIR,'mystem.exe')
NAME_OF_FILETYPES={'pop-mech-mag': pm_article_name_template, 'usual-case':simple_name_template}