def pm_article_name_template(url):
    _new_path=url.split('/')[-2].replace("-"," ")
    path_list = _new_path.split(' ')
    path_list.pop(0)
    path_list[0]=path_list[0].title()
    _new_path=' '.join(path_list)
    return _new_path


def simple_name_template(url):
    return url.split('/')[-1]