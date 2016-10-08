import os
from definitions import DEFAULT_MAG_ROOT,DEFAULT_MYSTEM_PATH, DEFAULT_MYSTEM_XML
import subprocess
import utils


def _get_two_dirsname(path):
    first_folder=os.path.split(os.path.split(path)[0])[1]
    second_folder=os.path.split(os.path.split(os.path.split(path)[0])[0])[1]
    file_name=os.path.split(path)[1]
    return utils.produce_path(second_folder,utils.produce_path(first_folder,file_name))

for root, dirs, files in os.walk(DEFAULT_MAG_ROOT, topdown=False):
    for name in files:
        _path_to_file=os.path.join(root, name)
        _output_file=utils.produce_path(DEFAULT_MYSTEM_XML,_get_two_dirsname(_path_to_file))
        t=subprocess.Popen([DEFAULT_MYSTEM_PATH,_path_to_file,_output_file])
        t.wait()
        print(DEFAULT_MYSTEM_PATH, _path_to_file, _output_file)