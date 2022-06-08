import tika
from tika import parser


def tika_reader(file_path):
    raw_text = parser.from_file(file_path)
    raw_list = raw_text['content'].splitlines()
    return raw_list


def main():
    file_path = input()
    print(tika_reader(file_path))


if __name__ == '__main__':
    main()


# End of pdfreader_reader.py