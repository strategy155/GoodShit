import os
import utils
from templates import pm_article_name_template, simple_name_template


ARTICLE_TYPE = 'pop-mech-mag'
NAME_OF_NEWSPAPER='Популярная Механика'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WEBPAGE_TYPE = 'html'
ROOT_URL = 'http://www.popmech.ru/'
ARCHIVE_URL='http://www.popmech.ru/magazine/'
DEFAULT_ROOT=utils.produce_path(ROOT_DIR,NAME_OF_NEWSPAPER)
DEFAULT_PLAIN_TEXT=utils.produce_path(DEFAULT_ROOT,'plain')
DEFAULT_MYSTEM_XML=utils.produce_path(DEFAULT_ROOT,'mystem-xml')
DEFAULT_MYSTEM_PLAIN=utils.produce_path(DEFAULT_ROOT,'mystem-plain')
NAME_OF_FILETYPES={'pop-mech-mag': pm_article_name_template, 'usual-case':simple_name_template}