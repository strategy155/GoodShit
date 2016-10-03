from definitions import ROOT_DIR,NAME_OF_NEWSPAPER
import utils


DEFAULT_ROOT=utils.produce_path(ROOT_DIR,NAME_OF_NEWSPAPER)
DEFAULT_PLAIN_TEXT=utils.produce_path(DEFAULT_ROOT,'plain')
DEFAULT_MYSTEM_XML=utils.produce_path(DEFAULT_ROOT,'mystem-xml')
DEFAULT_MYSTEM_PLAIN=utils.produce_path(DEFAULT_ROOT,'mystem-plain')


def creating_directory_map():
    utils.create_directory_if_needed(DEFAULT_ROOT)
    utils.create_directory_if_needed(DEFAULT_PLAIN_TEXT)
    utils.create_directory_if_needed(DEFAULT_MYSTEM_XML)
    utils.create_directory_if_needed(DEFAULT_MYSTEM_PLAIN)


def main():
    creating_directory_map()


if __name__ == '__main__':
    main()