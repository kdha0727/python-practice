# example.py

import urllib.request


def url_open(string):
    print(urllib.request.urlopen(string).read().decode('utf-8'))


if __name__ == '__main__':
    url_open("http://www.example.com")
