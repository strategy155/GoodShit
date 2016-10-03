from definitions import ROOT_DIR,NAME_OF_NEWSPAPER,DEFAULT_ROOT,DEFAULT_PLAIN_TEXT,DEFAULT_MYSTEM_XML,DEFAULT_MYSTEM_PLAIN
import utils


def creating_directory_map():
    utils.create_directory_if_needed(DEFAULT_ROOT)
    utils.create_directory_if_needed(DEFAULT_PLAIN_TEXT)
    utils.create_directory_if_needed(DEFAULT_MYSTEM_XML)
    utils.create_directory_if_needed(DEFAULT_MYSTEM_PLAIN)


def main():
    creating_directory_map()


if __name__ == '__main__':
    main()