import json
import random
import time
import urllib.request


def load_links():
    with open('data/images_links.json', 'r') as f:
        links = json.load(f)
    return links


def download_image(link_mimetype):
    link, mimetype = link_mimetype
    try:
        urllib.request.urlretrieve(
            link,
            f'data/images/{link.split("/")[-1]}.{mimetype.split("/")[-1]}')
        time.sleep(1)
    except Exception as e:
        print(e)
        print(link)


def download_images_parallel(links):
    i = 0
    for link_mimetype in links:
        download_image(link_mimetype)
        i += 1
        print(i)


if __name__ == '__main__':
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36')]
    urllib.request.install_opener(opener)
    links = load_links()
    links = [tuple(x) for x in links if
             x[1] in {'image/png', 'image/jpeg', 'image/jpg'}
             and x[0].startswith('http')]
    links = list(set(links))
    random.shuffle(links)
    print(len(links))
    download_images_parallel(links)
