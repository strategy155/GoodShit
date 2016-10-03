import utils
import urllib.parse
from definitions import ROOT_DIR, WEBPAGE_TYPE, ROOT_URL, ARCHIVE_URL,DEFAULT_PLAIN_TEXT
MAG_CLASS_DICT={"class": "box-reference-information"}
ARTICLES_CLASS_DICT= {"class":"article-preview-title"}
TAG_NAME = 'div'


def _extract_spec_refs_from_page(root_url,spec_dict):
    _page_tags = utils.get_tags_with_special_attrs(root_url,WEBPAGE_TYPE,TAG_NAME,spec_dict)
    return _page_tags


def _download_from_refs(list_of_refs,target_path):
    for _target_ref in list_of_refs:
        utils.download_file(_target_ref,target_path)
    return None


def _convert_popmech_tags_to_refs(list_of_tags):
    _list_of_refs =[]
    for _tag in list_of_tags:
        _list_of_refs.append(_extract_link_popmech(_tag))
    return _list_of_refs


def _extract_link_popmech(div_tag):
    return urllib.parse.urljoin(ROOT_URL,div_tag.a['href'])


def main():
    _mag_tags=_extract_spec_refs_from_page(ARCHIVE_URL,MAG_CLASS_DICT)
    _mag_refs=_convert_popmech_tags_to_refs(_mag_tags)
    for mag in _mag_refs:
        magazin_string=str(mag)
        path=utils.produce_path(DEFAULT_PLAIN_TEXT,utils.produce_path(magazin_string.split('/')[-3],magazin_string.split('/')[-2]))
        article_tags=_extract_spec_refs_from_page(mag, ARTICLES_CLASS_DICT)
        article_refs=_convert_popmech_tags_to_refs(article_tags)
        utils.create_directory_if_needed(path)
        _download_from_refs(article_refs,path)


if __name__ == '__main__':
    main()
